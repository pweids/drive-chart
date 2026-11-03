// Cloudflare Worker: relays ESPN's NFL feed with CORS headers.
// Deploy, then paste the worker's URL into Drive Chart > Data source.
export default {
  async fetch(req) {
    const u = new URL(req.url);
    if (!u.pathname.startsWith("/apis/site/v2/sports/football/nfl/"))
      return new Response("Not found", { status: 404 });
    const r = await fetch("https://site.api.espn.com" + u.pathname + u.search, { cf: { cacheTtl: 10 } });
    const h = new Headers(r.headers);
    h.set("Access-Control-Allow-Origin", "*");
    return new Response(r.body, { status: r.status, headers: h });
  },
};
