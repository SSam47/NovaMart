import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# --- 1. Update CSS: Reverse Marquee + Add Complete Alive Suite for all product images ---
old_marquee_kf = "@keyframes marqueeScroll{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}"
new_marquee_kf = "@keyframes marqueeScroll{0%{transform:translateX(-50%)}100%{transform:translateX(0%)}}"

assert old_marquee_kf in html, "Could not find old_marquee_kf"
html = html.replace(old_marquee_kf, new_marquee_kf)

# Replace breathing CSS block with enhanced Alive Always product animations
old_breathing_css = """/* Motion graphics & Breathable idle animation */
@keyframes breatheSlow {
  0% { transform: translateY(0px) rotate(0deg) scale(1); }
  50% { transform: translateY(-14px) rotate(0.8deg) scale(1.018); }
  100% { transform: translateY(0px) rotate(0deg) scale(1); }
}
@keyframes floatWordA {
  0%, 100% { transform: translate3d(0, 0, 0); }
  50% { transform: translate3d(-18px, -12px, 0); }
}
@keyframes floatWordB {
  0%, 100% { transform: translate3d(0, 0, 0); }
  50% { transform: translate3d(20px, 14px, 0); }
}
@keyframes floatWordEdge {
  0%, 100% { transform: translate3d(0, 0, 0); }
  50% { transform: translate3d(-14px, 0, 0); }
}

.hx-a {
  animation: floatWordA 12s ease-in-out infinite alternate;
}
.hx-b {
  animation: floatWordB 14s ease-in-out infinite alternate;
}
.edge span {
  animation: floatWordEdge 16s ease-in-out infinite alternate;
}
@keyframes breatheGentle {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-5px); }
}
@keyframes floatSubtle {
  0%, 100% { transform: translate3d(0, 0, 0); }
  50% { transform: translate3d(0, -6px, 0); }
}
@keyframes glowPulse {
  0%, 100% { filter: drop-shadow(0 14px 28px rgba(44,33,24,.12)); }
  50% { filter: drop-shadow(0 22px 36px rgba(155,111,67,.24)); }
}

/* Idle breathable animation applies smoothly to showcase elements */
.hx-product-wrap {
  position: absolute;
  inset: 0;
  animation: breatheSlow 6.5s ease-in-out infinite alternate, glowPulse 8s ease-in-out infinite alternate;
  will-change: transform;
}
.order-img, .fits-img {
  animation: breatheGentle 7s ease-in-out infinite alternate;
}
.plan.on {
  animation: floatSubtle 5s ease-in-out infinite alternate;
}
.wa-float:not(:hover) {
  animation: breatheGentle 4s ease-in-out infinite alternate;
}"""

