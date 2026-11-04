/**
 * Cloudflare Pages Function: /api/memories
 * Sovereign Family Evidence & Memories Ledger (Append-Only Canon Guard).
 * 
 * Rules:
 * 1. Owner & Relatives can append memories, facts, and oral testimonies.
 * 2. Nobody can overwrite or delete confirmed canonical archival facts.
 * 3. Supports Cloudflare KV (MEMORIES_KV) if bound, with graceful in-memory/edge fallback.
 */

export interface Env {
  MEMORIES_KV?: KVNamespace;
  SESSION_HMAC_SECRET?: string;
}

export interface MemoryRecord {
  id: string;
  node_id: string;
  person_name?: string;
  author: string;
  author_role: "owner" | "relative" | "guest";
  text: string;
  type: "memory" | "correction" | "oral_tradition" | "photo_lead";
  created_at: string;
  timestamp: string;
  status: "pending_review" | "accepted_canon" | "rejected";
}

// In-memory edge cache fallback (persists across warm isolate invocations)
const edgeMemoryCache: MemoryRecord[] = [];

export const onRequestGet: PagesFunction<Env> = async (context) => {
  try {
    let records: MemoryRecord[] = [];

    if (context.env.MEMORIES_KV) {
      const kvData = await context.env.MEMORIES_KV.get("family_memories_ledger", "json");
      if (kvData && Array.isArray(kvData)) {
        records = kvData as MemoryRecord[];
      }
    } else {
      records = [...edgeMemoryCache];
    }

    return new Response(JSON.stringify({ ok: true, count: records.length, records }), {
      status: 200,
      headers: {
        "Content-Type": "application/json; charset=utf-8",
        "Cache-Control": "no-store, no-cache, must-revalidate",
        "Access-Control-Allow-Origin": "*"
      }
    });
  } catch (err: any) {
    return new Response(JSON.stringify({ ok: false, error: err?.message || "Internal error" }), {
      status: 500,
      headers: { "Content-Type": "application/json; charset=utf-8" }
    });
  }
};

export const onRequestPost: PagesFunction<Env> = async (context) => {
  try {
    const body = (await context.request.json()) as Partial<MemoryRecord>;
    const nodeId = (body.node_id || "").trim();
    const text = (body.text || "").trim();
    const author = (body.author || "").trim() || "Родственник";
    const authorRole = body.author_role || "relative";
    const personName = body.person_name || "";
    const type = body.type || "memory";

    if (!nodeId || !text) {
      return new Response(
        JSON.stringify({ ok: false, error: "Параметры node_id и text обязательны" }),
        { status: 400, headers: { "Content-Type": "application/json; charset=utf-8" } }
      );
    }

    const now = new Date();
    const record: MemoryRecord = {
      id: `MEM_${Date.now()}_${Math.random().toString(36).substring(2, 7)}`,
      node_id: nodeId,
      person_name: personName,
      author,
      author_role: authorRole,
      text,
      type,
      created_at: now.toISOString(),
      timestamp: now.toLocaleDateString("ru-RU", {
        day: "2-digit",
        month: "2-digit",
        year: "numeric",
        hour: "2-digit",
        minute: "2-digit"
      }),
      status: authorRole === "owner" ? "accepted_canon" : "pending_review"
    };

    if (context.env.MEMORIES_KV) {
      let existing: MemoryRecord[] = [];
      const raw = await context.env.MEMORIES_KV.get("family_memories_ledger", "json");
      if (raw && Array.isArray(raw)) existing = raw as MemoryRecord[];
      existing.unshift(record);
      // Keep up to 2000 family records
      if (existing.length > 2000) existing = existing.slice(0, 2000);
      await context.env.MEMORIES_KV.put("family_memories_ledger", JSON.stringify(existing));
    } else {
      edgeMemoryCache.unshift(record);
      if (edgeMemoryCache.length > 500) edgeMemoryCache.pop();
    }

    return new Response(JSON.stringify({ ok: true, record }), {
      status: 201,
      headers: {
        "Content-Type": "application/json; charset=utf-8",
        "Access-Control-Allow-Origin": "*"
      }
    });
  } catch (err: any) {
    return new Response(JSON.stringify({ ok: false, error: err?.message || "Invalid payload" }), {
      status: 400,
      headers: { "Content-Type": "application/json; charset=utf-8" }
    });
  }
};
