# Mizar d.o.o. Celje — redesign pitch

Static site, redesign of mizar-celje.com. Open `index.html` through any static server, e.g. `python3 -m http.server`.

- Pages are generated from `build.py` (shared header, mega menu, contact and footer). Edit content there, then run `python3 build.py`.
- Styles: `assets/css/site.css`, motion: `assets/js/site.js` (GSAP + ScrollTrigger + Lenis, bundled locally).
- Font: Switzer (Fontshare, free licence), `assets/fonts/`.
- Images: `assets/img/` are Mizar's own photos and logo; `assets/gen/` are generated editorial stills (Higgsfield, Seedream 5 Pro / GPT Image).
- Pages carry `noindex` while this is a pitch. The contact form is a front-end demo only.
