#!/usr/bin/env python3
import os
import sys

# Import our template helper
from site_templates import get_header, get_footer

ROOT_DIR = "/Users/karthik/.gemini/antigravity/scratch/sugam-home-care"

def write_page(relative_filepath, html_content):
    full_path = os.path.join(ROOT_DIR, relative_filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(html_content.strip() + "\n")
    print(f"Generated: {relative_filepath}")

# ---------------------------------------------------------------------------
# 1. HOME PAGE (index.html)
# ---------------------------------------------------------------------------
def generate_home_page():
    header = get_header("/", depth=0)
    footer = get_footer(depth=0)
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sugam Home Care Services Chennai | Compassionate Care at Home</title>
  <meta name="description" content="Sugam Home Care Services provides personalized home care, maid services, caretaker support, elderly care, baby care, patient care, and nursing services at home in Chennai.">
  <link rel="canonical" href="https://sugamhomecareservices.in/">
  <link rel="icon" type="image/svg+xml" href="assets/images/favicon.svg">
  
  <!-- Open Graph -->
  <meta property="og:title" content="Sugam Home Care Services | Compassionate Home Care in Chennai">
  <meta property="og:description" content="Personalized care and everyday assistance at home for your loved ones in Chennai. Enquire for maid, elderly care, patient care, and nursing services.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://sugamhomecareservices.in/">
  <meta property="og:image" content="https://sugamhomecareservices.in/assets/images/logo.svg">
  
  <!-- Styles -->
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="stylesheet" href="assets/css/components.css">

  <!-- Schema.org Structured Data -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "HomeHealthService",
    "name": "Sugam Home Care Services",
    "image": "https://sugamhomecareservices.in/assets/images/logo.svg",
    "url": "https://sugamhomecareservices.in/",
    "telephone": "+918438861636",
    "priceRange": "$$",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "No. 123/12, Kattabomman Street, Kamaraj Nagar, New Perungalathur",
      "addressLocality": "Chennai",
      "addressRegion": "Tamil Nadu",
      "postalCode": "600063",
      "addressCountry": "IN"
    }},
    "geo": {{
      "@type": "GeoCoordinates",
      "latitude": 12.9056,
      "longitude": 80.0825
    }},
    "areaServed": [
      "New Perungalathur",
      "Perungalathur",
      "Tambaram",
      "Chromepet",
      "Pallavaram",
      "Vandalur",
      "Guduvanchery",
      "Chennai"
    ],
    "description": "Compassionate home care services in Chennai including maid services, caretaker assistance, baby care, elderly care, patient care, and qualified home nursing."
  }}
  </script>
</head>
<body>

{header}

