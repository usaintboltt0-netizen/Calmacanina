# Método CalmaCanina — Landing Page

Landing page estática de venta para **Método CalmaCanina**, un producto digital sobre ansiedad por separación en perros.

🌐 **Sitio en vivo:** [https://juanzekerespaldokk-crypto.github.io/PaginaCanina/](https://juanzekerespaldokk-crypto.github.io/PaginaCanina/)

## Archivos incluidos

- `index.html`: estructura semántica completa, meta tags, Open Graph, secciones de confianza, oferta, FAQ, CTAs y sticky CTA mobile.
- `styles.css`: diseño responsive, paleta visual, animaciones, mockups, testimonios, sección autora y soporte para `prefers-reduced-motion`.
- `main.js`: link configurable de Mercado Pago, sticky header, smooth scroll, animaciones con Intersection Observer, acordeón FAQ, countdown, menú mobile, año dinámico y sticky CTA mobile.
- `gracias.html`: página post-compra con tarjetas de descarga (Guía Principal, Calendario 21 Días, Plantillas Rutina Diaria, Audios de Relajación, Videos ESP/ENG).
- `author-doctor-dog.svg`: imagen digital estilo IA de la doctora/autora con un perro, usada para reforzar confianza.
- `avatar-*.png` / `avatar-*.svg`: avatares de ejemplo para testimonios.
- `make_avatars.py`: script usado para generar los SVG de avatares.
- `generate_og.py`: script para generar la imagen Open Graph (`og-calmacanina.jpg`).

## Materiales del producto

- `Guia_Principal_CalmaCanina.pdf` — Guía principal del método.
- `Calendario_21_Dias_CalmaCanina.pdf` — Calendario de 21 días de práctica.
- `Plantillas_Rutina_Diaria_CalmaCanina.pdf` — Plantillas de rutina diaria.
- `Videos_CalmaCanina_Espanol.pdf` — Guía de videos en español.
- `Videos_CalmaCanina_English.pdf` — Guía de videos en inglés.

## Audios de relajación (Music/)

- `mindfulliving-celebration-vibrations-350640.mp3`
- `nourishedbymusic-peaceful-mantra-240925.mp3`
- `purebinaural-purebinaural-45-hz-theta-isochronic-tones-with-fores-rain-496538.mp3`
- `ribhavagrawal-pure-theta-4-7hz-rain-and-417hz-music-351390.mp3`
- `tim_kulig_free_music-celestial-theta-brainstems-232571.mp3`

## Multimedia

- `calmacanina-brand.mp4` — Video de marca CalmaCanina.
- `CRACKKK.mp4` — Testimonio/video promocional.
- `ESTAESPAÑOLAMEVAAHACERMILLONETA.mp4` — Video de la autora.
- `quienes-somos.mp4` — Sección "Quién está detrás del proyecto".
- `testimonio_final.mp4` — Testimonio final.

## Imágenes

- `BANNERPRINCIPAL.png` / `BANERMOVIL.png` — Banners principal y mobile.
- `NUEVOBANNER.jpg` — Banner alternativo nuevo.
- `Logo_Principal.png` — Logo de CalmaCanina.
- `CARAVISIBLEDEMARCA.png` — Cara visible de la marca.
- `author-valentina.jpg` — Foto de la autora Valentina.
- `og-calmacanina.jpg` — Imagen Open Graph generada.

## Cómo abrir localmente

Abrí `index.html` directamente en el navegador o ejecutá un servidor local:

```bash
python -m http.server 8080
```

Luego visitá: `http://localhost:8080`

## Integración con Mercado Pago y Shopify

Los botones de compra usan los atributos `data-checkout-link` (Mercado Pago) y `data-shopify-link` (Shopify). Los links se centralizan en `main.js`:

```js
const CHECKOUT_URL = "https://mpago.li/13CBR7U";
const SHOPIFY_URL = "https://ebooksaudiolibros.myshopify.com/";
```

Ambos métodos de pago aparecen en:
- Sección de pricing (#pricing)
- CTA final (sección 12)
- Sticky CTA mobile (solo Mercado Pago, por espacio)

Para cambiar los links, editá `CHECKOUT_URL` y `SHOPIFY_URL` en `main.js`. También podés reemplazar los `href` de respaldo en `index.html`, aunque `main.js` los actualiza automáticamente al cargar la página.

## Secciones principales

1. Hero con promesa y CTA.
2. Dolores/problemas frecuentes.
3. Presentación del producto y contenidos incluidos.
4. Método en 3 pasos.
5. Para quién es / para quién no es.
6. Sobre la autora (Valentina).
7. Quién está detrás del proyecto (video).
8. Historias y testimonios.
9. Bonos.
10. Qué pasa después de comprar.
11. Oferta, countdown, garantía y FAQ.
12. Sticky CTA mobile (Mercado Pago).

## Página de gracias (post-compra)

`gracias.html` incluye tarjetas de descarga para todos los materiales:
- Guía Principal
- Calendario 21 Días
- Plantillas de Rutina Diaria
- 5 Audios de Relajación
- Videos en Español
- Videos en Inglés

## Pendientes opcionales antes de escalar campañas

- Agregar Meta Pixel y Google Analytics si se van a hacer campañas pagas.
- Revisar testimonios y materiales públicos para que siempre tengan autorización de uso.
- Ajustar dominio, Open Graph image y email de soporte si se usa otro branding.

## Deploy con hosting propio

Podés subir estos archivos a Netlify, Vercel, GitHub Pages, Cloudflare Pages o cualquier hosting estático.

**El sitio se despliega automáticamente en GitHub Pages desde la rama `master`.**

## Nota legal

El contenido del método es educativo y no reemplaza una consulta veterinaria profesional. Si el perro presenta síntomas médicos, dolor, heridas, cambios bruscos de conducta o ansiedad severa, se recomienda consultar a un veterinario o profesional de comportamiento canino.