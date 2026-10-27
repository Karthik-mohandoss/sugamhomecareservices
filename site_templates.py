#!/usr/bin/env python3
"""
Sugam Home Care Services - Site Generator Templates
Provides consistent Header, Navigation, Footer, Mobile Bar, and Callback Modal.
"""

import os

ROOT_DIR = "/Users/karthik/.gemini/antigravity/scratch/sugam-home-care"

# 11 Approved Services
SERVICES_NAV = [
    {"name": "Baby care services", "slug": "baby-care-services", "icon": "👶"},
    {"name": "Elderly care services", "slug": "elderly-care-services", "icon": "🧓"},
    {"name": "Patient care services", "slug": "patient-care-services", "icon": "🛏️"},
    {"name": "Senior citizen care services", "slug": "senior-citizen-care-services", "icon": "👴"},
    {"name": "Bedridden patient care services", "slug": "bedridden-patient-care-services", "icon": "🛌"},
    {"name": "Home health care for seniors", "slug": "home-health-care-for-seniors", "icon": "🩺"},
    {"name": "Dementia care for the elderly", "slug": "dementia-care-for-the-elderly", "icon": "🧠"},
    {"name": "Home care for cancer patients", "slug": "home-care-for-cancer-patients", "icon": "🎗️"},
    {"name": "Caretaker services at home", "slug": "caretaker-services-at-home", "icon": "🤝"},
    {"name": "Home nurse services", "slug": "home-nurse-services", "icon": "👩‍⚕️"},
    {"name": "Nursing Services", "slug": "nursing-services", "icon": "💉"}
]

# Official Google Ads (gtag.js) tracking scripts
GOOGLE_ADS_HEAD = '''  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=AW-18536226621"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'AW-18536226621');
    gtag('config', 'AW-18536226621/p8H3CJXguKodEL2-4YZF', {
      'phone_conversion_number': '84388 61636'
    });
  </script>

  <!-- Event snippet for Click to call (1) conversion page -->
  <script>
  function gtag_report_conversion(url) {
    var callback = function () {
      if (typeof(url) != 'undefined') {
        window.location = url;
      }
    };
    gtag('event', 'conversion', {
        'send_to': 'AW-18536226621/OU2_CJjguKodEL2-4YZF',
        'value': 1.0,
        'currency': 'INR',
        'event_callback': callback
    });
    return false;
  }
  </script>'''

