# Drive Chart

Spoiler-safe NFL drive tracker for watching on delay. Open `index.html` from GitHub Pages on a phone.

- Data: ESPN's public site API (`site.api.espn.com`), unofficial and subject to change.
- If the browser can't reach ESPN, deploy `worker.js` as a Cloudflare Worker and paste its URL under **Data source** in the page.

## Editing

Edit `app.html`, then run `python3 build.py` to regenerate `index.html` (adds the doctype and mobile viewport tags). Commit both.
