/**
 * Cloudflare Pages Edge Security Middleware (Astro Fortress 2026 Standard)
 * Enforces anti-indexing, anti-scraping, and security headers at the Cloudflare Edge.
 */

export interface Env {
  AUTH_SALT?: string;
  AUTH_PASSWORD_HASH?: string;
  AUTH_ITERATIONS?: string;
  SESSION_HMAC_SECRET?: string;
}

const AI_SCRAPER_REGEX = /(GPTBot|ClaudeBot|PerplexityBot|CCBot|Bytespider|Anthropic|Scrapy|HeadlessChrome)/i;

export const onRequest: PagesFunction<Env> = async (context) => {
  const { request, next } = context;
  const ua = request.headers.get("user-agent") || "";

  // 1. Block known AI scrapers and unauthorized bots at the Edge
  if (AI_SCRAPER_REGEX.test(ua) && !ua.includes("PlaywrightLocalQA")) {
    return new Response("403 Forbidden — Sovereign Heritage Fortress Gate", {
      status: 403,
      headers: {
        "Content-Type": "text/plain; charset=utf-8",
        "X-Robots-Tag": "noindex, nofollow, noarchive"
      }
    });
  }

  const response = await next();
  const newHeaders = new Headers(response.headers);

  // 2. Enforce Astro Fortress security headers
  newHeaders.set("X-Robots-Tag", "noindex, nofollow, noarchive, nosnippet");
  newHeaders.set("X-Frame-Options", "DENY");
  newHeaders.set("X-Content-Type-Options", "nosniff");
  newHeaders.set("Referrer-Policy", "no-referrer");

  return new Response(response.body, {
    status: response.status,
    statusText: response.statusText,
    headers: newHeaders
  });
};
