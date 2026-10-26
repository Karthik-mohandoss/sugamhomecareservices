/**
 * Sugam Home Care Services - Main JavaScript
 * Handles navigation, mobile menu, accordions, modals, dynamic config binding,
 * and automatic cache-bust validation for CDN edge updates.
 */

// Auto Cache-Buster & DOM Cleaner
function cleanLegacyElements() {
  try {
    // 1. Remove Preferred Contact Time from all forms immediately
    document.querySelectorAll('[name="preferredTime"]').forEach(el => {
      const group = el.closest('.form-group');
      if (group) group.remove();
      else el.remove();
    });

    document.querySelectorAll('label').forEach(label => {
      if (label.textContent && label.textContent.toLowerCase().includes('preferred contact time')) {
        const group = label.closest('.form-group');
        if (group) group.remove();
        else label.remove();
      }
    });

    // 2. Check for stale HTML version requiring refresh
    const hasOldMaidService = document.querySelector('a[href*="maid-services"]');
    const missingSeniorCare = !document.querySelector('a[href*="senior-citizen-care-services"]');
    const isHomePage = window.location.pathname === '/' || window.location.pathname === '/index.html' || window.location.pathname === '';
    
    if (isHomePage && (hasOldMaidService || missingSeniorCare)) {
      if (!window.location.search.includes('v=3')) {
        const targetUrl = new URL(window.location.href);
        targetUrl.searchParams.set('v', '3');
        window.location.replace(targetUrl.toString());
        return;
      }
    }
    
    // Clean up query param from address bar once fresh version is loaded
    if (window.location.search.includes('v=') && !hasOldMaidService && !missingSeniorCare) {
      if (window.history && window.history.replaceState) {
        window.history.replaceState(null, '', window.location.pathname);
      }
    }
  } catch (e) {
    // Graceful fallback
  }
}

// Run immediately upon script parsing
cleanLegacyElements();

document.addEventListener('DOMContentLoaded', () => {
  cleanLegacyElements();
  initDynamicConfig();
  initMobileNav();
  initFaqAccordion();
  initModal();
  initHeaderScroll();
});

/**
 * Injects values from SITE_CONFIG into elements with data-config attributes.
 */
function initDynamicConfig() {
  if (typeof SITE_CONFIG === 'undefined') return;

  // Bind phone numbers
  document.querySelectorAll('[data-config="phoneDisplay"]').forEach(el => {
    el.textContent = SITE_CONFIG.phoneDisplay;
  });
  document.querySelectorAll('[data-config="phoneTel"]').forEach(el => {
    el.setAttribute('href', SITE_CONFIG.phoneTel);
  });

  // Bind WhatsApp links & displays
  document.querySelectorAll('[data-config="whatsappDisplay"]').forEach(el => {
    el.textContent = SITE_CONFIG.whatsappDisplay;
  });
  document.querySelectorAll('[data-config="whatsappLink"]').forEach(el => {
    // If the element has a custom data-service message, customize the wa.me url
    const serviceName = el.getAttribute('data-service');
    if (serviceName) {
      const customMsg = `Hello Sugam Home Care Services, I would like to enquire about ${serviceName}.`;
      el.setAttribute('href', `https://wa.me/${SITE_CONFIG.whatsappRaw}?text=${encodeURIComponent(customMsg)}`);
    } else {
      el.setAttribute('href', SITE_CONFIG.whatsappLink);
    }
  });

  // Bind email & address
  document.querySelectorAll('[data-config="email"]').forEach(el => {
    el.textContent = SITE_CONFIG.email;
    if (el.tagName === 'A') {
      el.setAttribute('href', `mailto:${SITE_CONFIG.email}`);
    }
  });
  document.querySelectorAll('[data-config="addressFull"]').forEach(el => {
    el.textContent = SITE_CONFIG.address.full;
  });
}

/**
 * Mobile Drawer Menu Toggle
 */
