# Método Calma Canina™ — Landing Page

Landing page estática de venta para **Método Calma Canina™**, un producto digital sobre ansiedad por separación en perros.

🌐 **Sitio en vivo:** [https://usaintboltt0-netizen.github.io/Calmacanina/](https://usaintboltt0-netizen.github.io/Calmacanina/)

## Archivos incluidos

- `index.html`: estructura semántica completa con hero emocional, sección de problema/dolores, cuadrícula de solución, testimoniales, FAQ, pricing, garantía, sticky CTA mobile y schema.org Product + FAQPage structured data.
- `styles.css`: diseño responsive, paleta visual (verde bosque/dorado), animaciones fade-in, mockups de producto, testimonios, acordeón FAQ, soporte `prefers-reduced-motion`.
- `main.js`: configuración centralizada de Mercado Pago y Shopify, sticky header, smooth scroll, Intersection Observer para animaciones, acordeón FAQ, countdown de 7 días con localStorage, menú mobile, año dinámico en footer y sticky CTA mobile.
- `gracias.html`: página post-compra con tarjetas de descarga para Guía Principal, Calendario 21 Días, Plantillas Rutina Diaria, Audios de Relajación, Videos ESP/ENG.
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

- `PRESENTACION DE LA MEDICA.mp4` — Video de presentación de la médica/fundadora.
- `quienes-somos.mp4` — Video institucional "Quién está detrás del proyecto".
- `CLIENTESATISFECHO1.mp4` — Testimonio en video de cliente satisfecho.
- `CLIENTESATISFECHO2.mp4` — Testimonio en video de cliente satisfecho.
- `testimonio_1.mp4` a `testimonio_9.mp4` — Testimonios en video adicionales.
- `testimonio_final.mp4` — Testimonio final.

## Imágenes

- `BANNERPRINCIPAL.png` / `BANERMOVIL.png` — Banners principal y mobile.
- `NUEVOBANNER.jpg` — Banner alternativo.
- `Logo_Principal.png` — Logo de Calma Canina.
- `CARAVISIBLEDEMARCA.png` — Cara visible de la marca.
- `og-calmacanina.jpg` — Imagen Open Graph generada (1200×630px).
- `author-doctor-dog.svg` / `author-valentina.jpg` — Imágenes de la autora/doctora.
- `avatar-*.png` / `avatar-*.svg` — Avatares para testimonios (María, Carlos, Luciana, Sofía).
- `make_avatars.py` — Script para generar los SVG de avatares.

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
- Cierre emocional (sección 13)
- Sticky CTA mobile (solo Mercado Pago, por espacio)

Para cambiar los links, editá `CHECKOUT_URL` y `SHOPIFY_URL` en `main.js`.

## Secciones principales

1. **Hero** con promesa emocional, mockup del producto y trust strip (⭐ +500 dueños, método positivo, acceso inmediato, compra segura).
2. **Trust Strip** horizontal con indicadores de confianza (+2.500 familias, método positivo, 4.9/5 estrellas, etc.).
3. **Problema** (pain points): señales de ansiedad canina conector emocional.
4. **Solución**: grid de 6 beneficios del método (tranquilidad, comunicación, rutinas, ejercicios, confianza, resultados).
5. **Método en 3 pasos**: diagnosticar, aplicar rutina, monitorear y ajustar.
6. **Producto**: descripción completa del programa con mockup y checklist de incluídos.
7. **Quiénes Somos**: video de presentación de la médica + video institucional.
8. **Testimonios**: cards con avatares + video testimonials grid.
9. **Garantía**: garantía de 30 días con escudo visual.
10. **Confianza/Compra Segura**: encriptación SSL, entrega inmediata, método respetuoso.
11. **FAQ**: acordeón con preguntas frecuentes.
12. **Pricing**: comparativa de valor, precio con countdown, opciones Mercado Pago ($40 USD) y Shopify ($47 USD).
13. **Cierre Emocional**: llamado a la acción final con garantía.
14. **Footer**: navegación, soporte, disclaimer legal.
15. **Sticky CTA Mobile**: barra inferior fija con botón de compra.

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
- Restaurar `FAQPage` structured data si se requiere para SEO avanzado (fue simplificado a solo `Product` schema).

## Deploy con hosting propio

Podés subir estos archivos a Netlify, Vercel, GitHub Pages, Cloudflare Pages o cualquier hosting estático.

**El sitio se despliega automáticamente en GitHub Pages desde la rama `master` (o `gh-pages`).**

## Nota legal

El contenido del método es educativo y no reemplaza una consulta veterinaria profesional. Si el perro presenta síntomas médicos, dolor, heridas, cambios bruscos de conducta o ansiedad severa, se recomienda consultar a un veterinario o profesional de comportamiento canino.