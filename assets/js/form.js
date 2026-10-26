/**
 * Sugam Home Care Services - Lead Form Handler
 * Captures enquiries, validates inputs, records Google Ads UTM parameters & gclid,
 * saves to localStorage fallback, and redirects seamlessly to the Thank You page.
 */

document.addEventListener('DOMContentLoaded', () => {
  initLeadForms();
});

function initLeadForms() {
  const forms = document.querySelectorAll('.lead-form');

  forms.forEach(form => {
    form.addEventListener('submit', handleFormSubmit);
  });
}

function handleFormSubmit(e) {
  e.preventDefault();
  const form = e.target;
  const submitBtn = form.querySelector('.btn-submit-lead');
  const originalBtnText = submitBtn ? submitBtn.innerHTML : 'Request a Call Back';

  // Extract Form Data
  const nameInput = form.querySelector('input[name="fullName"]');
  const phoneInput = form.querySelector('input[name="phone"]');
  const serviceSelect = form.querySelector('select[name="service"]');
  const consentCheckbox = form.querySelector('input[name="consent"]');

  // Basic Validation
  if (!nameInput || !nameInput.value.trim()) {
    showFormError(nameInput, "Please enter your full name");
    return;
  }

  const phoneValue = phoneInput ? phoneInput.value.trim().replace(/[\s-]/g, '') : '';
  const phoneRegex = /^(\+91|91|0)?[6-9]\d{9}$/; // Standard Indian mobile phone validation
  if (!phoneValue || !phoneRegex.test(phoneValue)) {
    showFormError(phoneInput, "Please enter a valid 10-digit mobile number");
    return;
  }

  if (!serviceSelect || !serviceSelect.value) {
    showFormError(serviceSelect, "Please select the service you require");
    return;
  }

  if (consentCheckbox && !consentCheckbox.checked) {
    alert("Please check the consent box so our care coordinator can call you back.");
    consentCheckbox.focus();
    return;
  }

  // Extract UTM Parameters & GCLID from URL
  const urlParams = new URLSearchParams(window.location.search);
  const utmData = {
    utm_source: urlParams.get('utm_source') || 'direct',
    utm_medium: urlParams.get('utm_medium') || '',
    utm_campaign: urlParams.get('utm_campaign') || '',
    utm_term: urlParams.get('utm_term') || '',
    utm_content: urlParams.get('utm_content') || '',
    gclid: urlParams.get('gclid') || ''
  };

  const leadData = {
    id: 'LEAD-' + Date.now(),
    fullName: nameInput.value.trim(),
    phone: phoneValue,
    service: serviceSelect.value,
    submittedAt: new Date().toISOString(),
    pageUrl: window.location.pathname,
    pageTitle: document.title,
    utm: utmData
  };

  // UI state: submitting
  if (submitBtn) {
    submitBtn.disabled = true;
    submitBtn.innerHTML = `
      <svg class="icon animate-spin" viewBox="0 0 24 24" fill="none" stroke="currentColor">
        <circle cx="12" cy="12" r="10" stroke-width="4" stroke-opacity="0.25"></circle>
        <path d="M4 12a8 8 0 018-8" stroke-width="4"></path>
      </svg>
      Submitting Enquiry...
    `;
  }

  // Persist lead locally so no lead is ever lost
  try {
    const existingLeads = JSON.parse(localStorage.getItem('sugam_enquiries') || '[]');
    existingLeads.unshift(leadData);
    localStorage.setItem('sugam_enquiries', JSON.stringify(existingLeads));
    
    // Store latest lead in sessionStorage for Thank You page personalization
    sessionStorage.setItem('sugam_latest_lead', JSON.stringify(leadData));
  } catch (err) {
    console.warn("Could not save to localStorage", err);
  }

  // Trigger Google Ads conversion event if configured
  if (typeof gtag === 'function' && typeof SITE_CONFIG !== 'undefined' && SITE_CONFIG.googleAds && SITE_CONFIG.googleAds.enabled) {
    gtag('event', 'conversion', {
      'send_to': `${SITE_CONFIG.googleAds.conversionId}/${SITE_CONFIG.googleAds.conversionLabel}`,
      'value': 1.0,
      'currency': 'INR'
    });
  }

  // Dispatch email notification via backend endpoint
  const endpoint = window.location.protocol === 'file:' 
    ? 'https://sugamhomecareservices.in/send_enquiry.php' 
    : '/send_enquiry.php';

  let hasNavigated = false;
  const navigateToThankYou = () => {
    if (hasNavigated) return;
    hasNavigated = true;
    if (window.location.protocol === 'file:') {
      const isSubDir = window.location.pathname.split('/').filter(Boolean).length > 6;
      window.location.href = isSubDir ? '../thank-you/index.html' : 'thank-you/index.html';
    } else {
      window.location.href = '/thank-you/';
    }
  };

  // Safe timeout: never leave visitor hanging if network is slow
  const fallbackTimer = setTimeout(navigateToThankYou, 2500);

  fetch(endpoint, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    },
    body: JSON.stringify(leadData)
  })
    .then(res => res.json())
    .catch(err => {
      console.warn("Server email dispatch notice:", err);
    })
    .finally(() => {
      clearTimeout(fallbackTimer);
      navigateToThankYou();
    });
}

function showFormError(inputEl, message) {
  inputEl.classList.add('error');
  inputEl.focus();
  
  // Show error tooltip or shake
  let errorEl = inputEl.parentNode.querySelector('.form-error-msg');
  if (!errorEl) {
    errorEl = document.createElement('span');
    errorEl.className = 'form-error-msg';
    errorEl.style.color = '#DC2626';
    errorEl.style.fontSize = '0.75rem';
    errorEl.style.marginTop = '0.2rem';
    errorEl.style.display = 'block';
    inputEl.parentNode.appendChild(errorEl);
  }
  errorEl.textContent = message;

  inputEl.addEventListener('input', () => {
    inputEl.classList.remove('error');
    if (errorEl) errorEl.remove();
  }, { once: true });
}