function initMobileNav() {
  const hamburgerBtn = document.querySelector('.hamburger-btn');
  const navDrawer = document.querySelector('.mobile-nav-drawer');

  if (!hamburgerBtn || !navDrawer) return;

  hamburgerBtn.addEventListener('click', () => {
    const isOpen = hamburgerBtn.classList.toggle('is-active');
    navDrawer.classList.toggle('is-open', isOpen);
    document.body.style.overflow = isOpen ? 'hidden' : '';
    hamburgerBtn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
  });

  // Close menu when clicking on a link
  navDrawer.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      hamburgerBtn.classList.remove('is-active');
      navDrawer.classList.remove('is-open');
      document.body.style.overflow = '';
      hamburgerBtn.setAttribute('aria-expanded', 'false');
    });
  });

  // Close menu on ESC key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && navDrawer.classList.contains('is-open')) {
      hamburgerBtn.classList.remove('is-active');
      navDrawer.classList.remove('is-open');
      document.body.style.overflow = '';
      hamburgerBtn.setAttribute('aria-expanded', 'false');
    }
  });
}

/**
 * Accessible FAQ Accordion
 */
function initFaqAccordion() {
  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach((item, index) => {
    const questionBtn = item.querySelector('.faq-question');
    const answer = item.querySelector('.faq-answer');

    if (!questionBtn || !answer) return;

    // Set accessibility attributes
    const answerId = `faq-answer-${index}`;
    answer.setAttribute('id', answerId);
    questionBtn.setAttribute('aria-controls', answerId);
    questionBtn.setAttribute('aria-expanded', 'false');

    questionBtn.addEventListener('click', () => {
      const isOpen = item.classList.contains('is-open');

      // Close all other FAQs in the same group
      faqItems.forEach(otherItem => {
        if (otherItem !== item && otherItem.classList.contains('is-open')) {
          otherItem.classList.remove('is-open');
          const otherBtn = otherItem.querySelector('.faq-question');
          const otherAns = otherItem.querySelector('.faq-answer');
          if (otherBtn) otherBtn.setAttribute('aria-expanded', 'false');
          if (otherAns) otherAns.style.maxHeight = null;
        }
      });

      // Toggle current item
      if (isOpen) {
        item.classList.remove('is-open');
        questionBtn.setAttribute('aria-expanded', 'false');
        answer.style.maxHeight = null;
      } else {
        item.classList.add('is-open');
        questionBtn.setAttribute('aria-expanded', 'true');
        answer.style.maxHeight = answer.scrollHeight + 'px';
      }
    });
  });
}

/**
 * Modal Dialog (Callback Request)
 */
function initModal() {
  const modalOverlay = document.querySelector('.modal-overlay');
  const closeBtn = document.querySelector('.modal-close-btn');
  const openButtons = document.querySelectorAll('.btn-open-modal');
  const modalServiceSelect = document.querySelector('#modal-service-select');

  if (!modalOverlay) return;

  openButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const serviceToSelect = btn.getAttribute('data-service');
      if (modalServiceSelect && serviceToSelect) {
        modalServiceSelect.value = serviceToSelect;
      }
      openModal();
    });
  });

  function openModal() {
    modalOverlay.classList.add('is-open');
    document.body.style.overflow = 'hidden';
    const firstInput = modalOverlay.querySelector('input');
    if (firstInput) setTimeout(() => firstInput.focus(), 100);
  }

  function closeModal() {
    modalOverlay.classList.remove('is-open');
    document.body.style.overflow = '';
  }

  if (closeBtn) {
    closeBtn.addEventListener('click', closeModal);
  }

  modalOverlay.addEventListener('click', (e) => {
    if (e.target === modalOverlay) {
      closeModal();
    }
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modalOverlay.classList.contains('is-open')) {
      closeModal();
    }
  });
}

/**
 * Sticky Header Scroll State
 */
function initHeaderScroll() {
  const header = document.querySelector('.site-header');
  if (!header) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 30) {
      header.classList.add('is-scrolled');
    } else {
      header.classList.remove('is-scrolled');
    }
  }, { passive: true });
}