new_breathing_css = """/* Motion graphics & ALIVE ALWAYS product animations */
@keyframes breatheSlow {
  0% { transform: translateY(0px) rotate(0deg) scale(1); }
  50% { transform: translateY(-14px) rotate(0.8deg) scale(1.02); }
  100% { transform: translateY(0px) rotate(0deg) scale(1); }
}
@keyframes floatWordA {
  0%, 100% { transform: translate3d(0, 0, 0); }
  50% { transform: translate3d(18px, 12px, 0); }
}
@keyframes floatWordB {
  0%, 100% { transform: translate3d(0, 0, 0); }
  50% { transform: translate3d(-20px, -14px, 0); }
}
@keyframes floatWordEdge {
  0%, 100% { transform: translate3d(0, 0, 0); }
  50% { transform: translate3d(16px, 0, 0); }
}

.hx-a {
  animation: floatWordA 12s ease-in-out infinite alternate;
}
.hx-b {
  animation: floatWordB 14s ease-in-out infinite alternate;
}
.edge span {
  animation: floatWordEdge 16s ease-in-out infinite alternate;
}

/* Continuous alive organic breathing cycles for all product images */
@keyframes productAliveA {
  0%, 100% { transform: translateY(0px) scale(1) rotate(0deg); }
  50% { transform: translateY(-8px) scale(1.025) rotate(0.4deg); }
}
@keyframes productAliveB {
  0%, 100% { transform: translateY(0px) scale(1) rotate(0deg); }
  50% { transform: translateY(-7px) scale(1.022) rotate(-0.5deg); }
}
@keyframes productAliveC {
  0%, 100% { transform: translateY(0px) scale(1); }
  50% { transform: translateY(-6px) scale(1.02); }
}
@keyframes cinemagraphAlive {
  0%, 100% { transform: scale(1.02); }
  50% { transform: scale(1.05) translateY(-4px); }
}
@keyframes glowPulse {
  0%, 100% { filter: drop-shadow(0 14px 28px rgba(44,33,24,.12)); }
  50% { filter: drop-shadow(0 24px 40px rgba(155,111,67,.32)); }
}

/* ALL PRODUCT IMAGES ALIVE ALWAYS */
.hx-product-wrap {
  position: absolute;
  inset: 0;
  animation: breatheSlow 6.5s ease-in-out infinite alternate, glowPulse 8s ease-in-out infinite alternate;
  will-change: transform;
}

/* Story pinned product images constantly alive */
.story-media .sc img {
  animation: cinemagraphAlive 7.5s ease-in-out infinite alternate;
  will-change: transform;
}

/* Anatomy product showcase and cards constantly alive */
.anat-grid .a-main img {
  animation: productAliveA 6.8s ease-in-out infinite alternate, glowPulse 9s ease-in-out infinite alternate;
  will-change: transform, filter;
}
.anat-grid .a:not(.a-main):nth-child(odd) img {
  animation: productAliveB 6.2s ease-in-out infinite alternate;
  will-change: transform;
}
.anat-grid .a:not(.a-main):nth-child(even) img {
  animation: productAliveC 7s ease-in-out infinite alternate;
  will-change: transform;
}

/* Fits section product showcase alive */
.fits-img picture, .fits-img img {
  animation: productAliveA 7.2s ease-in-out infinite alternate, glowPulse 8.5s ease-in-out infinite alternate;
  will-change: transform, filter;
}

/* Lifestyle editorial product imagery continuous living depth */
.lf:nth-child(1) img {
  animation: cinemagraphAlive 8.5s ease-in-out infinite alternate;
  will-change: transform;
}
.lf:nth-child(2) img {
  animation: cinemagraphAlive 7.8s ease-in-out infinite alternate;
  will-change: transform;
}
.lf:nth-child(3) img {
  animation: cinemagraphAlive 8.2s ease-in-out infinite alternate;
  will-change: transform;
}

/* Gallery product grid images all staggered and alive always */
.g figure:nth-child(1) img { animation: productAliveA 6.4s ease-in-out infinite alternate; will-change: transform; }
.g figure:nth-child(2) img { animation: productAliveB 7.2s ease-in-out infinite alternate; will-change: transform; }
.g figure:nth-child(3) img { animation: productAliveC 6.0s ease-in-out infinite alternate; will-change: transform; }
.g figure:nth-child(4) img { animation: productAliveA 7.6s ease-in-out infinite alternate; will-change: transform; }
.g figure:nth-child(5) img { animation: productAliveB 6.8s ease-in-out infinite alternate; will-change: transform; }
.g figure:nth-child(6) img { animation: productAliveC 7.4s ease-in-out infinite alternate; will-change: transform; }
.g figure:nth-child(7) img { animation: productAliveA 8.0s ease-in-out infinite alternate; will-change: transform; }

.plan.on {
  animation: productAliveC 5s ease-in-out infinite alternate;
}
.wa-float:not(:hover) {
  animation: productAliveC 4s ease-in-out infinite alternate;
}"""

assert old_breathing_css in html, "Could not find old_breathing_css"
html = html.replace(old_breathing_css, new_breathing_css)