def get_header(current_path, depth=0):
    rel = "./" if depth == 0 else "../"
    
    is_home = (current_path == "/")
    is_about = (current_path == "/about-us/")
    is_services = ("/services" in current_path or current_path.endswith("-services/") or "care" in current_path or "nurse" in current_path)
    is_contact = (current_path == "/contact-us/")

    # Build dropdown items
    desktop_dropdown = ""
    mobile_submenu = ""
    for s in SERVICES_NAV:
        desktop_dropdown += f'''
          <a href="{rel}{s["slug"]}/" class="dropdown-item" role="menuitem">
            <span class="dropdown-item-icon">{s["icon"]}</span> {s["name"]}
          </a>'''
        mobile_submenu += f'''
          <a href="{rel}{s["slug"]}/" class="mobile-sub-link">{s["icon"]} {s["name"]}</a>'''
    
    return f'''<!-- Topbar for Quick Contact & Reassurance -->
<div class="header-topbar">
  <div class="container topbar-content">
    <div class="topbar-left">
      <span class="topbar-item">
        <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
        Chennai &amp; All Over Tamil Nadu
      </span>
      <span class="topbar-badge">Trusted Home Care in Chennai • 24-Hr Service Across Tamil Nadu</span>
    </div>
    <div class="topbar-right">
      <a href="tel:+918438861636" data-config="phoneTel" class="topbar-item">
        <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"></path></svg>
        Call: <strong data-config="phoneDisplay">+91 84388 61636</strong>
      </a>
      <a href="https://wa.me/918438861636" data-config="whatsappLink" target="_blank" rel="noopener noreferrer" class="topbar-item">
        <svg class="icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0012.04 2zm5.79 14.07c-.24.67-1.39 1.29-1.93 1.37-.5.08-1.12.11-3.56-.88-3.09-1.28-5.06-4.42-5.21-4.63-.16-.2-1.24-1.66-1.24-3.16 0-1.51.78-2.25 1.06-2.55.28-.3.61-.38.81-.38.2 0 .41 0 .59.01.19.01.44-.07.69.52.25.6.86 2.1.94 2.25.08.16.14.34.03.55-.11.21-.16.34-.32.53-.16.19-.34.42-.48.56-.16.16-.33.33-.14.65.19.32.84 1.38 1.8 2.24 1.24 1.11 2.28 1.45 2.61 1.61.32.16.51.14.7-.08.19-.22.82-.95 1.04-1.28.22-.32.44-.27.75-.16.3.11 1.93.91 2.26 1.08.33.16.55.25.63.39.08.13.08.77-.16 1.44z"></path></svg>
        WhatsApp Us
      </a>
    </div>
  </div>
</div>

<!-- Main Sticky Header -->
<header class="site-header" id="site-header">
  <div class="container navbar">
    <!-- Brand Logo -->
    <a href="{rel}" class="navbar-brand" aria-label="Sugam Home Care Services Home">
      <img src="{rel}assets/images/logo.svg" alt="Sugam Home Care Services Logo" class="brand-logo-img" width="240" height="52">
    </a>

    <!-- Desktop Navigation -->
    <nav class="nav-menu" aria-label="Main Navigation">
      <a href="{rel}" class="nav-link {'active' if is_home else ''}">Home</a>
      <a href="{rel}about-us/" class="nav-link {'active' if is_about else ''}">About Us</a>
      
      <!-- Services Dropdown (11 Services) -->
      <div class="nav-dropdown">
        <a href="{rel}services/" class="nav-link nav-dropdown-toggle {'active' if is_services else ''}" aria-haspopup="true" aria-expanded="false">
          Services
          <svg class="dropdown-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"></path></svg>
        </a>
        <div class="nav-dropdown-menu" role="menu" style="min-width: 320px; max-height: 480px; overflow-y: auto;">
          {desktop_dropdown}
        </div>
      </div>

      <a href="{rel}contact-us/" class="nav-link {'active' if is_contact else ''}">Contact Us</a>
    </nav>

    <!-- Header Actions (Calls & WhatsApp) -->
    <div class="header-actions">
      <a href="https://wa.me/918438861636" data-config="whatsappLink" target="_blank" rel="noopener noreferrer" class="btn-header-whatsapp" aria-label="Chat on WhatsApp">
        <svg class="icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0012.04 2zm5.79 14.07c-.24.67-1.39 1.29-1.93 1.37-.5.08-1.12.11-3.56-.88-3.09-1.28-5.06-4.42-5.21-4.63-.16-.2-1.24-1.66-1.24-3.16 0-1.51.78-2.25 1.06-2.55.28-.3.61-.38.81-.38.2 0 .41 0 .59.01.19.01.44-.07.69.52.25.6.86 2.1.94 2.25.08.16.14.34.03.55-.11.21-.16.34-.32.53-.16.19-.34.42-.48.56-.16.16-.33.33-.14.65.19.32.84 1.38 1.8 2.24 1.24 1.11 2.28 1.45 2.61 1.61.32.16.51.14.7-.08.19-.22.82-.95 1.04-1.28.22-.32.44-.27.75-.16.3.11 1.93.91 2.26 1.08.33.16.55.25.63.39.08.13.08.77-.16 1.44z"></path></svg>
        WhatsApp
      </a>
      <a href="tel:+918438861636" data-config="phoneTel" class="btn-header-call" aria-label="Call Sugam Home Care Services">
        <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"></path></svg>
        <span class="btn-call-text">Call Now</span>
      </a>

      <!-- Hamburger Menu for Mobile -->
      <button type="button" class="hamburger-btn" aria-label="Toggle navigation menu" aria-expanded="false" aria-controls="mobile-drawer">
        <span class="hamburger-line"></span>
        <span class="hamburger-line"></span>
        <span class="hamburger-line"></span>
      </button>
    </div>
  </div>

  <!-- Mobile Drawer Menu -->
  <div class="mobile-nav-drawer" id="mobile-drawer" aria-label="Mobile Navigation Drawer">
    <ul class="mobile-nav-list">
      <li class="mobile-nav-item">
        <a href="{rel}" class="mobile-nav-link {'active' if is_home else ''}">Home</a>
      </li>
      <li class="mobile-nav-item">
        <a href="{rel}about-us/" class="mobile-nav-link {'active' if is_about else ''}">About Us</a>
      </li>
      <li class="mobile-nav-item">
        <a href="{rel}services/" class="mobile-nav-link {'active' if is_services else ''}">All Home Care Services</a>
        <div class="mobile-submenu">
          {mobile_submenu}
        </div>
      </li>
      <li class="mobile-nav-item">
        <a href="{rel}contact-us/" class="mobile-nav-link {'active' if is_contact else ''}">Contact Us</a>
      </li>
    </ul>

    <div class="mobile-actions">
      <a href="tel:+918438861636" data-config="phoneTel" class="btn btn-primary btn-lg" style="width: 100%;">
        <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"></path></svg>
        Call Us Directly
      </a>
      <a href="https://wa.me/918438861636" data-config="whatsappLink" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp btn-lg" style="width: 100%;">
        <svg class="icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0012.04 2zm5.79 14.07c-.24.67-1.39 1.29-1.93 1.37-.5.08-1.12.11-3.56-.88-3.09-1.28-5.06-4.42-5.21-4.63-.16-.2-1.24-1.66-1.24-3.16 0-1.51.78-2.25 1.06-2.55.28-.3.61-.38.81-.38.2 0 .41 0 .59.01.19.01.44-.07.69.52.25.6.86 2.1.94 2.25.08.16.14.34.03.55-.11.21-.16.34-.32.53-.16.19-.34.42-.48.56-.16.16-.33.33-.14.65.19.32.84 1.38 1.8 2.24 1.24 1.11 2.28 1.45 2.61 1.61.32.16.51.14.7-.08.19-.22.82-.95 1.04-1.28.22-.32.44-.27.75-.16.3.11 1.93.91 2.26 1.08.33.16.55.25.63.39.08.13.08.77-.16 1.44z"></path></svg>
        Chat on WhatsApp
      </a>
    </div>
  </div>
</header>
'''