<main>
  <!-- SECTION A: HERO SECTION -->
  <section class="hero-section">
    <div class="container hero-grid">
      <!-- Left Column: Value Proposition & CTAs -->
      <div class="hero-content">
        <div class="hero-badge">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
          Dedicated Home Care in Chennai
        </div>
        
        <h1 class="hero-headline">
          Compassionate Home Care Services for <span class="accent-teal">Your Loved Ones</span>
        </h1>
        
        <p class="hero-description">
          Personalized care and everyday assistance at home, helping families find the support they need for their loved ones.
        </p>

        <!-- CTAs -->
        <div class="hero-cta-group">
          <a href="#enquiry-section" class="btn btn-primary btn-lg">
            Talk to Our Care Team
          </a>
          <a href="services/" class="btn btn-outline-primary btn-lg">
            Explore Our Services
          </a>
        </div>

        <!-- Visible Phone CTA -->
        <a href="tel:+918438861636" data-config="phoneTel" class="hero-phone-cta">
          <div class="hero-phone-icon-wrap">
            <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"></path></svg>
          </div>
          <span>Call Us for Care Inquiries: <strong data-config="phoneDisplay">+91 84388 61636</strong></span>
        </a>

        <!-- Trust Badges -->
        <div class="hero-trust-list">
          <div class="hero-trust-item">
            <svg class="hero-trust-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
            <span>In-Home Convenience</span>
          </div>
          <div class="hero-trust-item">
            <svg class="hero-trust-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
            <span>Personalized Care Plan</span>
          </div>
          <div class="hero-trust-item">
            <svg class="hero-trust-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
            <span>Family-Centered Service</span>
          </div>
          <div class="hero-trust-item">
            <svg class="hero-trust-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
            <span>Simple Enquiry Process</span>
          </div>
        </div>
      </div>

      <!-- Right Column: Hero Short Enquiry Form -->
      <div class="hero-card-wrapper" id="enquiry-section">
        <div class="enquiry-card">
          <div class="enquiry-card-header">
            <span class="badge-tag">Quick Consultation</span>
            <h2 class="enquiry-card-title">Request a Call Back</h2>
            <p class="enquiry-card-subtitle">Tell us what kind of home care assistance your family needs.</p>
          </div>

          <form class="lead-form" action="thank-you/" method="GET">
            <div class="form-group">
              <label class="form-label" for="hero-fullName">Full Name <span class="required">*</span></label>
              <input type="text" id="hero-fullName" name="fullName" class="form-control" placeholder="Enter your full name" required>
            </div>

            <div class="form-group">
              <label class="form-label" for="hero-phone">Phone Number <span class="required">*</span></label>
              <input type="tel" id="hero-phone" name="phone" class="form-control" placeholder="e.g. 8438861636" required>
            </div>

            <div class="form-group">
              <label class="form-label" for="hero-service">Service Required <span class="required">*</span></label>
              <select id="hero-service" name="service" class="form-control form-select" required>
                <option value="">Select a Home Care Service</option>
                <option value="Maid Services">Maid Services</option>
                <option value="Home Health Care Services">Home Health Care Services</option>
                <option value="Caretaker Services">Caretaker Services</option>
                <option value="Baby Care Taker">Baby Care Taker</option>
                <option value="Elderly Care Services">Elderly Care Services</option>
                <option value="Patient Care Services">Patient Care Services</option>
                <option value="Nursing Services at Home">Nursing Services at Home</option>
              </select>
            </div>

            <div class="form-group">
              <label class="form-label" for="hero-preferredTime">Preferred Contact Time <span style="font-size:0.75rem; color:var(--text-light);">(Optional)</span></label>
              <select id="hero-preferredTime" name="preferredTime" class="form-control form-select">
                <option value="Anytime (As soon as possible)">Anytime (As soon as possible)</option>
                <option value="Morning (9 AM - 12 PM)">Morning (9 AM - 12 PM)</option>
                <option value="Afternoon (12 PM - 4 PM)">Afternoon (12 PM - 4 PM)</option>
                <option value="Evening (4 PM - 8 PM)">Evening (4 PM - 8 PM)</option>
              </select>
            </div>

            <div class="form-consent">
              <input type="checkbox" id="hero-consent" name="consent" required checked>
              <label for="hero-consent">I agree to be contacted by Sugam Home Care Services to discuss my home care requirements.</label>
            </div>

            <button type="submit" class="btn-submit-lead">
              <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"></path></svg>
              Request a Call Back
            </button>

            <div class="form-security-note">
              <svg class="icon" style="width:14px; height:14px; color:var(--color-secondary);" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0110 0v4"></path></svg>
              Your contact details are strictly kept private for enquiry purposes.
            </div>
          </form>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION B: TRUST AND REASSURANCE -->
  <section class="section section-bg-surface">
    <div class="container">
      <div class="section-header">
        <span class="badge-tag">Why Families Trust Us</span>
        <h2>Support Designed for Your Family’s Peace of Mind</h2>
        <p class="section-subtitle">We focus on reliable, dignified care tailored to individual household and health needs.</p>
      </div>

      <div class="trust-grid">
        <div class="trust-card">
          <div class="trust-icon-box">🏡</div>
          <h3>Care at Home</h3>
          <p>Assistance delivered right where your family feels safest and most comfortable — in your own home environment.</p>
        </div>

        <div class="trust-card">
          <div class="trust-icon-box">📋</div>
          <h3>Personalized Support</h3>
          <p>Every family’s daily routine is distinct. We listen carefully to design care assistance that aligns with your specific schedule.</p>
        </div>

        <div class="trust-card">
          <div class="trust-icon-box">👨‍👩‍👧‍👦</div>
          <h3>Family-Focused Service</h3>
          <p>We work in close coordination with family members to ensure continuous updates, transparency, and caring attention.</p>
        </div>

        <div class="trust-card">
          <div class="trust-icon-box">💬</div>
          <h3>Easy Enquiry & Assistance</h3>
          <p>Clear, responsive communication via phone or WhatsApp. Discuss your needs without pressure or complex formalities.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION C: OUR HOME CARE SERVICES -->
  <section class="section">
    <div class="container">
      <div class="section-header">
        <span class="badge-tag">Comprehensive Care Solutions</span>
        <h2>Our Home Care Services</h2>
        <p class="section-subtitle">Explore our specialized services designed for Chennai households, senior citizens, infants, and recovering patients.</p>
      </div>

      <div class="services-grid">
        <!-- 1. Maid Services -->
        <article class="service-card">
          <div class="service-card-media">
            <img src="assets/images/service-maid.svg" alt="Reliable Maid Services in Chennai" class="service-card-img" width="600" height="400" loading="lazy">
            <span class="service-card-badge">Household Support</span>
          </div>
          <div class="service-card-body">
            <div class="service-card-header">
              <span class="service-card-icon">🧹</span>
              <h3 class="service-card-title"><a href="maid-services/">Maid Services</a></h3>
            </div>
            <p class="service-card-text">
              Reliable household assistance including daily sweeping, mopping, kitchen cleaning, dishwashing, and tidying to keep your home fresh.
            </p>
            <div class="service-card-features">
              <div class="service-feature-item">
                <svg class="service-feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                <span>Floor sweeping & wet mopping</span>
              </div>
              <div class="service-feature-item">
                <svg class="service-feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                <span>Kitchen slab & sink maintenance</span>
              </div>
            </div>
            <div class="service-card-actions">
              <a href="maid-services/" class="btn btn-outline-primary">Learn More</a>
              <button type="button" class="btn btn-primary btn-open-modal" data-service="Maid Services">Enquire</button>
            </div>
          </div>
        </article>

        <!-- 2. Home Health Care Services -->
        <article class="service-card">
          <div class="service-card-media">
            <img src="assets/images/service-home-health.svg" alt="Home Health Care Services Chennai" class="service-card-img" width="600" height="400" loading="lazy">
            <span class="service-card-badge">Health Management</span>
          </div>
          <div class="service-card-body">
            <div class="service-card-header">
              <span class="service-card-icon">🩺</span>
              <h3 class="service-card-title"><a href="home-health-care-services/">Home Health Care</a></h3>
            </div>
            <p class="service-card-text">
              Structured home health support, vitals monitoring (BP, sugar, pulse), medication supervision, and post-discharge recovery coordination.
            </p>
            <div class="service-card-features">
              <div class="service-feature-item">
                <svg class="service-feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                <span>Routine health vitals monitoring</span>
              </div>
              <div class="service-feature-item">
                <svg class="service-feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                <span>Post-hospitalization routine support</span>
              </div>
            </div>
            <div class="service-card-actions">
              <a href="home-health-care-services/" class="btn btn-outline-primary">Learn More</a>
              <button type="button" class="btn btn-primary btn-open-modal" data-service="Home Health Care Services">Enquire</button>
            </div>
          </div>
        </article>

        <!-- 3. Caretaker Services -->
        <article class="service-card">
          <div class="service-card-media">
            <img src="assets/images/service-caretaker.svg" alt="Caretaker Services in Chennai" class="service-card-img" width="600" height="400" loading="lazy">
            <span class="service-card-badge">Everyday Living</span>
          </div>
          <div class="service-card-body">
            <div class="service-card-header">
              <span class="service-card-icon">🤝</span>
              <h3 class="service-card-title"><a href="caretaker-services/">Caretaker Services</a></h3>
            </div>
            <p class="service-card-text">
              Attentive everyday assistance with mobility, feeding, personal grooming, medication reminders, and comforting companionship.
            </p>
            <div class="service-card-features">
              <div class="service-feature-item">
                <svg class="service-feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                <span>Assistance with daily activities</span>
              </div>
              <div class="service-feature-item">
                <svg class="service-feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                <span>Day or night care arrangements</span>
              </div>
            </div>
            <div class="service-card-actions">
              <a href="caretaker-services/" class="btn btn-outline-primary">Learn More</a>
              <button type="button" class="btn btn-primary btn-open-modal" data-service="Caretaker Services">Enquire</button>
            </div>
          </div>
        </article>

        <!-- 4. Baby Care Taker -->
        <article class="service-card">
          <div class="service-card-media">
            <img src="assets/images/service-baby-care.svg" alt="Baby Care Taker in Chennai" class="service-card-img" width="600" height="400" loading="lazy">
            <span class="service-card-badge">Mother & Child</span>
          </div>
          <div class="service-card-body">
            <div class="service-card-header">
              <span class="service-card-icon">👶</span>
              <h3 class="service-card-title"><a href="baby-care-taker/">Baby Care Taker</a></h3>
            </div>
            <p class="service-card-text">
              Gentle, dependable infant care support, feeding assistance, diaper changing, baby massage, and newborn routine support for resting mothers.
            </p>
            <div class="service-card-features">
              <div class="service-feature-item">
                <svg class="service-feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                <span>Gentle baby bathing & feeding care</span>
              </div>
              <div class="service-feature-item">
                <svg class="service-feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                <span>Support for new mothers resting at home</span>
              </div>
            </div>
            <div class="service-card-actions">
              <a href="baby-care-taker/" class="btn btn-outline-primary">Learn More</a>
              <button type="button" class="btn btn-primary btn-open-modal" data-service="Baby Care Taker">Enquire</button>
            </div>
          </div>
        </article>

        <!-- 5. Elderly Care Services -->
        <article class="service-card">
          <div class="service-card-media">
            <img src="assets/images/service-elderly-care.svg" alt="Elderly Care Services Chennai" class="service-card-img" width="600" height="400" loading="lazy">
            <span class="service-card-badge">Senior Dignity</span>
          </div>
          <div class="service-card-body">
            <div class="service-card-header">
              <span class="service-card-icon">🧓</span>
              <h3 class="service-card-title"><a href="elderly-care-services/">Elderly Care Services</a></h3>
            </div>
            <p class="service-card-text">
              Dignified, warm senior care supporting daily routines, fall prevention, walking assistance, medication reminders, and companionship.
            </p>
            <div class="service-card-features">
              <div class="service-feature-item">
                <svg class="service-feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                <span>Walking support & fall prevention</span>
              </div>
              <div class="service-feature-item">
                <svg class="service-feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                <span>Emotional support & companionship</span>
              </div>
            </div>
            <div class="service-card-actions">
              <a href="elderly-care-services/" class="btn btn-outline-primary">Learn More</a>
              <button type="button" class="btn btn-primary btn-open-modal" data-service="Elderly Care Services">Enquire</button>
            </div>
          </div>
        </article>

        <!-- 6. Patient Care Services -->
        <article class="service-card">
          <div class="service-card-media">
            <img src="assets/images/service-patient-care.svg" alt="Patient Care Services Chennai" class="service-card-img" width="600" height="400" loading="lazy">
            <span class="service-card-badge">Bedside Care</span>
          </div>
          <div class="service-card-body">
            <div class="service-card-header">
              <span class="service-card-icon">🛏️</span>
              <h3 class="service-card-title"><a href="patient-care-services/">Patient Care Services</a></h3>
            </div>
            <p class="service-card-text">
              Dedicated bedside assistance for bedridden or recovering individuals, sponge baths, diaper hygiene, and gentle physical positioning.
            </p>
            <div class="service-card-features">
              <div class="service-feature-item">
                <svg class="service-feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                <span>Bed positioning & personal hygiene</span>
              </div>
              <div class="service-feature-item">
                <svg class="service-feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                <span>Post-surgery bedside assistance</span>
              </div>
            </div>
            <div class="service-card-actions">
              <a href="patient-care-services/" class="btn btn-outline-primary">Learn More</a>
              <button type="button" class="btn btn-primary btn-open-modal" data-service="Patient Care Services">Enquire</button>
            </div>
          </div>
        </article>

        <!-- 7. Nursing Services at Home -->
        <article class="service-card" style="grid-column: span 1;">
          <div class="service-card-media">
            <img src="assets/images/service-nursing.svg" alt="Nursing Services at Home Chennai" class="service-card-img" width="600" height="400" loading="lazy">
            <span class="service-card-badge">Clinical Procedures</span>
          </div>
          <div class="service-card-body">
            <div class="service-card-header">
              <span class="service-card-icon">👩‍⚕️</span>
              <h3 class="service-card-title"><a href="nursing-services-at-home/">Nursing Services at Home</a></h3>
            </div>
            <p class="service-card-text">
              Qualified home nursing care for prescribed clinical procedures: injections, wound dressing, catheter care, IV fluids, and post-op nursing.
            </p>
            <div class="service-card-features">
              <div class="service-feature-item">
                <svg class="service-feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                <span>Sterile wound care & injection support</span>
              </div>
              <div class="service-feature-item">
                <svg class="service-feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                <span>Adherence to physician prescription</span>
              </div>
            </div>
            <div class="service-card-actions">
              <a href="nursing-services-at-home/" class="btn btn-outline-primary">Learn More</a>
              <button type="button" class="btn btn-primary btn-open-modal" data-service="Nursing Services at Home">Enquire</button>
            </div>
          </div>
        </article>
      </div>
    </div>
  </section>

  <!-- SECTION D: WHY CHOOSE SUGAM HOME CARE SERVICES? -->
  <section class="section section-bg-warm">
    <div class="container">
      <div class="section-header">
        <span class="badge-tag">Our Care Commitment</span>
        <h2>Why Choose Sugam Home Care Services?</h2>
        <p class="section-subtitle">We believe in compassionate care, honest communication, and respectful service delivery.</p>
      </div>

      <div class="benefits-grid">
        <div class="benefit-item">
          <div class="benefit-number">01</div>
          <h3>Care Tailored to Individual Needs</h3>
          <p>We take time to understand your family member’s routine, medical background, and personal habits before suggesting care assistance.</p>
        </div>

        <div class="benefit-item">
          <div class="benefit-number">02</div>
          <h3>Support in the Comfort of Home</h3>
          <p>Familiar home surroundings promote emotional security, faster healing, and dignity for seniors and recovering patients.</p>
        </div>

        <div class="benefit-item">
          <div class="benefit-number">03</div>
          <h3>Convenient Communication with Our Team</h3>
          <p>Reach us easily via phone or WhatsApp. We remain accessible to answer questions and adjust schedules as requirements change.</p>
        </div>

        <div class="benefit-item">
          <div class="benefit-number">04</div>
          <h3>Attention to Family Preferences</h3>
          <p>From dietary routines to language comfort (Tamil & English speaking staff), we respect what matters most to your household.</p>
        </div>

        <div class="benefit-item">
          <div class="benefit-number">05</div>
          <h3>Simple Enquiry & Consultation Process</h3>
          <p>No complicated contracts or hidden clauses. We provide clear explanations of duties, hours, and available options upfront.</p>
        </div>

        <div class="benefit-item" style="background: linear-gradient(135deg, #0F2C59 0%, #1E3A8A 100%); color: #FFFFFF;">
          <div class="benefit-number" style="background: rgba(255,255,255,0.2); color: #FFFFFF;">✓</div>
          <h3 style="color:#FFFFFF;">Discuss Your Care Requirements</h3>
          <p style="color:#E2E8F0;">Need assistance choosing between general caretaking and clinical nursing? Our team is happy to guide you.</p>
          <a href="#enquiry-section" class="btn btn-secondary btn-sm" style="margin-top:auto; align-self:flex-start;">Request a Consultation</a>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION E: HOW IT WORKS -->
  <section class="section">
    <div class="container">
      <div class="section-header">
        <span class="badge-tag">Simple & Transparent</span>
        <h2>How It Works</h2>
        <p class="section-subtitle">Arranging dependable home care support for your family is simple and straightforward.</p>
      </div>

      <div class="steps-grid">
        <div class="step-card">
          <div class="step-badge">1</div>
          <h3>Tell Us What You Need</h3>
          <p>Submit our simple enquiry form, call our number, or send a message on WhatsApp outlining your requirements.</p>
        </div>

        <div class="step-card">
          <div class="step-badge">2</div>
          <h3>Discuss With Our Team</h3>
          <p>We review specific needs, preferred timings (day, night, 12-hour, or 24-hour), and location in Chennai.</p>
        </div>

        <div class="step-card">
          <div class="step-badge">3</div>
          <h3>Review Suitable Options</h3>
          <p>We identify suitable care professionals matching your requested assistance, experience, and household preferences.</p>
        </div>

        <div class="step-card">
          <div class="step-badge">4</div>
          <h3>Arrange Service After Confirmation</h3>
          <p>Once you are completely satisfied with the proposed plan, service commences with ongoing family coordination.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION F: SERVICE-SPECIFIC CARE HIGHLIGHTS -->
  <section class="section section-bg-surface">
    <div class="container">
      <div class="section-header">
        <span class="badge-tag">Tailored Service Categories</span>
        <h2>Understanding the Levels of Care We Provide</h2>
        <p class="section-subtitle">We clearly differentiate everyday household help, general caregiving, and professional clinical nursing.</p>
      </div>

      <div class="highlights-grid">
        <!-- Highlight 1: Everyday Household Needs -->
        <div class="highlight-box">
          <div class="highlight-icon">🧹</div>
          <h3>Support for Everyday Household Needs</h3>
          <p>
            Designed for busy families, working professionals, and seniors needing dependable daily domestic help. Our maid services cover sweeping, mopping, kitchen dishwashing, surface dusting, and household orderliness.
          </p>
          <div class="highlight-scope-tag">Scope: Non-Medical Household Maintenance</div>
        </div>

        <!-- Highlight 2: Personal Assistance for Families and Seniors -->
        <div class="highlight-box teal-accent">
          <div class="highlight-icon">🤝</div>
          <h3>Personal Assistance for Families & Seniors</h3>
          <p>
            Compassionate non-medical caregiving. Caretakers assist with bathing, dressing, meal feeding, medication reminders, walking support, and comforting conversation for seniors or recovering adults.
          </p>
          <div class="highlight-scope-tag">Scope: Non-Medical Caregiving & Companionship</div>
        </div>

        <!-- Highlight 3: Home-Based Patient & Nursing Support -->
        <div class="highlight-box amber-accent">
          <div class="highlight-icon">👩‍⚕️</div>
          <h3>Home-Based Patient & Nursing Support</h3>
          <p>
            For individuals with medical requirements. Professional nurses administer physician-prescribed injections, dressing of surgical wounds, catheter management, and clinical vitals monitoring.
          </p>
          <div class="highlight-scope-tag">Scope: Qualified Clinical Nursing (Prescription Required)</div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION G: FREQUENTLY ASKED QUESTIONS -->
  <section class="section">
    <div class="container">
      <div class="section-header">
        <span class="badge-tag">Got Questions?</span>
        <h2>Frequently Asked Questions</h2>
        <p class="section-subtitle">Find answers to common questions about our home care services in Chennai.</p>
      </div>

      <div class="faq-container">
        <!-- FAQ 1 -->
        <div class="faq-item">
          <button type="button" class="faq-question">
            <span>What home care services do you provide?</span>
            <svg class="faq-icon-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </button>
          <div class="faq-answer">
            <div class="faq-answer-inner">
              Sugam Home Care Services provides seven dedicated services: Maid Services, Home Health Care Services, Caretaker Services, Baby Care Taker, Elderly Care Services, Patient Care Services, and Nursing Services at Home.
            </div>
          </div>
        </div>

        <!-- FAQ 2 -->
        <div class="faq-item">
          <button type="button" class="faq-question">
            <span>How can I enquire about a caregiver?</span>
            <svg class="faq-icon-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </button>
          <div class="faq-answer">
            <div class="faq-answer-inner">
              You can simply fill out the short enquiry form on our website, call our phone number directly, or send us a message on WhatsApp. Our care coordinator will discuss your loved one’s specific requirements and guide you through available options.
            </div>
          </div>
        </div>

        <!-- FAQ 3 -->
        <div class="faq-item">
          <button type="button" class="faq-question">
            <span>Do you provide elderly care services at home?</span>
            <svg class="faq-icon-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </button>
          <div class="faq-answer">
            <div class="faq-answer-inner">
              Yes, we provide dedicated Elderly Care Services. Our caretakers support seniors with daily mobility, bathing and grooming assistance, timely medication reminders, companionship, and everyday household comfort.
            </div>
          </div>
        </div>

        <!-- FAQ 4 -->
        <div class="faq-item">
          <button type="button" class="faq-question">
            <span>Can I enquire about nursing services at home?</span>
            <svg class="faq-icon-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </button>
          <div class="faq-answer">
            <div class="faq-answer-inner">
              Yes. For medical procedures such as wound dressings, injection administration, IV fluid management, or urinary catheter care, we coordinate qualified home nurses. Please note that clinical procedures require a valid doctor’s prescription.
            </div>
          </div>
        </div>

        <!-- FAQ 5 -->
        <div class="faq-item">
          <button type="button" class="faq-question">
            <span>How do I request baby care assistance?</span>
            <svg class="faq-icon-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </button>
          <div class="faq-answer">
            <div class="faq-answer-inner">
              Select "Baby Care Taker" in our enquiry form or WhatsApp us with your baby's age and desired timing. We will discuss your family's preferences and arrange an experienced baby caretaker to assist with feeding, massage, bathing, and baby routine care.
            </div>
          </div>
        </div>

        <!-- FAQ 6 -->
        <div class="faq-item">
          <button type="button" class="faq-question">
            <span>How can I find out about service availability?</span>
            <svg class="faq-icon-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </button>
          <div class="faq-answer">
            <div class="faq-answer-inner">
              Service availability depends on your specific locality in Chennai (such as New Perungalathur, Tambaram, Chromepet, Vandalur, etc.) and required shift hours. Please reach out to our team with your location for accurate availability confirmation.
            </div>
          </div>
        </div>

        <!-- FAQ 7 -->
        <div class="faq-item">
          <button type="button" class="faq-question">
            <span>How are service charges determined?</span>
            <svg class="faq-icon-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </button>
          <div class="faq-answer">
            <div class="faq-answer-inner">
              Charges are transparently calculated based on the type of service (general housekeeping, caregiving, or clinical nursing), the daily hours required (part-time, 12-hour day/night, or 24-hour), and the level of patient assistance needed. We discuss all costs clearly before service confirmation.
            </div>
          </div>
        </div>

        <!-- FAQ 8 -->
        <div class="faq-item">
          <button type="button" class="faq-question">
            <span>How can I contact Sugam Home Care Services?</span>
            <svg class="faq-icon-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </button>
          <div class="faq-answer">
            <div class="faq-answer-inner">
              You can call us directly at <strong data-config="phoneDisplay">+91 84388 61636</strong>, send a WhatsApp message, or visit our office at No. 123/12, Kattabomman Street, Kamaraj Nagar, New Perungalathur, Chennai – 600063.
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION H: FINAL CTA BANNER -->
  <section class="final-cta-section">
    <div class="container final-cta-box">
      <span class="badge-tag" style="background-color: rgba(255,255,255,0.15); color: #2DD4BF;">Ready to Get Started?</span>
      <h2>Looking for Home Care Support for Your Family?</h2>
      <p>
        Tell us what kind of assistance you need. Our team can discuss your requirements and the available service options.
      </p>
      <div class="final-cta-buttons">
        <a href="tel:+918438861636" data-config="phoneTel" class="btn btn-white btn-lg">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"></path></svg>
          Call Now
        </a>
        <a href="https://wa.me/918438861636" data-config="whatsappLink" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp btn-lg">
          <svg class="icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0012.04 2zm5.79 14.07c-.24.67-1.39 1.29-1.93 1.37-.5.08-1.12.11-3.56-.88-3.09-1.28-5.06-4.42-5.21-4.63-.16-.2-1.24-1.66-1.24-3.16 0-1.51.78-2.25 1.06-2.55.28-.3.61-.38.81-.38.2 0 .41 0 .59.01.19.01.44-.07.69.52.25.6.86 2.1.94 2.25.08.16.14.34.03.55-.11.21-.16.34-.32.53-.16.19-.34.42-.48.56-.16.16-.33.33-.14.65.19.32.84 1.38 1.8 2.24 1.24 1.11 2.28 1.45 2.61 1.61.32.16.51.14.7-.08.19-.22.82-.95 1.04-1.28.22-.32.44-.27.75-.16.3.11 1.93.91 2.26 1.08.33.16.55.25.63.39.08.13.08.77-.16 1.44z"></path></svg>
          WhatsApp Us
        </a>
        <a href="#enquiry-section" class="btn btn-secondary btn-lg">
          Request a Call Back
        </a>
      </div>
    </div>
  </section>

  <!-- SECTION I: CONTACT AND LOCATION -->
  <section class="section section-bg-surface">
    <div class="container">
      <div class="section-header">
        <span class="badge-tag">Reach Out to Us</span>
        <h2>Contact & Office Location</h2>
        <p class="section-subtitle">Conveniently located in New Perungalathur, serving households across Chennai.</p>
      </div>

      <div class="contact-details-grid">
        <!-- Office Details Card -->
        <div class="contact-info-card">
          <div class="contact-info-item">
            <div class="contact-icon-wrapper">📍</div>
            <div class="contact-info-content">
              <h4>Registered Office Address</h4>
              <p>
                <strong>Sugam Home Care Services</strong><br>
                No. 123/12, Kattabomman Street,<br>
                Kamaraj Nagar, New Perungalathur,<br>
                Chennai – 600063, Tamil Nadu, India.
              </p>
            </div>
          </div>

          <div class="contact-info-item">
            <div class="contact-icon-wrapper">📞</div>
            <div class="contact-info-content">
              <h4>Phone Support</h4>
              <p>
                <a href="tel:+918438861636" data-config="phoneTel" style="color:var(--color-primary); font-weight:700;">
                  <span data-config="phoneDisplay">+91 84388 61636</span>
                </a>
              </p>
              <p style="font-size:0.85rem; color:var(--text-light);">Available during regular consultation hours</p>
            </div>
          </div>

          <div class="contact-info-item">
            <div class="contact-icon-wrapper">💬</div>
            <div class="contact-info-content">
              <h4>WhatsApp Quick Chat</h4>
              <p>
                <a href="https://wa.me/918438861636" data-config="whatsappLink" target="_blank" rel="noopener noreferrer" style="color:var(--color-whatsapp-dark); font-weight:700;">
                  Chat with Our Care Team
                </a>
              </p>
              <p style="font-size:0.85rem; color:var(--text-light);">Send us your requirements anytime</p>
            </div>
          </div>

          <div class="contact-info-item">
            <div class="contact-icon-wrapper">🗺️</div>
            <div class="contact-info-content">
              <h4>Key Chennai Service Localities</h4>
              <div class="service-areas-pills">
                <span class="area-pill">New Perungalathur</span>
                <span class="area-pill">Perungalathur</span>
                <span class="area-pill">Tambaram</span>
                <span class="area-pill">Chromepet</span>
                <span class="area-pill">Pallavaram</span>
                <span class="area-pill">Vandalur</span>
                <span class="area-pill">Guduvanchery</span>
                <span class="area-pill">Medavakkam</span>
                <span class="area-pill">Velachery</span>
                <span class="area-pill">Greater Chennai</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Location Map / Office Representation -->
        <div class="contact-info-card" style="padding: 1.5rem; display: flex; flex-direction: column;">
          <h3 style="margin-bottom: 0.5rem; font-size: 1.25rem;">Our Service Area in Chennai</h3>
          <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 1rem;">
            We coordinate home care visits across South Chennai and surrounding neighborhoods from our New Perungalathur office.
          </p>
          <div style="width: 100%; height: 320px; border-radius: var(--radius-lg); overflow: hidden; border: 1px solid var(--border-light); position: relative; background-color: var(--bg-neutral);">
            <!-- Interactive Map Embed -->
            <iframe 
              title="Sugam Home Care Services Office Location"
              src="https://maps.google.com/maps?q=Kattabomman%20Street%2C%20New%20Perungalathur%2C%20Chennai%20600063&t=&z=14&ie=UTF8&iwloc=&output=embed" 
              width="100%" 
              height="100%" 
              style="border:0;" 
              allowfullscreen="" 
              loading="lazy" 
              referrerpolicy="no-referrer-when-downgrade">
            </iframe>
          </div>
          <div style="margin-top: 1rem; text-align: center;">
            <a href="https://maps.google.com/?q=Kattabomman+Street+New+Perungalathur+Chennai+600063" target="_blank" rel="noopener noreferrer" class="btn btn-outline-primary btn-sm">
              Open in Google Maps
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
</main>

{footer}

</body>
</html>'''

    write_page("index.html", html)

generate_home_page()
print("Home page built successfully!")
