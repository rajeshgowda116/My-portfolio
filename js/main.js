/* ==========================================================================
   RAJESH NAGAPPA GOUDA — PORTFOLIO INTERACTIVE JAVASCRIPT
   Features: Continuous Scroll Observer (re-triggers on scroll up & down), 
   Animated Counters, Sticky Navbar, Mobile Navigation Drawer, Form Handler.
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {

  // --- 1. SMOOTH ANCHOR LINK SCROLLING ---
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        e.preventDefault();
        const headerOffset = 90;
        const elementPosition = targetElement.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

        window.scrollTo({
          top: offsetPosition,
          behavior: 'smooth'
        });
      }
    });
  });

  // --- 2. STICKY NAVBAR SCROLL OBSERVER ---
  const header = document.querySelector('.header');
  const navLinks = document.querySelectorAll('.nav-link');
  const sections = document.querySelectorAll('section[id]');

  window.addEventListener('scroll', () => {
    if (window.scrollY > 30) {
      header.classList.add('nav-scrolled');
    } else {
      header.classList.remove('nav-scrolled');
    }

    // Active Section Link Observer
    let current = '';
    sections.forEach(section => {
      const sectionTop = section.offsetTop - 120;
      const sectionHeight = section.offsetHeight;
      if (window.scrollY >= sectionTop && window.scrollY < sectionTop + sectionHeight) {
        current = section.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === `#${current}`) {
        link.classList.add('active');
      }
    });
  }, { passive: true });

  // --- 3. MOBILE HAMBURGER MENU TOGGLE ---
  const hamburger = document.querySelector('.hamburger');
  const mobileNav = document.querySelector('.mobile-nav-overlay');
  const mobileLinks = document.querySelectorAll('.mobile-nav-overlay .nav-link');

  if (hamburger && mobileNav) {
    hamburger.addEventListener('click', () => {
      hamburger.classList.toggle('is-active');
      mobileNav.classList.toggle('is-active');
      document.body.style.overflow = mobileNav.classList.contains('is-active') ? 'hidden' : '';
    });

    mobileLinks.forEach(link => {
      link.addEventListener('click', () => {
        hamburger.classList.remove('is-active');
        mobileNav.classList.remove('is-active');
        document.body.style.overflow = '';
      });
    });
  }

  // --- 4. RE-TRIGGERING SCROLL REVEAL OBSERVER (ANIMATES EVERY TIME YOU SCROLL) ---
  const revealElements = document.querySelectorAll('.reveal-up, .reveal-fade');

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
      } else {
        // Re-trigger animation every time user scrolls away and back
        entry.target.classList.remove('active');
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -40px 0px'
  });

  revealElements.forEach(el => revealObserver.observe(el));

  // --- 5. ANIMATED STAT COUNTERS ---
  const statNumbers = document.querySelectorAll('.stat-num');

  const countObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        statNumbers.forEach(stat => {
          const target = parseInt(stat.getAttribute('data-target') || '0', 10);
          const suffix = stat.getAttribute('data-suffix') || '';
          let count = 0;
          const duration = 1800;
          const step = Math.max(1, Math.floor(target / (duration / 30)));

          const timer = setInterval(() => {
            count += step;
            if (count >= target) {
              count = target;
              clearInterval(timer);
            }
            stat.textContent = count + suffix;
          }, 30);
        });
      }
    });
  }, { threshold: 0.4 });

  const statsContainer = document.querySelector('.hero-stats');
  if (statsContainer) {
    countObserver.observe(statsContainer);
  }

  // --- 6. CONTACT FORM SUBMISSION HANDLER ---
  const contactForm = document.getElementById('contactForm');
  const toast = document.getElementById('toast');

  if (contactForm && toast) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const btn = contactForm.querySelector('button[type="submit"]');
      const originalText = btn.innerHTML;

      btn.innerHTML = `Sending...`;
      btn.disabled = true;

      setTimeout(() => {
        contactForm.reset();
        btn.innerHTML = originalText;
        btn.disabled = false;

        // Show toast
        toast.classList.add('show');
        setTimeout(() => {
          toast.classList.remove('show');
        }, 4000);
      }, 1000);
    });
  }

});