def get_footer(depth=0):
    rel = "./" if depth == 0 else "../"
    
    # Build footer services links
    footer_svc_links = ""
    for s in SERVICES_NAV:
        footer_svc_links += f'<li><a href="{rel}{s["slug"]}/" class="footer-link">{s["name"]}</a></li>\n          '

    return f'''<!-- Site Footer -->
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <!-- Col 1: About Sugam -->
      <div class="footer-col">
        <a href="{rel}" aria-label="Sugam Home Care Services">
          <img src="{rel}assets/images/logo.svg" alt="Sugam Home Care Services" width="200" height="44" style="filter: brightness(0) invert(1);">
        </a>
        <p class="footer-brand-p">
          Providing compassionate, personalized home care, senior care, bedridden patient support, cancer recovery, and qualified nursing services across Chennai and all over Tamil Nadu.
        </p>
        <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
          <span class="badge-tag" style="background-color: rgba(13, 148, 136, 0.2); color: #2DD4BF;">Chennai &amp; Tamil Nadu</span>
          <span class="badge-tag" style="background-color: rgba(255, 255, 255, 0.1); color: #E2E8F0;">24-Hr Service Available</span>
        </div>
      </div>

      <!-- Col 2: Quick Links -->
      <div class="footer-col">
        <h4>Company</h4>
        <ul class="footer-links">
          <li><a href="{rel}" class="footer-link">Home</a></li>
          <li><a href="{rel}about-us/" class="footer-link">About Us</a></li>
          <li><a href="{rel}services/" class="footer-link">All Services</a></li>
          <li><a href="{rel}contact-us/" class="footer-link">Contact Us</a></li>
          <li><a href="{rel}privacy-policy/" class="footer-link">Privacy Policy</a></li>
          <li><a href="{rel}terms-and-conditions/" class="footer-link">Terms and Conditions</a></li>
        </ul>
      </div>

      <!-- Col 3: Services (11 Approved) -->
      <div class="footer-col">
        <h4>Our Services</h4>
        <ul class="footer-links">
          {footer_svc_links}
        </ul>
      </div>

      <!-- Col 4: Office & Locations -->
      <div class="footer-col">
        <h4>Office &amp; Service Coverage</h4>
        <p style="color: #CBD5E1; font-size: 0.875rem; line-height: 1.5; margin-bottom: 0.75rem;">
          <strong style="color: #FFFFFF;">Sugam Home Care Services</strong><br>
          No. 123/12, Kattabomman Street,<br>
          Kamaraj Nagar, New Perungalathur,<br>
          Chennai – 600063, Tamil Nadu, India.
        </p>
        <p style="color: #CBD5E1; font-size: 0.875rem; margin-bottom: 0.5rem;">
          Phone: <a href="tel:+918438861636" data-config="phoneTel" style="color: #2DD4BF; font-weight: 700;"><span data-config="phoneDisplay">+91 84388 61636</span></a>
        </p>
        <p style="color: #CBD5E1; font-size: 0.875rem; margin-bottom: 0.5rem;">
          WhatsApp: <a href="https://wa.me/918438861636" data-config="whatsappLink" target="_blank" rel="noopener noreferrer" style="color: #25D366; font-weight: 700;">Chat on WhatsApp</a>
        </p>
        <div style="background: rgba(255, 255, 255, 0.05); padding: 0.75rem; border-radius: var(--radius-sm); border: 1px solid rgba(255, 255, 255, 0.1); margin-top: 0.75rem;">
          <p style="color: #2DD4BF; font-size: 0.825rem; font-weight: 700; margin-bottom: 0.25rem;">Coverage Notice:</p>
          <p style="color: #94A3B8; font-size: 0.775rem; line-height: 1.4; margin-bottom: 0;">
            Primary service available across 35+ Chennai localities (Tambaram, Vandalur, Guduvanchery, Sholinganallur, Navalur, OMR, ECR, Adyar, Velachery, Anna Nagar, Porur, etc.). Services across Tamil Nadu outside Chennai are provided on a One-Day Full (24-Hour) basis.
          </p>
        </div>
      </div>
    </div>

    <!-- Medical & Emergency Notice -->
    <div class="footer-disclaimer-box">
      <strong>Important Healthcare Notice:</strong> Sugam Home Care Services provides non-clinical household assistance, elderly/patient caregiving, and professional nursing coordination at home. We do not operate an emergency medical ambulance service or emergency room. In case of an acute or life-threatening medical emergency, please contact 108 or proceed immediately to the nearest hospital emergency department.
    </div>

    <!-- Bottom Copyright -->
    <div class="footer-bottom">
      <div>
        &copy; 2026 Sugam Home Care Services. All rights reserved.
      </div>
      <div class="footer-bottom-links">
        <a href="{rel}privacy-policy/">Privacy Policy</a>
        <a href="{rel}terms-and-conditions/">Terms & Conditions</a>
        <a href="{rel}contact-us/">Contact</a>
      </div>
    </div>
  </div>
</footer>

<!-- Mobile Sticky Bottom CTA Bar -->
<aside class="mobile-bottom-bar" aria-label="Quick Actions">
  <div class="mobile-bottom-grid">
    <a href="https://wa.me/918438861636" data-config="whatsappLink" target="_blank" rel="noopener noreferrer" class="mobile-bottom-btn btn-mobile-whatsapp">
      <svg class="icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0012.04 2zm5.79 14.07c-.24.67-1.39 1.29-1.93 1.37-.5.08-1.12.11-3.56-.88-3.09-1.28-5.06-4.42-5.21-4.63-.16-.2-1.24-1.66-1.24-3.16 0-1.51.78-2.25 1.06-2.55.28-.3.61-.38.81-.38.2 0 .41 0 .59.01.19.01.44-.07.69.52.25.6.86 2.1.94 2.25.08.16.14.34.03.55-.11.21-.16.34-.32.53-.16.19-.34.42-.48.56-.16.16-.33.33-.14.65.19.32.84 1.38 1.8 2.24 1.24 1.11 2.28 1.45 2.61 1.61.32.16.51.14.7-.08.19-.22.82-.95 1.04-1.28.22-.32.44-.27.75-.16.3.11 1.93.91 2.26 1.08.33.16.55.25.63.39.08.13.08.77-.16 1.44z"></path></svg>
      WhatsApp
    </a>
    <a href="tel:+918438861636" data-config="phoneTel" class="mobile-bottom-btn btn-mobile-call">
      <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"></path></svg>
      Call Now
    </a>
  </div>
</aside>

<!-- Modal: Quick Callback Enquiry (11 Services) -->
<div class="modal-overlay" id="callback-modal" role="dialog" aria-modal="true" aria-labelledby="modal-title">
  <div class="modal-card">
    <button type="button" class="modal-close-btn" aria-label="Close modal">&times;</button>
    <div style="text-align: center; margin-bottom: 1.25rem;">
      <span class="badge-tag">Quick Response</span>
      <h3 id="modal-title" style="margin-bottom: 0.25rem;">Request a Call Back</h3>
      <p style="font-size: 0.875rem; color: var(--text-muted); margin-bottom: 0;">Leave your contact details and our care coordinator will reach out shortly.</p>
    </div>
    <form class="lead-form modal-form">
      <div class="form-group">
        <label class="form-label">Full Name <span class="required">*</span></label>
        <input type="text" name="fullName" class="form-control" placeholder="e.g. Ramesh Kumar" required>
      </div>
      <div class="form-group">
        <label class="form-label">Phone Number <span class="required">*</span></label>
        <input type="tel" name="phone" class="form-control" placeholder="e.g. 8438861636" required>
      </div>
      <div class="form-group">
        <label class="form-label">Service Required <span class="required">*</span></label>
        <select name="service" id="modal-service-select" class="form-control form-select" required>
          <option value="">Select Service</option>
          <option value="Baby care services">Baby care services</option>
          <option value="Elderly care services">Elderly care services</option>
          <option value="Patient care services">Patient care services</option>
          <option value="Senior citizen care services">Senior citizen care services</option>
          <option value="Bedridden patient care services">Bedridden patient care services</option>
          <option value="Home health care for seniors">Home health care for seniors</option>
          <option value="Dementia care for the elderly">Dementia care for the elderly</option>
          <option value="Home care for cancer patients">Home care for cancer patients</option>
          <option value="Caretaker services at home">Caretaker services at home</option>
          <option value="Home nurse services">Home nurse services</option>
          <option value="Nursing Services">Nursing Services</option>
        </select>
      </div>
      <div class="form-consent">
        <input type="checkbox" name="consent" id="modal-consent" required checked>
        <label for="modal-consent">I agree to be contacted by Sugam Home Care Services regarding this enquiry.</label>
      </div>
      <button type="submit" class="btn btn-submit-lead">
        Request a Call Back
      </button>
    </form>
  </div>
</div>

<!-- Scripts -->
<script src="{rel}assets/js/config.js?v=7"></script>
<script src="{rel}assets/js/main.js?v=7"></script>
<script src="{rel}assets/js/form.js?v=7"></script>
'''

print("Updated site_templates.py successfully!")
