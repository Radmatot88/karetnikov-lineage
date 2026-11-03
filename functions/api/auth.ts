/**
 * Cloudflare Pages Function: /api/auth
 * Zero-Hardcode PBKDF2-HMAC-SHA256 verification against Environment Secrets (AUTH_SALT, AUTH_PASSWORD_HASH).
 * Never stores or logs plaintext passwords. Issues a signed HttpOnly; Secure; SameSite=Strict session cookie.
 */

export interface Env {
  AUTH_SALT: string;
  AUTH_PASSWORD_HASH: string;
  RELATIVE_AUTH_SALT?: string;
  RELATIVE_AUTH_PASSWORD_HASH?: string;
  AUTH_ITERATIONS?: string;
  SESSION_HMAC_SECRET: string;
}

function hexToBytes(hex: string): Uint8Array {
  const clean = hex.trim();
  const bytes = new Uint8Array(clean.length / 2);
  for (let i = 0; i < bytes.length; i++) {
    bytes[i] = parseInt(clean.substring(i * 2, i * 2 + 2), 16);
  }
  return bytes;
}

function bytesToHex(bytes: Uint8Array): string {
  return Array.from(bytes)
    .map((b) => b.toString(16).padStart(2, "0"))
    .join("");
}

function timingSafeEqualHex(a: string, b: string): boolean {
  if (a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) {
    diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  }
  return diff === 0;
}

export const onRequestPost: PagesFunction<Env> = async (context) => {
  try {
    const body = (await context.request.json()) as { password?: string };
    const password = body?.password || "";

    const saltHex = context.env.AUTH_SALT;
    const expectedHashHex = context.env.AUTH_PASSWORD_HASH;
    const iterations = parseInt(context.env.AUTH_ITERATIONS || "100000", 10);
    const hmacSecret = context.env.SESSION_HMAC_SECRET || "fallback-local-dev-only";

    if (!saltHex || !expectedHashHex) {
      return new Response(
        JSON.stringify({ ok: false, error: "Edge secrets not configured (.dev.vars)" }),
        { status: 500, headers: { "Content-Type": "application/json" } }
      );
    }

    const enc = new TextEncoder();
    const keyMaterial = await crypto.subtle.importKey(
      "raw",
      enc.encode(password),
      { name: "PBKDF2" },
      false,
      ["deriveBits"]
    );

    const derivedBits = await crypto.subtle.deriveBits(
      {
        name: "PBKDF2",
        salt: hexToBytes(saltHex),
        iterations,
        hash: "SHA-256"
      },
      keyMaterial,
      256
    );

    const computedHashHex = bytesToHex(new Uint8Array(derivedBits));
    let accessRole: "owner" | "relative_append_only" | null = null;

    if (timingSafeEqualHex(computedHashHex, expectedHashHex.toLowerCase())) {
      accessRole = "owner";
    } else if (context.env.RELATIVE_AUTH_SALT && context.env.RELATIVE_AUTH_PASSWORD_HASH) {
      const relDerivedBits = await crypto.subtle.deriveBits(
        {
          name: "PBKDF2",
          salt: hexToBytes(context.env.RELATIVE_AUTH_SALT),
          iterations,
          hash: "SHA-256"
        },
        keyMaterial,
        256
      );
      const relComputedHex = bytesToHex(new Uint8Array(relDerivedBits));
      if (timingSafeEqualHex(relComputedHex, context.env.RELATIVE_AUTH_PASSWORD_HASH.toLowerCase())) {
        accessRole = "relative_append_only";
      }
    }

    if (!accessRole) {
      return new Response(
        JSON.stringify({ ok: false, error: "Неверный ключ доступа к родовому архиву" }),
        { status: 401, headers: { "Content-Type": "application/json" } }
      );
    }

    // Issue HMAC-signed session token
    const exp = Math.floor(Date.now() / 1000) + 60 * 60 * 12; // 12 hours
    const payloadStr = `karetnikov_ sovereign_${exp}`;
    const hmacKey = await crypto.subtle.importKey(
      "raw",
      enc.encode(hmacSecret),
      { name: "HMAC", hash: "SHA-256" },
      false,
      ["sign"]
    );
    const sigBits = await crypto.subtle.sign("HMAC", hmacKey, enc.encode(payloadStr));
    const sigHex = bytesToHex(new Uint8Array(sigBits));
    const cookieVal = `${exp}.${sigHex}`;

    return new Response(JSON.stringify({ ok: true, access_role: accessRole, exp }), {
      status: 200,
      headers: {
        "Content-Type": "application/json",
        "Set-Cookie": `kh_fortress_session=${cookieVal}; Path=/; HttpOnly; Secure; SameSite=Strict; Max-Age=43200`
      }
    });
  } catch {
    return new Response(JSON.stringify({ ok: false, error: "Invalid request" }), {
      status: 400,
      headers: { "Content-Type": "application/json" }
    });
  }
};