# --- 2. Update JavaScript: Reverse All Scroll / Scrub Animations Across the Whole Website ---
old_js_block = """    gsap.to('.hx-a', { xPercent: -14, ease: 'none', scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: true } });
    gsap.to('.hx-b', { xPercent: 10, ease: 'none', scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: true } });
    $$('.edge span').forEach((e, i) => gsap.fromTo(e, { xPercent: i % 2 ? -18 : 0 }, { xPercent: i % 2 ? 0 : -18, ease: 'none', scrollTrigger: { trigger: e.closest('section'), start: 'top bottom', end: 'bottom top', scrub: true } }));
    gsap.to('.hx-stage', { yPercent: 8, ease: 'none', scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: true } });
    if (reduce) return;

    // line-by-line headline reveals (reverse when scrolled back)
    $$('.lines').forEach(h => { if (h.closest('.hero')) return;
      gsap.from($$('i', h), { yPercent: 105, duration: 1, stagger: .09, ease: 'power4.out',
        scrollTrigger: { trigger: h, start: 'top 88%', toggleActions: 'play none none reverse' } });
    });

    // pinned 5-scene story, fully scrubbed (reverses with scroll)
    const sc = $$('.sc'), st = $$('.st'), n = sc.length;
    const tl = gsap.timeline({ defaults: { ease: 'none' }, scrollTrigger: { trigger: '.story', start: 'top top', end: 'bottom bottom', scrub: .6 } });
    tl.fromTo($('img', sc[0]), { scale: 1.15 }, { scale: 1.02, duration: 1 }, 0)
      .fromTo('.story-media', { xPercent: 0 }, { xPercent: -3, duration: n }, 0);
    for (let i = 1; i < n; i++) {
      const t = i - .45;
      tl.fromTo(sc[i], { clipPath: 'inset(100% 0% 0% 0%)' }, { clipPath: 'inset(0% 0% 0% 0%)', duration: .55, ease: 'power2.inOut' }, t)
        .fromTo($('img', sc[i]), { scale: 1.15, yPercent: 4 }, { scale: 1.02, yPercent: 0, duration: 1.1 }, t)
        .to($('img', sc[i - 1]), { yPercent: -6, duration: .55 }, t)
        .to(st[i - 1], { opacity: 0, y: -40, duration: .3 }, t)
        .fromTo(st[i], { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: .35 }, t + .2)
        .to('.story-bg', { opacity: i % 2 ? .55 : 1, duration: .55 }, t);
    }

    // Dynamic motion graphic scroll-reactive tilt & float on headlines
    $$('.lines').forEach(h => {
      const isHero = h.closest('.hero');
      const spans = $$('span', h);
      const items = $$('i', h);
      
      if (!isHero) {
        gsap.fromTo(items, 
          { yPercent: 110, rotateZ: 3, opacity: 0 },
          { yPercent: 0, rotateZ: 0, opacity: 1, duration: 1.15, stagger: 0.1, ease: 'power4.out',
            scrollTrigger: { trigger: h, start: 'top 88%', toggleActions: 'play none none reverse' }
          }
        );
      }
      
      // Continuous scrub parallax on titles as you scroll through them
      gsap.to(h, {
        y: -25,
        ease: 'none',
        scrollTrigger: {
          trigger: h,
          start: 'top bottom',
          end: 'bottom top',
          scrub: 1
        }
      });
    });

    // Lifestyle captions kinetic motion graphic entry & parallax
    $$('.lf').forEach(lf => {
      const title = $('.lf-c h3', lf);
      if (title) {
        gsap.fromTo(title,
          { y: 50, opacity: 0, letterSpacing: '0.04em' },
          { y: 0, opacity: 1, letterSpacing: '0em', duration: 1.2, ease: 'power3.out',
            scrollTrigger: { trigger: lf, start: 'top 75%', toggleActions: 'play none none reverse' }
          }
        );
        gsap.to(title, {
          yPercent: -15,
          ease: 'none',
          scrollTrigger: { trigger: lf, start: 'top bottom', end: 'bottom top', scrub: 1.2 }
        });
      }
    });

    // Anatomy items motion graphics staggered float
    $$('.anat-grid .a').forEach((card, idx) => {
      gsap.fromTo(card,
        { y: 40 + (idx % 3) * 15, opacity: 0 },
        { y: 0, opacity: 1, duration: 1, ease: 'power3.out',
          scrollTrigger: { trigger: card, start: 'top 90%', toggleActions: 'play none none reverse' }
        }
      );
      gsap.to(card, {
        y: -18,
        ease: 'none',
        scrollTrigger: { trigger: card, start: 'top bottom', end: 'bottom top', scrub: 1 }
      });
    });

    // 3 Sizes spec list kinetic stagger
    gsap.fromTo('.sizes li',
      { x: -30, opacity: 0 },
      { x: 0, opacity: 1, duration: 0.9, stagger: 0.14, ease: 'power3.out',
        scrollTrigger: { trigger: '.sizes', start: 'top 85%', toggleActions: 'play none none reverse' }
      }
    );

    // FAQ items motion graphic slide in
    gsap.fromTo('.why-faq details, .faq details',
      { y: 24, opacity: 0 },
      { y: 0, opacity: 1, duration: 0.85, stagger: 0.08, ease: E,
        scrollTrigger: { trigger: '.why-faq, .faq', start: 'top 82%', toggleActions: 'play none none reverse' }
      }
    );

    // Pricing plan cards motion stagger & scrub float
    gsap.fromTo('.plan',
      { y: 45, opacity: 0, scale: 0.97 },
      { y: 0, opacity: 1, scale: 1, duration: 0.9, stagger: 0.12, ease: 'back.out(1.2)',
        scrollTrigger: { trigger: '.plans', start: 'top 85%', toggleActions: 'play none none reverse' }
      }
    );

    // Order checkout container soft floating motion entry
    gsap.fromTo('.order-in',
      { y: 40, opacity: 0 },
      { y: 0, opacity: 1, duration: 1.1, ease: 'power3.out',
        scrollTrigger: { trigger: '.order', start: 'top 80%', toggleActions: 'play none none reverse' }
      }
    );

    // Photography mask reveals + subtle 4K zoom
    $$('.reveal').forEach(el => {
      const img = $('img', el);
      gsap.timeline({ scrollTrigger: { trigger: el, start: 'top 92%', toggleActions: 'play none none reverse' } })
        .fromTo(el, { clipPath: 'inset(0% 0% 100% 0%)' }, { clipPath: 'inset(0% 0% 0% 0%)', duration: 1.1, ease: 'power3.inOut' }, 0)
        .fromTo(img, { scale: 1.08 }, { scale: 1, duration: 1.8, ease: 'power2.out' }, 0);
    });

    // Smooth parallax drift on full-width lifestyle photos
    $$('.lf img').forEach(img => gsap.fromTo(img, { yPercent: -8 }, { yPercent: 8, ease: 'none',
      scrollTrigger: { trigger: img.closest('.lf'), start: 'top bottom', end: 'bottom top', scrub: 1 } }));
      
    // Kinetic floating drift in gallery
    $$('.g figure').forEach((fig, i) => {
      const img = $('img', fig);
      gsap.fromTo(fig, 
        { y: (i % 2 === 0 ? 30 : -20), opacity: 0.8 },
        { y: (i % 2 === 0 ? -30 : 20), opacity: 1, ease: 'none',
          scrollTrigger: { trigger: fig, start: 'top bottom', end: 'bottom top', scrub: 1.2 }
        }
      );
      if (img) {
        gsap.fromTo(img, { scale: 1.08 }, { scale: 1.02, ease: 'none',
          scrollTrigger: { trigger: fig, start: 'top bottom', end: 'bottom top', scrub: 1 }
        });
      }
    });"""

