import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Let's inspect CSS to add the breathable keyframes and smooth motion styling
breathing_css = """
/* Motion graphics & Breathable idle animation */
@keyframes breatheSlow {
  0%, 100% { transform: translateY(0px) scale(1); }
  50% { transform: translateY(-7px) scale(1.008); }
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
.hx-stage {
  animation: breatheSlow 6s ease-in-out infinite alternate, glowPulse 8s ease-in-out infinite alternate;
}
.order-img, .fits-img {
  animation: breatheGentle 7s ease-in-out infinite alternate;
}
.plan.on {
  animation: floatSubtle 5s ease-in-out infinite alternate;
}
.wa-float:not(:hover) {
  animation: breatheGentle 4s ease-in-out infinite alternate;
}

/* Kinetic motion graphics on titles while scrolling */
.lines > span {
  display: block;
  overflow: hidden;
  padding-bottom: .08em;
}
.lines > span > i {
  display: inline-block;
  will-change: transform, opacity;
  transform-origin: left center;
}
.lf-c h3 {
  will-change: transform, opacity;
}
"""

# Insert breathing CSS before </style>
html = html.replace("</style></head>", breathing_css + "\n</style></head>")

# Now let's enhance the GSAP animation script
old_script = """    // mask reveals + scale 1.04 -> 1 for photography
    $$('.reveal').forEach(el => {
      const img = $('img', el);
      gsap.timeline({ scrollTrigger: { trigger: el, start: 'top 90%', toggleActions: 'play none none reverse' } })
        .fromTo(el, { clipPath: 'inset(0% 0% 100% 0%)' }, { clipPath: 'inset(0% 0% 0% 0%)', duration: 1.1, ease: 'power3.inOut' }, 0)
        .fromTo(img, { scale: 1.04 }, { scale: 1, duration: 1.6, ease: 'power2.out' }, 0);
    });

    // controlled parallax on full-width lifestyle photos
    $$('.lf img').forEach(img => gsap.fromTo(img, { yPercent: -6 }, { yPercent: 6, ease: 'none',
      scrollTrigger: { trigger: img.closest('.lf'), start: 'top bottom', end: 'bottom top', scrub: true } }));
    // subtle horizontal drift in gallery
    $$('.g img').forEach((img, i) => gsap.fromTo(img, { xPercent: i % 2 ? -2 : 2, scale: 1.06 }, { xPercent: i % 2 ? 2 : -2, scale: 1.06, ease: 'none',
      scrollTrigger: { trigger: img, start: 'top bottom', end: 'bottom top', scrub: true } }));

    // pricing reveal
    gsap.from('.plan', { y: 30, opacity: 0, duration: .9, stagger: .1, ease: E,
      scrollTrigger: { trigger: '.plans', start: 'top 85%', toggleActions: 'play none none reverse' } });
    gsap.from('.why-faq details', { y: 20, opacity: 0, duration: .8, stagger: .08, ease: E,
      scrollTrigger: { trigger: '.why-faq', start: 'top 80%', toggleActions: 'play none none reverse' } });
  };"""

new_script = """    // Dynamic motion graphic scroll-reactive tilt & float on headlines
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
    });
  };"""

if old_script in html:
    html = html.replace(old_script, new_script)
    print("Script successfully replaced")
else:
    print("Old script pattern not matched directly, checking differences")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("nova-mart-aone.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Files saved successfully!")
