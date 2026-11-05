(() => {
  const root = document.documentElement;
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const hasGsap = window.gsap && window.ScrollTrigger;
  if (reduced || !hasGsap) root.classList.add('reduced');
  root.classList.add('js');

  /* header: shadow when scrolled, hide on scroll down */
  const hdr = document.querySelector('.hdr');
  let lastY = 0;
  const onScroll = (y) => {
    hdr.classList.toggle('is-scrolled', y > 8);
    const megaOpen = document.body.classList.contains('mega-open') || document.body.classList.contains('menu-open');
    hdr.classList.toggle('is-hidden', !megaOpen && y > 400 && y > lastY);
    lastY = y;
  };

  /* mega menu */
  const megaBtn = document.querySelector('[data-mega]');
  const mega = document.querySelector('.mega');
  const setMega = (on) => {
    document.body.classList.toggle('mega-open', on);
    hdr.classList.toggle('mega-open', on);
    megaBtn && megaBtn.setAttribute('aria-expanded', on);
  };
  if (megaBtn && mega) {
    let t;
    const open = () => { clearTimeout(t); setMega(true); };
    const close = () => { t = setTimeout(() => setMega(false), 160); };
    megaBtn.addEventListener('mouseenter', open);
    megaBtn.addEventListener('mouseleave', close);
    mega.addEventListener('mouseenter', open);
    mega.addEventListener('mouseleave', close);
    megaBtn.addEventListener('click', () => setMega(!document.body.classList.contains('mega-open')));
    document.querySelector('.mega-scrim')?.addEventListener('click', () => setMega(false));
    addEventListener('keydown', (e) => e.key === 'Escape' && setMega(false));
  }

  /* mobile menu */
  document.querySelector('.hdr__burger')?.addEventListener('click', () => {
    const on = !document.body.classList.contains('menu-open');
    document.body.classList.toggle('menu-open', on);
    document.querySelector('.hdr__burger').setAttribute('aria-expanded', on);
  });

  /* contact form: demo submission for the pitch */
  document.querySelectorAll('.form').forEach((f) => f.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!f.reportValidity()) return;
    f.classList.add('sent');
    if (window.ScrollTrigger) ScrollTrigger.refresh();
  }));

  /* references photo rotation */
  document.querySelectorAll('.refs__photos').forEach((box) => {
    const imgs = [...box.querySelectorAll('img')];
    if (imgs.length < 2) return;
    let i = 0;
    setInterval(() => {
      imgs[i].classList.remove('on');
      i = (i + 1) % imgs.length;
      imgs[i].classList.add('on');
    }, 2600);
  });

  /* split text into word spans for scroll fill */
  document.querySelectorAll('[data-fill]').forEach((el) => {
    el.innerHTML = el.textContent.trim().split(/\s+/).map((w) => `<span class="w">${w}</span>`).join(' ');
  });

  const done = () => document.querySelectorAll('[data-fill] .w').forEach((w) => { w.style.color = ''; w.style.opacity = 1; });

  if (reduced || !hasGsap) {
    document.querySelector('.loader')?.remove();
    addEventListener('scroll', () => onScroll(scrollY), { passive: true });
    document.querySelectorAll('[data-fill] .w').forEach((w) => w.removeAttribute('class'));
    document.querySelectorAll('[data-count]').forEach((n) => (n.textContent = n.dataset.count));
    return;
  }

  gsap.registerPlugin(ScrollTrigger);

  /* smooth scroll */
  let lenis;
  if (window.Lenis) {
    lenis = new Lenis({ lerp: 0.1 });
    lenis.on('scroll', (e) => { ScrollTrigger.update(); onScroll(e.scroll); });
    gsap.ticker.add((t) => lenis.raf(t * 1000));
    gsap.ticker.lagSmoothing(0);
    document.querySelectorAll('a[href^="#"]').forEach((a) => a.addEventListener('click', (e) => {
      const target = document.querySelector(a.getAttribute('href'));
      if (target) { e.preventDefault(); lenis.scrollTo(target, { offset: -90 }); }
    }));
  } else {
    addEventListener('scroll', () => onScroll(scrollY), { passive: true });
  }

  /* intro: loader once per session, then hero lines */
  const heroLines = gsap.utils.toArray('.hero__title .ln > span, .phero__title .ln > span');
  gsap.set(heroLines, { yPercent: 105 });
  const intro = () => {
    gsap.to(heroLines, { yPercent: 0, duration: 1.2, ease: 'expo.out', stagger: 0.09 });
    gsap.from('.hero__aside > *, .phero__intro > *, .phero__crumb', { opacity: 0, y: 24, duration: 1, ease: 'expo.out', stagger: 0.08, delay: 0.35 });
  };
  const loader = document.querySelector('.loader');
  let seen = false;
  try { seen = sessionStorage.getItem('mizar-intro') === '1'; sessionStorage.setItem('mizar-intro', '1'); } catch (e) {}
  if (loader && !seen) {
    const num = loader.querySelector('.loader__num');
    const c = { v: 0 };
    gsap.timeline()
      .to(c, { v: 100, duration: 1.1, ease: 'power2.inOut', onUpdate: () => (num.textContent = Math.round(c.v)) })
      .to(loader.querySelector('.loader__in'), { opacity: 0, y: -16, duration: 0.45, ease: 'power2.in' })
      .to(loader, { opacity: 0, duration: 0.5, ease: 'power2.out', onComplete: () => loader.remove() })
      .add(intro, '-=0.35');
  } else {
    loader?.remove();
    intro();
  }

  /* reveals */
  gsap.utils.toArray('[data-reveal]').forEach((el) => {
    gsap.to(el, {
      opacity: 1, y: 0, duration: 1.1, ease: 'expo.out',
      delay: (+el.dataset.reveal || 0) * 0.1,
      scrollTrigger: { trigger: el, start: 'top 88%', once: true },
    });
  });

  /* image parallax inside fixed frames */
  gsap.utils.toArray('[data-parallax]').forEach((img) => {
    gsap.fromTo(img, { yPercent: -6 }, {
      yPercent: 6, ease: 'none',
      scrollTrigger: { trigger: img.parentElement, start: 'top bottom', end: 'bottom top', scrub: true },
    });
  });

  /* hero frame opens to full width */
  gsap.utils.toArray('[data-expand]').forEach((f) => {
    const gut = getComputedStyle(root).getPropertyValue('--gut').trim();
    gsap.fromTo(f, { clipPath: `inset(0px ${gut} 0px ${gut})` }, {
      clipPath: 'inset(0px 0px 0px 0px)', ease: 'none',
      scrollTrigger: { trigger: f, start: 'top 85%', end: 'top 10%', scrub: true },
    });
  });

  /* words fill from gray to ink */
  gsap.utils.toArray('[data-fill]').forEach((el) => {
    const words = el.querySelectorAll('.w');
    const to = el.closest('.state') ? { opacity: 1 } : { color: '#171411' };
    gsap.to(words, { ...to, stagger: 0.05, ease: 'none',
      scrollTrigger: { trigger: el, start: 'top 80%', end: 'bottom 50%', scrub: true } });
  });

  /* counters finish exactly on their value */
  gsap.utils.toArray('[data-count]').forEach((n) => {
    const end = +n.dataset.count;
    const o = { v: Math.max(0, end - (end > 1000 ? 60 : end)) };
    n.textContent = Math.round(o.v);
    gsap.to(o, {
      v: end, duration: 1.8, ease: 'power3.out',
      onUpdate: () => (n.textContent = Math.round(o.v)),
      onComplete: () => (n.textContent = end),
      scrollTrigger: { trigger: n, start: 'top 90%', once: true },
    });
  });

  /* footer wordmark rises */
  const word = document.querySelector('.ftr__word span');
  if (word) gsap.fromTo(word, { yPercent: 60 }, { yPercent: 0, ease: 'none', scrollTrigger: { trigger: '.ftr__word', start: 'top bottom', end: 'bottom bottom', scrub: true } });

  addEventListener('load', () => ScrollTrigger.refresh());
  window.__done = done;
})();
