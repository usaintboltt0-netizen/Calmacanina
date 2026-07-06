# Método CalmaCanina — Landing Page

Landing page estática de venta para **Método CalmaCanina**, un producto digital sobre ansiedad por separación en perros.

## Archivos incluidos

- `index.html`: estructura semántica completa, meta tags, Open Graph, secciones de confianza, oferta, FAQ, CTAs y sticky CTA mobile.
- `styles.css`: diseño responsive, paleta visual, animaciones, mockups, testimonios, sección autora y soporte para `prefers-reduced-motion`.
- `main.js`: link configurable de Mercado Pago, sticky header, smooth scroll, animaciones con Intersection Observer, acordeón FAQ, countdown, menú mobile, año dinámico y sticky CTA mobile.
- `author-doctor-dog.svg`: imagen digital estilo IA de la doctora/autora con un perro, usada para reforzar confianza.
- `avatar-*.png` / `avatar-*.svg`: avatares de ejemplo para testimonios.
- `make_avatars.py`: script usado para generar los SVG de avatares.

## Cómo abrir localmente

Abrí `index.html` directamente en el navegador o ejecutá un servidor local:

```bash
python -m http.server 8080
```

Luego visitá: `http://localhost:8080`

## Integración con Mercado Pago

Los botones de compra que salen a checkout usan el atributo `data-checkout-link`. El link se centraliza en `main.js`:

```js
const CHECKOUT_URL = "https://link.mercadopago.com/calmacanina-demo";
```

Ese link actual es **ficticio/demo** para revisar el procedimiento visual. Antes de publicar o correr anuncios, reemplazalo por tu link real de Mercado Pago, por ejemplo:

```js
const CHECKOUT_URL = "https://mpago.la/TU_LINK_REAL";
```

También podés reemplazar los `href` de respaldo en `index.html`, aunque `main.js` los actualiza automáticamente al cargar la página.

## Secciones principales

1. Hero con promesa y CTA.
2. Dolores/problemas frecuentes.
3. Presentación del producto y contenidos incluidos.
4. Método en 3 pasos.
5. Para quién es / para quién no es.
6. Sobre la autora.
7. Testimonios de ejemplo.
8. Bonos.
9. Qué pasa después de comprar.
10. Oferta, countdown, garantía y FAQ.

## Pendientes antes de publicar

- Reemplazar el link ficticio de Mercado Pago por el link real de cobro.
- Agregar Meta Pixel y Google Analytics en los placeholders del `<head>` si se van a hacer campañas.
- Cambiar testimonios ficticios por testimonios reales con autorización.
- Ajustar dominio, Open Graph image y email de soporte si se usa otro branding.

## Deploy con hosting propio

Podés subir estos archivos a Netlify, Vercel, GitHub Pages, Cloudflare Pages o cualquier hosting estático.

## Nota legal

Los testimonios actuales son ejemplos comerciales editables. Reemplazalos por testimonios reales antes de campañas pagas para evitar problemas de cumplimiento publicitario.