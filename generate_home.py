#!/usr/bin/env python3
import os
import sys

from site_templates import get_header, get_footer

ROOT_DIR = "/Users/karthik/.gemini/antigravity/scratch/sugam-home-care"

LOCATIONS = [
    "Tambaram", "Vandalur", "Guduvanchery", "Sholinganallur", "Navalur", "OMR", "ECR", 
    "Adyar", "Velachery", "Nanganallur", "Madipakkam", "Pallavaram", "Chromepet", 
    "Alandur", "Guindy", "Adambakkam", "Taramani", "Nungambakkam", "Kodambakkam", 
    "Chetpet", "Egmore", "Thousand Lights", "Royapettah", "Anna Nagar", "Mogappair", 
    "Ambattur", "Avadi", "Porur", "Iyyappanthangal", "Ayanavaram", "Royapuram", 
    "Purasawalkam", "Panaiyur", "Thoraipakkam", "Perungudi", "T. Nagar", "Ashok Nagar"
]

SERVICES_HOME = [
    {
        "id": "baby-care-services",
        "slug": "baby-care-services",
        "name": "Baby care services",
        "badge": "Infant & Mother",
        "icon": "👶",
        "image": "service-baby-care.svg",
        "desc": "Tender infant care, newborn massage, warm bath assistance, bottle feeding, and soothing routine support for resting mothers.",
        "feat1": "Newborn oil massage & warm bath",
        "feat2": "Mother postpartum rest support"
    },
    {
        "id": "elderly-care-services",
        "slug": "elderly-care-services",
        "name": "Elderly care services",
        "badge": "Senior Well-Being",
        "icon": "🧓",
        "image": "service-elderly-care.svg",
        "desc": "Dignified, warm senior care supporting daily routines, mobility assistance, fall prevention, personal hygiene, and loving companionship.",
        "feat1": "Fall prevention & walking support",
        "feat2": "Medication reminders & companionship"
    },
    {
        "id": "patient-care-services",
        "slug": "patient-care-services",
        "name": "Patient care services",
        "badge": "Bedside Recovery",
        "icon": "🛏️",
        "image": "service-patient-care.svg",
        "desc": "Dedicated bedside assistance for recovering patients, mobility support, sponge bathing, feeding, and personal hygiene upkeep at home.",
        "feat1": "Sponge bath & personal hygiene",
        "feat2": "Post-surgery recovery assistance"
    },
    {
        "id": "senior-citizen-care-services",
        "slug": "senior-citizen-care-services",
        "name": "Senior citizen care services",
        "badge": "Senior Assistance",
        "icon": "👴",
        "image": "service-senior-citizen.svg",
        "desc": "Comprehensive senior citizen support promoting healthy daily routines, nutritious meal assistance, and empathetic presence.",
        "feat1": "Daily living & mobility support",
        "feat2": "Mental engagement & social presence"
    },
    {
        "id": "bedridden-patient-care-services",
        "slug": "bedridden-patient-care-services",
        "name": "Bedridden patient care services",
        "badge": "Intensive Bedside",
        "icon": "🛌",
        "image": "service-bedridden.svg",
        "desc": "Specialized bed care: 2-hour body repositioning, bedsore prevention, bed bathing, adult diaper hygiene, and gentle feeding.",
        "feat1": "2-hour body turning & bedsore prevention",
        "feat2": "Adult diaper hygiene & catheter support"
    },
    {
        "id": "home-health-care-for-seniors",
        "slug": "home-health-care-for-seniors",
        "name": "Home health care for seniors",
        "badge": "Health Monitoring",
        "icon": "🩺",
        "image": "service-home-health.svg",
        "desc": "Structured health monitoring for elders: blood pressure, sugar, pulse tracking, medication adherence, and doctor coordination.",
        "feat1": "Routine vitals tracking (BP/SpO2/Sugar)",
        "feat2": "Physician schedule supervision"
    },
    {
        "id": "dementia-care-for-the-elderly",
        "slug": "dementia-care-for-the-elderly",
        "name": "Dementia care for the elderly",
        "badge": "Specialized Memory",
        "icon": "🧠",
        "image": "service-dementia.svg",
        "desc": "Specialized cognitive support, calm daily routines, reassurance, and continuous safety oversight for seniors with Alzheimer's and memory loss.",
        "feat1": "Safe wandering prevention & patience",
        "feat2": "Reassuring familiar memory routines"
    },
    {
        "id": "home-care-for-cancer-patients",
        "slug": "home-care-for-cancer-patients",
        "name": "Home care for cancer patients",
        "badge": "Supportive Oncology",
        "icon": "🎗️",
        "image": "service-cancer-care.svg",
        "desc": "Compassionate oncology support: post-chemotherapy recovery assistance, comfort positioning, nutrition tracking, and palliative care.",
        "feat1": "Post-chemo comfort & recovery support",
        "feat2": "Hydration tracking & gentle palliative care"
    },
    {
        "id": "caretaker-services-at-home",
        "slug": "caretaker-services-at-home",
        "name": "Caretaker services at home",
        "badge": "Everyday Living",
        "icon": "🤝",
        "image": "service-caretaker.svg",
        "desc": "Attentive everyday assistance with bathing, dressing, meal feeding, medication reminders, and comforting companion care.",
        "feat1": "Assistance with daily activities",
        "feat2": "Day, night, or 24-hr live-in shifts"
    },
    {
        "id": "home-nurse-services",
        "slug": "home-nurse-services",
        "name": "Home nurse services",
        "badge": "Home Nursing",
        "icon": "👩‍⚕️",
        "image": "service-home-nurse.svg",
        "desc": "Qualified visiting or shift-based nurses for clinical procedures, injections, wound dressings, IV therapy, and recovery supervision.",
        "feat1": "Visiting or full-day nurse arrangements",
        "feat2": "Clinical procedures under prescription"
    },
    {
        "id": "nursing-services",
        "slug": "nursing-services",
        "name": "Nursing Services",
        "badge": "Clinical Procedures",
        "icon": "💉",
        "image": "service-nursing.svg",
        "desc": "Clinical nursing at home under medical prescription: sterile dressing, IV line care, catheterization, Ryle's tube, and post-op care.",
        "feat1": "Sterile wound dressing & IV cannula care",
        "feat2": "Strict aseptic hospital standards"
    }
]

