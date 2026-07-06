document.addEventListener("DOMContentLoaded", () => {

    /* ═══ MUSIC PLAYER ═══ */
    const audio = document.createElement("audio");
    audio.id = "relax-audio";
    audio.loop = true;
    audio.preload = "none";
    document.body.appendChild(audio);

    const TRACKS = [
        "Music/ribhavagrawal-pure-theta-4-7hz-rain-and-417hz-music-351390.mp3",
        "Music/nourishedbymusic-peaceful-mantra-240925.mp3"
    ];
    let trackIdx = 0;

    const audioBars = document.querySelectorAll(".mock-audio-bar");

    audioBars.forEach(bar => {
        bar.addEventListener("click", function onClick() {
            if (audio.paused) {
                trackIdx = (trackIdx + 1) % TRACKS.length;
                audio.src = TRACKS[trackIdx];
                audio.play().catch(() => { });
                audioBars.forEach(b => b.classList.add("playing"));
                this.querySelector(".mock-audio-badge").textContent = "▶ REPRODUCIENDO";
            } else {
                audio.pause();
                audioBars.forEach(b => {
                    b.classList.remove("playing");
                    b.querySelector(".mock-audio-badge").textContent = "BONO";
                });
            }
        });
    });

    /* ═══ CONFIGURACIÓN DE PAGO ═══
       1) En Mercado Pago creá un "Link de pago" por $47 USD o su equivalente.
       2) Copiá el link generado.
       3) Pegalo abajo reemplazando el valor de CHECKOUT_URL.
       Ejemplos válidos: https://mpago.la/XXXXXXX o https://link.mercadopago.com/tuusuario */
    const CHECKOUT_URL = "https://link.mercadopago.com.ar/calmacaninos";

    document.querySelectorAll("[data-checkout-link]").forEach(link => {
        link.setAttribute("href", CHECKOUT_URL);
    });

    /* ═══ 1. STICKY HEADER ═══ */
    const header = document.getElementById("site-header");
    const onScroll = () => header.classList.toggle("scrolled", window.scrollY > 60);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });

    /* ═══ 2. SMOOTH SCROLL ═══ */
    document.querySelectorAll(".cta-link, .nav-links a[href^='#']").forEach(link => {
        link.addEventListener("click", (e) => {
            const href = link.getAttribute("href");
            if (!href || !href.startsWith("#")) return;
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: "smooth", block: "start" });
                document.getElementById("nav-links")?.classList.remove("open");
            }
        });
    });

    /* ═══ 3. INTERSECTION OBSERVER ═══ */
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add("visible");
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.15, rootMargin: "-50px" });

    /* ═══ 4. STAGGERED PAIN ITEMS ═══ */
    document.querySelectorAll(".pain-item").forEach((el, i) => {
        el.style.transitionDelay = `${i * 0.12}s`;
        observer.observe(el);
    });

    /* Observe cards */
    document.querySelectorAll(".step-card, .fit-card, .testimonial-card, .bonus-card, .after-card").forEach(el => observer.observe(el));

    /* ═══ 5. FAQ ACCORDION ═══ */
    document.querySelectorAll(".faq-btn").forEach(btn => {
        btn.addEventListener("click", () => {
            const item = btn.closest(".faq-item");
            document.querySelectorAll(".faq-item").forEach(faq => {
                if (faq !== item) {
                    faq.classList.remove("active");
                    faq.querySelector(".faq-btn").setAttribute("aria-expanded", "false");
                }
            });
            const isActive = item.classList.toggle("active");
            btn.setAttribute("aria-expanded", String(isActive));
        });
    });

    /* ═══ 7. MOBILE MENU TOGGLE ═══ */
    const menuToggle = document.getElementById("menu-toggle");
    const navLinks = document.getElementById("nav-links");
    if (menuToggle && navLinks) {
        const setMenuState = (isOpen) => {
            navLinks.classList.toggle("open", isOpen);
            menuToggle.classList.toggle("active", isOpen);
            menuToggle.setAttribute("aria-expanded", String(isOpen));
            menuToggle.setAttribute("aria-label", isOpen ? "Cerrar menú" : "Abrir menú");
            document.body.style.overflow = isOpen ? "hidden" : "";
        };

        menuToggle.addEventListener("click", () => setMenuState(!navLinks.classList.contains("open")));

        navLinks.querySelectorAll("a").forEach(link => {
            link.addEventListener("click", () => setMenuState(false));
        });

        document.addEventListener("click", (event) => {
            if (!navLinks.classList.contains("open")) return;
            if (navLinks.contains(event.target) || menuToggle.contains(event.target)) return;
            setMenuState(false);
        });
    }

    /* ═══ 8. DYNAMIC FOOTER YEAR ═══ */
    const yearEl = document.getElementById("footer-year");
    if (yearEl) yearEl.textContent = new Date().getFullYear();

    /* ═══ 9. TESTIMONIOS ═══
       Se dejaron fijos para cargar más rápido y evitar dependencias externas. */

    /* ═══ 9. COUNTDOWN ═══
       Fecha objetivo: 7 días desde la primera carga del usuario.
       Se persiste en localStorage para que no se reinicie al recargar. */
    const countdownEl = document.getElementById("countdown");
    if (countdownEl) {
        const STORAGE_KEY = "cc_countdown_end";
        let endTime = localStorage.getItem(STORAGE_KEY);
        if (!endTime) {
            const target = new Date();
            target.setDate(target.getDate() + 7);
            target.setHours(23, 59, 59, 0);
            endTime = target.getTime().toString();
            localStorage.setItem(STORAGE_KEY, endTime);
        }
        endTime = parseInt(endTime, 10);

        const pad = n => String(n).padStart(2, "0");
        const updateCountdown = () => {
            const diff = Math.max(0, endTime - Date.now());
            const d = Math.floor(diff / 86400000);
            const h = Math.floor((diff % 86400000) / 3600000);
            const m = Math.floor((diff % 3600000) / 60000);
            const s = Math.floor((diff % 60000) / 1000);
            document.getElementById("cd-days").textContent = pad(d);
            document.getElementById("cd-hours").textContent = pad(h);
            document.getElementById("cd-minutes").textContent = pad(m);
            document.getElementById("cd-seconds").textContent = pad(s);

            if (diff <= 0) {
                // Countdown expirado — reiniciar para próxima visita
                localStorage.removeItem(STORAGE_KEY);
            }
        };
        updateCountdown();
        setInterval(updateCountdown, 1000);
    }

    /* ═══ 10. STICKY MOBILE CTA ═══ */
    const stickyCta = document.getElementById("sticky-cta-mobile");
    const heroSection = document.getElementById("hero");
    const pricingSection = document.getElementById("pricing");
    if (stickyCta && heroSection) {
        const checkSticky = () => {
            const heroBottom = heroSection.getBoundingClientRect().bottom;
            const pricingTop = pricingSection ? pricingSection.getBoundingClientRect().top : Infinity;
            // Show after hero passes, hide when pricing is visible
            const show = heroBottom < 0 && pricingTop > window.innerHeight;
            stickyCta.classList.toggle("visible", show);
        };
        window.addEventListener("scroll", checkSticky, { passive: true });
        checkSticky();
    }
});