new_js_block = """    // REVERSED scroll scrub directions across the whole website
    gsap.to('.hx-a', { xPercent: 14, ease: 'none', scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: true } });
    gsap.to('.hx-b', { xPercent: -10, ease: 'none', scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: true } });
    $$('.edge span').forEach((e, i) => gsap.fromTo(e, { xPercent: i % 2 ? 18 : 0 }, { xPercent: i % 2 ? 0 : 18, ease: 'none', scrollTrigger: { trigger: e.closest('section'), start: 'top bottom', end: 'bottom top', scrub: true } }));
    gsap.to('.hx-stage', { yPercent: -8, ease: 'none', scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: true } });
    if (reduce) return;

    // line-by-line headline reveals (reverse when scrolled back)
    $$('.lines').forEach(h => { if (h.closest('.hero')) return;
      gsap.from($$('i', h), { yPercent: 105, duration: 1, stagger: .09, ease: 'power4.out',
        scrollTrigger: { trigger: h, start: 'top 88%', toggleActions: 'play none none reverse' } });
    });

    // pinned 5-scene story, fully scrubbed with REVERSED scroll transitions
    const sc = $$('.sc'), st = $$('.st'), n = sc.length;
    const tl = gsap.timeline({ defaults: { ease: 'none' }, scrollTrigger: { trigger: '.story', start: 'top top', end: 'bottom bottom', scrub: .6 } });
    tl.fromTo($('img', sc[0]), { scale: 1.02 }, { scale: 1.15, duration: 1 }, 0)
      .fromTo('.story-media', { xPercent: 0 }, { xPercent: 3, duration: n }, 0);
    for (let i = 1; i < n; i++) {
      const t = i - .45;
      tl.fromTo(sc[i], { clipPath: 'inset(0% 0% 100% 0%)' }, { clipPath: 'inset(0% 0% 0% 0%)', duration: .55, ease: 'power2.inOut' }, t)
        .fromTo($('img', sc[i]), { scale: 1.02, yPercent: -4 }, { scale: 1.15, yPercent: 0, duration: 1.1 }, t)
        .to($('img', sc[i - 1]), { yPercent: 6, duration: .55 }, t)
        .to(st[i - 1], { opacity: 0, y: 40, duration: .3 }, t)
        .fromTo(st[i], { opacity: 0, y: -40 }, { opacity: 1, y: 0, duration: .35 }, t + .2)
        .to('.story-bg', { opacity: i % 2 ? .55 : 1, duration: .55 }, t);
    }

    // Dynamic motion graphic scroll-reactive tilt & float on headlines (REVERSED scrub)
    $$('.lines').forEach(h => {
      const isHero = h.closest('.hero');
      const spans = $$('span', h);
      const items = $$('i', h);
      
      if (!isHero) {
        gsap.fromTo(items, 
          { yPercent: 110, rotateZ: -3, opacity: 0 },
          { yPercent: 0, rotateZ: 0, opacity: 1, duration: 1.15, stagger: 0.1, ease: 'power4.out',
            scrollTrigger: { trigger: h, start: 'top 88%', toggleActions: 'play none none reverse' }
          }
        );
      }
      
      // Continuous scrub parallax on titles (REVERSED: moves downwards smoothly)
      gsap.to(h, {
        y: 25,
        ease: 'none',
        scrollTrigger: {
          trigger: h,
          start: 'top bottom',
          end: 'bottom top',
          scrub: 1
        }
      });
    });

    // Lifestyle captions kinetic motion graphic entry & parallax (REVERSED scrub)
    $$('.lf').forEach(lf => {
      const title = $('.lf-c h3', lf);
      if (title) {
        gsap.fromTo(title,
          { y: 50, opacity: 0, letterSpacing: '0.04em' },
          { y: 0, opacity: 1, letterSpacing: '0em', duration: 1.2, ease: 'power3.out',
            scrollTrigger: { trigger: lf, start: 'top 75%', toggleActions: 'play none none reverse' }
          }
        );
        gsap.to(title, {
          yPercent: 15,
          ease: 'none',
          scrollTrigger: { trigger: lf, start: 'top bottom', end: 'bottom top', scrub: 1.2 }
        });
      }
    });

    // Anatomy items motion graphics staggered float (REVERSED scrub)
    $$('.anat-grid .a').forEach((card, idx) => {
      gsap.fromTo(card,
        { y: 40 + (idx % 3) * 15, opacity: 0 },
        { y: 0, opacity: 1, duration: 1, ease: 'power3.out',
          scrollTrigger: { trigger: card, start: 'top 90%', toggleActions: 'play none none reverse' }
        }
      );
      gsap.to(card, {
        y: 18,
        ease: 'none',
        scrollTrigger: { trigger: card, start: 'top bottom', end: 'bottom top', scrub: 1 }
      });
    });

    // 3 Sizes spec list kinetic stagger (REVERSED entry)
    gsap.fromTo('.sizes li',
      { x: 30, opacity: 0 },
      { x: 0, opacity: 1, duration: 0.9, stagger: 0.14, ease: 'power3.out',
        scrollTrigger: { trigger: '.sizes', start: 'top 85%', toggleActions: 'play none none reverse' }
      }
    );

    // FAQ items motion graphic slide in
    gsap.fromTo('.why-faq details, .faq details',
      { y: 24, opacity: 0 },
      { y: 0, opacity: 1, duration: 0.85, stagger: 0.08, ease: E,
        scrollTrigger: { trigger: '.why-faq, .faq', start: 'top 82%', toggleActions: 'play none none reverse' }
      }
    );

    // Pricing plan cards motion stagger & scrub float
    gsap.fromTo('.plan',
      { y: 45, opacity: 0, scale: 0.97 },
      { y: 0, opacity: 1, scale: 1, duration: 0.9, stagger: 0.12, ease: 'back.out(1.2)',
        scrollTrigger: { trigger: '.plans', start: 'top 85%', toggleActions: 'play none none reverse' }
      }
    );

    // Order checkout container soft floating motion entry
    gsap.fromTo('.order-in',
      { y: 40, opacity: 0 },
      { y: 0, opacity: 1, duration: 1.1, ease: 'power3.out',
        scrollTrigger: { trigger: '.order', start: 'top 80%', toggleActions: 'play none none reverse' }
      }
    );

    // Photography mask reveals + subtle 4K zoom (REVERSED clip reveal from top)
    $$('.reveal').forEach(el => {
      const img = $('img', el);
      gsap.timeline({ scrollTrigger: { trigger: el, start: 'top 92%', toggleActions: 'play none none reverse' } })
        .fromTo(el, { clipPath: 'inset(100% 0% 0% 0%)' }, { clipPath: 'inset(0% 0% 0% 0%)', duration: 1.1, ease: 'power3.inOut' }, 0)
        .fromTo(img, { scale: 1.08 }, { scale: 1, duration: 1.8, ease: 'power2.out' }, 0);
    });

    // Smooth parallax drift on full-width lifestyle photos (REVERSED direction)
    $$('.lf img').forEach(img => gsap.fromTo(img, { yPercent: 8 }, { yPercent: -8, ease: 'none',
      scrollTrigger: { trigger: img.closest('.lf'), start: 'top bottom', end: 'bottom top', scrub: 1 } }));
      
    // Kinetic floating drift in gallery (REVERSED float & zoom scrub)
    $$('.g figure').forEach((fig, i) => {
      const img = $('img', fig);
      gsap.fromTo(fig, 
        { y: (i % 2 === 0 ? -30 : 20), opacity: 0.8 },
        { y: (i % 2 === 0 ? 30 : -20), opacity: 1, ease: 'none',
          scrollTrigger: { trigger: fig, start: 'top bottom', end: 'bottom top', scrub: 1.2 }
        }
      );
      if (img) {
        gsap.fromTo(img, { scale: 1.02 }, { scale: 1.08, ease: 'none',
          scrollTrigger: { trigger: fig, start: 'top bottom', end: 'bottom top', scrub: 1 }
        });
      }
    });"""

assert old_js_block in html, "Could not find old_js_block"
html = html.replace(old_js_block, new_js_block)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("nova-mart-aone.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Both index.html and nova-mart-aone.html updated successfully!")