def generate_home_page():
    header = get_header("/", depth=0)
    footer = get_footer(depth=0)
    
    # Build service cards HTML
    service_cards_html = ""
    for s in SERVICES_HOME:
        service_cards_html += f'''
        <!-- {s["name"]} -->
        <article class="service-card">
          <div class="service-card-media">
            <img src="assets/images/{s["image"]}" alt="{s["name"]} in Chennai" class="service-card-img" width="600" height="400" loading="lazy">
            <span class="service-card-badge">{s["badge"]}</span>
          </div>
          <div class="service-card-body">
            <div class="service-card-header">
              <span class="service-card-icon">{s["icon"]}</span>
              <h3 class="service-card-title"><a href="{s["slug"]}/">{s["name"]}</a></h3>
            </div>
            <p class="service-card-text">{s["desc"]}</p>
            <div class="service-card-features">
              <div class="service-feature-item">
                <svg class="service-feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                <span>{s["feat1"]}</span>
              </div>
              <div class="service-feature-item">
                <svg class="service-feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                <span>{s["feat2"]}</span>
              </div>
            </div>
            <div class="service-card-actions">
              <a href="{s["slug"]}/" class="btn btn-outline-primary">Learn More</a>
              <button type="button" class="btn btn-primary btn-open-modal" data-service="{s["name"]}">Enquire</button>
            </div>
          </div>
        </article>'''

    # Build location pills HTML
    loc_pills_html = ""
    for loc in LOCATIONS:
        loc_pills_html += f'<span class="area-pill">{loc}</span>\n                '

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sugam Home Care Services Chennai | Compassionate Care at Home</title>
  <meta name="description" content="Sugam Home Care Services provides personalized home care, senior care, elderly care, patient care, bedridden care, cancer recovery, dementia care, and qualified home nursing across Chennai and all over Tamil Nadu.">
  <link rel="canonical" href="https://sugamhomecareservices.in/">
  <link rel="icon" type="image/svg+xml" href="assets/images/favicon.svg">
  
  <!-- Open Graph -->
  <meta property="og:title" content="Sugam Home Care Services | Compassionate Home Care in Chennai & Tamil Nadu">
  <meta property="og:description" content="Personalized care and everyday assistance at home for your loved ones in Chennai and Tamil Nadu. Enquire for elderly, patient, bedridden, dementia, and nursing services.">
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
      "Chennai", "Tambaram", "Vandalur", "Guduvanchery", "Sholinganallur", "Navalur", "OMR", "ECR", 
      "Adyar", "Velachery", "Pallavaram", "Chromepet", "Anna Nagar", "Porur", "Tamil Nadu"
    ],
    "description": "Compassionate home care services in Chennai and across Tamil Nadu including baby care, elderly care, patient care, senior citizen support, bedridden care, dementia care, cancer home care, and qualified nursing."
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
          Chennai &amp; All Over Tamil Nadu
        </div>
        
        <h1 class="hero-headline">
          Compassionate Home Care Services for <span class="accent-teal">Your Loved Ones</span>
        </h1>
        
        <p class="hero-description">
          Personalized care and everyday assistance at home, helping families find the support they need for elderly parents, recovering patients, infants, and special medical care.
        </p>

        <!-- CTAs -->
        <div class="hero-cta-group">
          <a href="#enquiry-section" class="btn btn-primary btn-lg">
            Talk to Our Care Team
          </a>
          <a href="services/" class="btn btn-outline-primary btn-lg">
            Explore All 11 Services
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
            <span>Tamil Nadu Wide Coverage</span>
          </div>
          <div class="hero-trust-item">
            <svg class="hero-trust-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
            <span>24/7 Shift Options Available</span>
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
          <h3>Easy Enquiry &amp; Assistance</h3>
          <p>Clear, responsive communication via phone or WhatsApp. Discuss your needs without pressure or complex formalities.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION C: OUR 11 HOME CARE SERVICES -->
  <section class="section">
    <div class="container">
      <div class="section-header">
        <span class="badge-tag">Comprehensive Care Solutions</span>
        <h2>Our Home Care Services</h2>
        <p class="section-subtitle">Explore our 11 specialized services designed for senior citizens, bedridden individuals, cancer recovery, dementia patients, infants, and medical home care.</p>
      </div>

      <div class="services-grid">
        {service_cards_html}
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
          <p>From dietary routines to language comfort (Tamil &amp; English speaking staff), we respect what matters most to your household.</p>
        </div>

        <div class="benefit-item">
          <div class="benefit-number">05</div>
          <h3>Simple Enquiry &amp; Consultation Process</h3>
          <p>No complicated contracts or hidden clauses. We provide clear explanations of duties, hours, and available options upfront.</p>
        </div>

        <div class="benefit-item" style="background: linear-gradient(135deg, #0F2C59 0%, #1E3A8A 100%); color: #FFFFFF;">
          <div class="benefit-number" style="background: rgba(255,255,255,0.2); color: #FFFFFF;">✓</div>
          <h3 style="color:#FFFFFF;">Discuss Your Care Requirements</h3>
          <p style="color:#E2E8F0;">Need assistance choosing between daily caretaking and clinical nursing? Our team is happy to guide you.</p>
          <a href="#enquiry-section" class="btn btn-secondary btn-sm" style="margin-top:auto; align-self:flex-start;">Request a Consultation</a>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION E: HOW IT WORKS -->
  <section class="section">
    <div class="container">
      <div class="section-header">
        <span class="badge-tag">Simple &amp; Transparent</span>
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
          <p>We review specific needs, preferred timings (day, night, 12-hour, or 24-hour), and location in Chennai or Tamil Nadu.</p>
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
        <span class="badge-tag">Levels of Care</span>
        <h2>Understanding the Categories of Care We Provide</h2>
        <p class="section-subtitle">We offer structured solutions ranging from daily personal support to advanced bedside recovery and clinical nursing.</p>
      </div>

      <div class="highlights-grid">
        <!-- Highlight 1: Senior & Elderly Care -->
        <div class="highlight-box">
          <div class="highlight-icon">🧓</div>
          <h3>Senior Citizen &amp; Elderly Living Care</h3>
          <p>
            Designed for senior parents living independently or needing everyday assistance. Caretakers support mobility, fall prevention, personal hygiene, nutritious meals, medication reminders, and empathetic companionship.
          </p>
          <div class="highlight-scope-tag">Scope: Non-Medical Caregiving &amp; Companionship</div>
        </div>

        <!-- Highlight 2: Specialized Bedside & Oncology Care -->
        <div class="highlight-box teal-accent">
          <div class="highlight-icon">🛌</div>
          <h3>Bedridden, Dementia &amp; Cancer Patient Care</h3>
          <p>
            Specialized in-home care for patients with higher dependency: 2-hour body repositioning to prevent bedsores, post-chemotherapy comfort support, calm memory care routines for dementia, and catheter/hygiene management.
          </p>
          <div class="highlight-scope-tag">Scope: Advanced Bedside &amp; Oncology Support</div>
        </div>

        <!-- Highlight 3: Clinical Home Nursing -->
        <div class="highlight-box amber-accent">
          <div class="highlight-icon">👩‍⚕️</div>
          <h3>Home Nurse &amp; Clinical Nursing Services</h3>
          <p>
            Delivered by qualified nurses under physician prescription: IM/IV injections, sterile dressing of surgical incisions or chronic ulcers, IV fluids, urinary catheterization, and Ryle's tube care.
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
        <p class="section-subtitle">Find answers to common questions about our home care services in Chennai and across Tamil Nadu.</p>
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
              Sugam Home Care Services provides 11 dedicated services: Baby care services, Elderly care services, Patient care services, Senior citizen care services, Bedridden patient care services, Home health care for seniors, Dementia care for the elderly, Home care for cancer patients, Caretaker services at home, Home nurse services, and Nursing Services.
            </div>
          </div>
        </div>

        <!-- FAQ 2 -->
        <div class="faq-item">
          <button type="button" class="faq-question">
            <span>Which locations in Chennai do you cover?</span>
            <svg class="faq-icon-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </button>
          <div class="faq-answer">
            <div class="faq-answer-inner">
              We cover 35+ major areas across Chennai including Tambaram, Vandalur, Guduvanchery, Sholinganallur, Navalur, OMR, ECR, Adyar, Velachery, Nanganallur, Madipakkam, Pallavaram, Chromepet, Alandur, Guindy, Adambakkam, Taramani, Nungambakkam, Kodambakkam, Chetpet, Egmore, Thousand Lights, Royapettah, Anna Nagar, Mogappair, Ambattur, Avadi, Porur, Iyyappanthangal, Ayanavaram, Royapuram, Purasawalkam, Panaiyur, Thoraipakkam, Perungudi, T. Nagar, and Ashok Nagar.
            </div>
          </div>
        </div>

        <!-- FAQ 3 -->
        <div class="faq-item">
          <button type="button" class="faq-question">
            <span>Do you provide home care services outside Chennai across Tamil Nadu?</span>
            <svg class="faq-icon-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </button>
          <div class="faq-answer">
            <div class="faq-answer-inner">
              Yes! We provide home care services all over Tamil Nadu. Please note that outside our primary Chennai coverage areas, services across Tamil Nadu are provided exclusively on a One-Day Full (24-Hour / Full-Day) care basis.
            </div>
          </div>
        </div>

        <!-- FAQ 4 -->
        <div class="faq-item">
          <button type="button" class="faq-question">
            <span>How do you support bedridden and paralyzed patients?</span>
            <svg class="faq-icon-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </button>
          <div class="faq-answer">
            <div class="faq-answer-inner">
              Our Bedridden Patient Care Services focus on regular 2-hour position turning to prevent bedsores, meticulous perineal hygiene and diaper changes, sponge bathing in bed, passive limb movement, and gentle feeding support.
            </div>
          </div>
        </div>

        <!-- FAQ 5 -->
        <div class="faq-item">
          <button type="button" class="faq-question">
            <span>What support is provided for dementia and Alzheimer's patients?</span>
            <svg class="faq-icon-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </button>
          <div class="faq-answer">
            <div class="faq-answer-inner">
              Our Dementia Care for the Elderly focuses on patient safety, preventing unsupervised wandering, maintaining familiar reassuring routines, assisting with bathing and eating with gentle encouragement, and reducing agitation.
            </div>
          </div>
        </div>

        <!-- FAQ 6 -->
        <div class="faq-item">
          <button type="button" class="faq-question">
            <span>Do you provide home care for cancer recovery and palliative care?</span>
            <svg class="faq-icon-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </button>
          <div class="faq-answer">
            <div class="faq-answer-inner">
              Yes. Our Home Care for Cancer Patients provides gentle bedside support, post-chemotherapy and radiation comfort care, hydration monitoring, nausea relief positioning, and emotional companionship in the peaceful environment of your home.
            </div>
          </div>
        </div>

        <!-- FAQ 7 -->
        <div class="faq-item">
          <button type="button" class="faq-question">
            <span>Can I enquire about clinical home nurse services?</span>
            <svg class="faq-icon-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </button>
          <div class="faq-answer">
            <div class="faq-answer-inner">
              Yes. Qualified nurses visit or stay on shift for physician-prescribed injections, IV fluid infusions, sterile wound dressings, and catheter care. A valid doctor’s prescription is required for all clinical procedures.
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
        Tell us what kind of assistance you need. Our team can discuss your requirements and available service options across Chennai and Tamil Nadu.
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

  <!-- SECTION I: CONTACT AND LOCATION WITH ALL 37 CHENNAI LOCATIONS + TAMIL NADU NOTE -->
  <section class="section section-bg-surface">
    <div class="container">
      <div class="section-header">
        <span class="badge-tag">Service Coverage</span>
        <h2>Our Service Locations Across Chennai &amp; Tamil Nadu</h2>
        <p class="section-subtitle">Serving households across 35+ prime Chennai locations and all over Tamil Nadu.</p>
      </div>

      <div class="contact-details-grid">
        <!-- Office & Coverage Details Card -->
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
              <p style="font-size:0.85rem; color:var(--text-light);">Available for consultation &amp; booking</p>
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
              <p style="font-size:0.85rem; color:var(--text-light);">Immediate response on WhatsApp</p>
            </div>
          </div>

          <!-- All Over Tamil Nadu Callout -->
          <div style="background: linear-gradient(135deg, #0F2C59 0%, #163E7D 100%); color: #FFFFFF; border-radius: var(--radius-md); padding: 1.25rem;">
            <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.35rem;">
              <span style="font-size:1.25rem;">🚩</span>
              <strong style="color:#2DD4BF; font-size:1rem;">All Over Tamil Nadu Service</strong>
            </div>
            <p style="color:#E2E8F0; font-size:0.85rem; line-height:1.5; margin-bottom:0;">
              We provide home care services across all districts of Tamil Nadu. For locations outside our primary Chennai areas, service is provided on a <strong>One-Day Full (24-Hour)</strong> basis.
            </p>
          </div>

          <!-- Primary Chennai Localities -->
          <div class="contact-info-item" style="margin-top: 0.5rem;">
            <div class="contact-icon-wrapper">🗺️</div>
            <div class="contact-info-content">
              <h4>Primary Chennai Coverage Areas</h4>
              <div class="service-areas-pills">
                {loc_pills_html}
              </div>
            </div>
          </div>
        </div>

        <!-- Location Map / Office Representation -->
        <div class="contact-info-card" style="padding: 1.5rem; display: flex; flex-direction: column;">
          <h3 style="margin-bottom: 0.5rem; font-size: 1.25rem;">Our Central Office in New Perungalathur</h3>
          <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 1rem;">
            Centrally coordinating care staff across Chennai neighborhoods and outstation Tamil Nadu assignments.
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

    full_path = os.path.join(ROOT_DIR, "index.html")
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(html.strip() + "\n")
    print("Generated: index.html with 11 services and all 37 locations + TN 24hr note")

if __name__ == "__main__":
    generate_home_page()
