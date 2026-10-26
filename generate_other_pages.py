#!/usr/bin/env python3
import os
from site_templates import get_header, get_footer, GOOGLE_ADS_HEAD

ROOT_DIR = "/Users/karthik/.gemini/antigravity/scratch/sugam-home-care"

LOCATIONS = [
    "Tambaram", "Vandalur", "Guduvanchery", "Sholinganallur", "Navalur", "OMR", "ECR", 
    "Adyar", "Velachery", "Nanganallur", "Madipakkam", "Pallavaram", "Chromepet", 
    "Alandur", "Guindy", "Adambakkam", "Taramani", "Nungambakkam", "Kodambakkam", 
    "Chetpet", "Egmore", "Thousand Lights", "Royapettah", "Anna Nagar", "Mogappair", 
    "Ambattur", "Avadi", "Porur", "Iyyappanthangal", "Ayanavaram", "Royapuram", 
    "Purasawalkam", "Panaiyur", "Thoraipakkam", "Perungudi", "T. Nagar", "Ashok Nagar"
]

SERVICES_DIRECTORY = [
    {"name": "Baby care services", "slug": "baby-care-services", "icon": "👶", "badge": "Infant & Mother", "img": "service-baby-care.svg", "desc": "Tender infant care, newborn massage, warm bath, bottle feeding, and restful recovery support for mothers."},
    {"name": "Elderly care services", "slug": "elderly-care-services", "icon": "🧓", "badge": "Senior Well-Being", "img": "service-elderly-care.svg", "desc": "Dignified senior care supporting mobility, fall prevention, personal hygiene, and loving companionship."},
    {"name": "Patient care services", "slug": "patient-care-services", "icon": "🛏️", "badge": "Bedside Recovery", "img": "service-patient-care.svg", "desc": "Attentive bedside support for recovering patients, mobility assistance, sponge bathing, and feeding."},
    {"name": "Senior citizen care services", "slug": "senior-citizen-care-services", "icon": "👴", "badge": "Senior Assistance", "img": "service-senior-citizen.svg", "desc": "Active daily living support, walking assistance, nutritious meal help, and empathetic presence."},
    {"name": "Bedridden patient care services", "slug": "bedridden-patient-care-services", "icon": "🛌", "badge": "Intensive Bedside", "img": "service-bedridden.svg", "desc": "Specialized bed care: 2-hour body repositioning, bedsore prevention, bed bathing, and diaper hygiene."},
    {"name": "Home health care for seniors", "slug": "home-health-care-for-seniors", "icon": "🩺", "badge": "Health Monitoring", "img": "service-home-health.svg", "desc": "Structured vitals monitoring (BP, sugar, pulse), medication schedule oversight, and geriatric wellness."},
    {"name": "Dementia care for the elderly", "slug": "dementia-care-for-the-elderly", "icon": "🧠", "badge": "Specialized Memory", "img": "service-dementia.svg", "desc": "Specialized memory support, wandering safety, reassuring routines, and calm patience for Alzheimer's patients."},
    {"name": "Home care for cancer patients", "slug": "home-care-for-cancer-patients", "icon": "🎗️", "badge": "Supportive Oncology", "img": "service-cancer-care.svg", "desc": "Post-chemotherapy recovery, comfort positioning, nutrition tracking, and palliative home companionship."},
    {"name": "Caretaker services at home", "slug": "caretaker-services-at-home", "icon": "🤝", "badge": "Everyday Living", "img": "service-caretaker.svg", "desc": "Everyday assistance with personal grooming, mobility, feeding, medication reminders, and companionship."},
    {"name": "Home nurse services", "slug": "home-nurse-services", "icon": "👩‍⚕️", "badge": "Home Nursing", "img": "service-home-nurse.svg", "desc": "Qualified visiting or shift-based nurses for clinical procedures, injections, wound care, and recovery."},
    {"name": "Nursing Services", "slug": "nursing-services", "icon": "💉", "badge": "Clinical Procedures", "img": "service-nursing.svg", "desc": "Clinical nursing at home under medical prescription: IV infusions, sterile wound dressings, and catheter care."}
]

def write_file(rel_path, content):
    full = os.path.join(ROOT_DIR, rel_path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Generated: {rel_path}")

# ---------------------------------------------------------------------------
# 1. ABOUT US PAGE
# ---------------------------------------------------------------------------
def generate_about_page():
    header = get_header("/about-us/", depth=1)
    footer = get_footer(depth=1)
    rel = "../"
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
{GOOGLE_ADS_HEAD}
  <title>About Us | Sugam Home Care Services Chennai &amp; Tamil Nadu</title>
  <meta name="description" content="Learn about Sugam Home Care Services. Our mission, values, and commitment to compassionate, reliable home care, senior care, bedridden care, and nursing across Chennai and Tamil Nadu.">
  <link rel="canonical" href="https://sugamhomecareservices.in/about-us/">
  <link rel="icon" type="image/svg+xml" href="{rel}assets/images/favicon.svg">
  <link rel="stylesheet" href="{rel}assets/css/style.css?v=5">
  <link rel="stylesheet" href="{rel}assets/css/components.css?v=5">
</head>
<body>

{header}

<main>
  <!-- Hero Section -->
  <section class="service-hero-section">
    <div class="container">
      <nav class="breadcrumbs" aria-label="Breadcrumbs">
        <a href="{rel}">Home</a>
        <span class="breadcrumbs-separator">/</span>
        <span>About Us</span>
      </nav>

      <div class="section-header text-left" style="max-width: 800px; margin-bottom: 1.5rem;">
        <span class="badge-tag">Our Story &amp; Mission</span>
        <h1 style="font-size: clamp(2.2rem, 3.5vw, 3rem); margin-bottom: 1rem;">
          Compassionate Care for Families Across Chennai &amp; Tamil Nadu
        </h1>
        <p class="lead" style="color: var(--text-muted); font-size: 1.15rem;">
          Sugam Home Care Services was founded with a straightforward purpose: to provide families with dependable, respectful, and compassionate care assistance for elderly parents, recovering patients, and infants in the comfort of home.
        </p>
      </div>
    </div>
  </section>

  <!-- Core Values & Philosophy -->
  <section class="section">
    <div class="container">
      <div class="section-header">
        <span class="badge-tag">Guiding Principles</span>
        <h2>What Drives Sugam Home Care Services</h2>
        <p class="section-subtitle">We believe true caregiving goes beyond physical tasks — it is about dignity, patience, and mutual respect.</p>
      </div>

      <div class="benefits-grid">
        <div class="benefit-item">
          <div class="benefit-number">01</div>
          <h3>Dignity &amp; Respect</h3>
          <p>Whether assisting an elderly grandparent, a bedridden patient, or a newborn baby, we treat every individual with warmth, honor, and deep respect.</p>
        </div>

        <div class="benefit-item">
          <div class="benefit-number">02</div>
          <h3>Honest Communication</h3>
          <p>We believe in transparent discussions regarding what our caregivers can do, shift timings, charges, and expectations without overpromising.</p>
        </div>

        <div class="benefit-item">
          <div class="benefit-number">03</div>
          <h3>Family-Centered Approach</h3>
          <p>We work collaboratively with children, spouses, and family elders, respecting household traditions, dietary choices, and routines.</p>
        </div>

        <div class="benefit-item">
          <div class="benefit-number">04</div>
          <h3>Safety &amp; Reliability</h3>
          <p>We verify identities, understand previous care background, and ensure caregivers are attentive, clean, and dedicated to their duties.</p>
        </div>

        <div class="benefit-item">
          <div class="benefit-number">05</div>
          <h3>Chennai &amp; Tamil Nadu Reach</h3>
          <p>Headquartered in New Perungalathur, serving 35+ Chennai localities and providing 24-Hour full-day care across all districts of Tamil Nadu.</p>
        </div>

        <div class="benefit-item">
          <div class="benefit-number">06</div>
          <h3>Clear Care Boundaries</h3>
          <p>We clearly delineate non-medical caregiving help from clinical nursing, ensuring patients receive the appropriate level of medical oversight safely.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Final CTA -->
  <section class="final-cta-section">
    <div class="container final-cta-box">
      <span class="badge-tag" style="background-color: rgba(255,255,255,0.15); color: #2DD4BF;">Talk with Us</span>
      <h2>Have Questions About Our Home Care Team?</h2>
      <p>Our care coordinator is available to answer your questions and help you explore the best options for your family.</p>
      <div class="final-cta-buttons">
        <a href="tel:+918438861636" data-config="phoneTel" class="btn btn-white btn-lg">Call Us Directly</a>
        <a href="https://wa.me/918438861636" data-config="whatsappLink" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp btn-lg">Chat on WhatsApp</a>
        <a href="{rel}contact-us/" class="btn btn-secondary btn-lg">Visit Contact Page</a>
      </div>
    </div>
  </section>
</main>

{footer}

</body>
</html>'''

    write_file("about-us/index.html", html)

# ---------------------------------------------------------------------------
# 2. CONTACT US PAGE
# ---------------------------------------------------------------------------
def generate_contact_page():
    header = get_header("/contact-us/", depth=1)
    footer = get_footer(depth=1)
    rel = "../"

    loc_pills = ""
    for loc in LOCATIONS:
        loc_pills += f'<span class="area-pill">{loc}</span>\n                '

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
{GOOGLE_ADS_HEAD}
  <title>Contact Us | Sugam Home Care Services Chennai &amp; Tamil Nadu</title>
  <meta name="description" content="Contact Sugam Home Care Services. Call +91 84388 61636 or WhatsApp for home care, senior care, bedridden patient care, and nursing across Chennai and Tamil Nadu.">
  <link rel="canonical" href="https://sugamhomecareservices.in/contact-us/">
  <link rel="icon" type="image/svg+xml" href="{rel}assets/images/favicon.svg">
  <link rel="stylesheet" href="{rel}assets/css/style.css?v=5">
  <link rel="stylesheet" href="{rel}assets/css/components.css?v=5">
</head>
<body>

{header}

<main>
  <section class="service-hero-section">
    <div class="container">
      <nav class="breadcrumbs" aria-label="Breadcrumbs">
        <a href="{rel}">Home</a>
        <span class="breadcrumbs-separator">/</span>
        <span>Contact Us</span>
      </nav>

      <div class="section-header text-left" style="max-width: 800px; margin-bottom: 1.5rem;">
        <span class="badge-tag">Get in Touch</span>
        <h1 style="font-size: clamp(2.2rem, 3.5vw, 3rem); margin-bottom: 1rem;">
          Contact Sugam Home Care Services
        </h1>
        <p class="lead" style="color: var(--text-muted); font-size: 1.15rem;">
          We are here to assist you with reliable, compassionate care for your loved ones. Call, message on WhatsApp, or send an enquiry form below.
        </p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="contact-details-grid">
        <!-- Left: Full Contact Information & Address -->
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
              <h4>Phone Number</h4>
              <p>
                <a href="tel:+918438861636" data-config="phoneTel" style="color:var(--color-primary); font-weight:700; font-size:1.1rem;">
                  <span data-config="phoneDisplay">+91 84388 61636</span>
                </a>
              </p>
              <p style="font-size:0.85rem; color:var(--text-light);">Tap to call our care coordinator directly</p>
            </div>
          </div>

          <div class="contact-info-item">
            <div class="contact-icon-wrapper">💬</div>
            <div class="contact-info-content">
              <h4>WhatsApp Quick Chat</h4>
              <p>
                <a href="https://wa.me/918438861636" data-config="whatsappLink" target="_blank" rel="noopener noreferrer" style="color:var(--color-whatsapp-dark); font-weight:700; font-size:1.05rem;">
                  Chat with Our Care Team on WhatsApp
                </a>
              </p>
              <p style="font-size:0.85rem; color:var(--text-light);">Fastest way to get answers to your questions</p>
            </div>
          </div>

          <div class="contact-info-item">
            <div class="contact-icon-wrapper">✉️</div>
            <div class="contact-info-content">
              <h4>Email Enquiries</h4>
              <p>
                <a href="mailto:sugamhomecare35@gmail.com" data-config="email" style="color:var(--color-secondary); font-weight:600;">
                  sugamhomecare35@gmail.com
                </a>
              </p>
            </div>
          </div>

          <!-- All Over Tamil Nadu Notice -->
          <div style="background: linear-gradient(135deg, #0F2C59 0%, #163E7D 100%); color: #FFFFFF; border-radius: var(--radius-md); padding: 1.25rem;">
            <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.35rem;">
              <span style="font-size:1.25rem;">🚩</span>
              <strong style="color:#2DD4BF; font-size:1rem;">All Over Tamil Nadu Service Availability:</strong>
            </div>
            <p style="color:#E2E8F0; font-size:0.85rem; line-height:1.5; margin-bottom:0;">
              Outside our primary Chennai locations, home care services across Tamil Nadu are provided on a <strong>One-Day Full (24-Hour)</strong> basis.
            </p>
          </div>

          <div class="contact-info-item" style="margin-top: 0.5rem;">
            <div class="contact-icon-wrapper">🗺️</div>
            <div class="contact-info-content">
              <h4>Primary Chennai Coverage Areas</h4>
              <div class="service-areas-pills">
                {loc_pills}
              </div>
            </div>
          </div>
        </div>

        <!-- Right: Contact Form (11 Services) -->
        <div class="enquiry-card">
          <div class="enquiry-card-header">
            <span class="badge-tag">Direct Enquiry</span>
            <h2 class="enquiry-card-title">Send Us a Message</h2>
            <p class="enquiry-card-subtitle">Fill out the details below and we will get back to you promptly.</p>
          </div>

          <form class="lead-form" action="{rel}thank-you/" method="GET">
            <div class="form-group">
              <label class="form-label">Full Name <span class="required">*</span></label>
              <input type="text" name="fullName" class="form-control" placeholder="Enter your full name" required>
            </div>

            <div class="form-group">
              <label class="form-label">Phone Number <span class="required">*</span></label>
              <input type="tel" name="phone" class="form-control" placeholder="e.g. 8438861636" required>
            </div>

            <div class="form-group">
              <label class="form-label">Service Required <span class="required">*</span></label>
              <select name="service" class="form-control form-select" required>
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
              <input type="checkbox" id="contact-consent" name="consent" required checked>
              <label for="contact-consent">I agree to be contacted by Sugam Home Care Services regarding this enquiry.</label>
            </div>

            <button type="submit" class="btn-submit-lead">
              Submit Enquiry
            </button>
          </form>
        </div>
      </div>
    </div>
  </section>

  <!-- Interactive Map Section -->
  <section class="section section-bg-surface" style="padding-top: 2rem;">
    <div class="container">
      <div class="section-header">
        <span class="badge-tag">Find Us</span>
        <h2>Our Office Location in Chennai</h2>
        <p class="section-subtitle">No. 123/12, Kattabomman Street, Kamaraj Nagar, New Perungalathur, Chennai – 600063.</p>
      </div>
      <div style="width: 100%; height: 380px; border-radius: var(--radius-xl); overflow: hidden; border: 1px solid var(--border-light); box-shadow: var(--shadow-sm);">
        <iframe 
          title="Sugam Home Care Services Google Map"
          src="https://maps.google.com/maps?q=Kattabomman%20Street%2C%20New%20Perungalathur%2C%20Chennai%20600063&t=&z=14&ie=UTF8&iwloc=&output=embed" 
          width="100%" 
          height="100%" 
          style="border:0;" 
          allowfullscreen="" 
          loading="lazy">
        </iframe>
      </div>
    </div>
  </section>
</main>

{footer}

</body>
</html>'''

    write_file("contact-us/index.html", html)

# ---------------------------------------------------------------------------
# 3. ALL SERVICES DIRECTORY (11 Services)
# ---------------------------------------------------------------------------
def generate_services_directory():
    header = get_header("/services/", depth=1)
    footer = get_footer(depth=1)
    rel = "../"

    cards_html = ""
    for s in SERVICES_DIRECTORY:
        cards_html += f'''
        <article class="service-card">
          <div class="service-card-media">
            <img src="{rel}assets/images/{s["img"]}" alt="{s["name"]}" class="service-card-img" width="600" height="400" loading="lazy">
            <span class="service-card-badge">{s["badge"]}</span>
          </div>
          <div class="service-card-body">
            <div class="service-card-header">
              <span class="service-card-icon">{s["icon"]}</span>
              <h3 class="service-card-title"><a href="{rel}{s["slug"]}/">{s["name"]}</a></h3>
            </div>
            <p class="service-card-text">{s["desc"]}</p>
            <div class="service-card-actions">
              <a href="{rel}{s["slug"]}/" class="btn btn-outline-primary">View Details</a>
              <button type="button" class="btn btn-primary btn-open-modal" data-service="{s["name"]}">Enquire</button>
            </div>
          </div>
        </article>'''

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
{GOOGLE_ADS_HEAD}
  <title>All Home Care Services | Sugam Home Care Services Chennai &amp; Tamil Nadu</title>
  <meta name="description" content="Explore all 11 home care services provided by Sugam Home Care Services: Baby Care, Elderly Care, Patient Care, Senior Citizen Care, Bedridden Care, Dementia Care, Cancer Care, and Nursing.">
  <link rel="canonical" href="https://sugamhomecareservices.in/services/">
  <link rel="icon" type="image/svg+xml" href="{rel}assets/images/favicon.svg">
  <link rel="stylesheet" href="{rel}assets/css/style.css?v=5">
  <link rel="stylesheet" href="{rel}assets/css/components.css?v=5">
</head>
<body>

{header}

<main>
  <section class="service-hero-section">
    <div class="container">
      <nav class="breadcrumbs" aria-label="Breadcrumbs">
        <a href="{rel}">Home</a>
        <span class="breadcrumbs-separator">/</span>
        <span>Services</span>
      </nav>

      <div class="section-header text-left" style="max-width: 800px; margin-bottom: 1.5rem;">
        <span class="badge-tag">Comprehensive Care Directory</span>
        <h1 style="font-size: clamp(2.2rem, 3.5vw, 3rem); margin-bottom: 1rem;">
          Our 11 Home Care Services
        </h1>
        <p class="lead" style="color: var(--text-muted); font-size: 1.15rem;">
          Specialized, compassionate care across Chennai and all over Tamil Nadu. Designed for senior citizens, bedridden individuals, cancer recovery, dementia support, and clinical nursing.
        </p>
      </div>
    </div>
  </section>

  <!-- Service Cards Grid (11 Services) -->
  <section class="section">
    <div class="container">
      <div class="services-grid">
        {cards_html}
      </div>
    </div>
  </section>

  <!-- Final CTA -->
  <section class="final-cta-section">
    <div class="container final-cta-box">
      <span class="badge-tag" style="background-color: rgba(255,255,255,0.15); color: #2DD4BF;">Need Guidance?</span>
      <h2>Unsure Which Service You Need?</h2>
      <p>Talk with our care coordinator. We will review your family member’s needs and recommend the ideal care plan.</p>
      <div class="final-cta-buttons">
        <a href="tel:+918438861636" data-config="phoneTel" class="btn btn-white btn-lg">Call Us Now</a>
        <a href="https://wa.me/918438861636" data-config="whatsappLink" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp btn-lg">Chat on WhatsApp</a>
        <button type="button" class="btn btn-secondary btn-lg btn-open-modal">Request a Call Back</button>
      </div>
    </div>
  </section>
</main>

{footer}

</body>
</html>'''

    write_file("services/index.html", html)

# ---------------------------------------------------------------------------
# 4. PRIVACY POLICY PAGE
# ---------------------------------------------------------------------------
def generate_privacy_page():
    header = get_header("/privacy-policy/", depth=1)
    footer = get_footer(depth=1)
    rel = "../"

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
{GOOGLE_ADS_HEAD}
  <title>Privacy Policy | Sugam Home Care Services</title>
  <meta name="description" content="Privacy Policy for Sugam Home Care Services. Explaining how we collect, use, and protect your personal contact information.">
  <link rel="canonical" href="https://sugamhomecareservices.in/privacy-policy/">
  <link rel="icon" type="image/svg+xml" href="{rel}assets/images/favicon.svg">
  <link rel="stylesheet" href="{rel}assets/css/style.css?v=5">
  <link rel="stylesheet" href="{rel}assets/css/components.css?v=5">
</head>
<body>

{header}

<main>
  <section class="service-hero-section">
    <div class="container">
      <nav class="breadcrumbs" aria-label="Breadcrumbs">
        <a href="{rel}">Home</a>
        <span class="breadcrumbs-separator">/</span>
        <span>Privacy Policy</span>
      </nav>
      <div class="section-header text-left" style="max-width: 800px; margin-bottom: 0;">
        <span class="badge-tag">Legal &amp; Data Protection</span>
        <h1>Privacy Policy</h1>
        <p class="section-subtitle">Last Updated: October 2026</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container-narrow">
      <div style="background-color: #FFFFFF; border-radius: var(--radius-lg); padding: 2.5rem; border: 1px solid var(--border-light); line-height: 1.8;">
        <h3 style="color: var(--color-primary); margin-top: 1rem;">1. Introduction</h3>
        <p>Sugam Home Care Services ("we", "our", or "us"), located at No. 123/12, Kattabomman Street, Kamaraj Nagar, New Perungalathur, Chennai – 600063, Tamil Nadu, India, respects your privacy. This Privacy Policy outlines how we collect, handle, and safeguard your personal information when you visit our website (https://sugamhomecareservices.in/) or contact us regarding home care services.</p>

        <h3 style="color: var(--color-primary); margin-top: 2rem;">2. Information We Collect</h3>
        <p>When you enquire through our website forms, phone, or WhatsApp, we may collect:</p>
        <ul style="list-style: disc; padding-left: 1.5rem; margin-bottom: 1rem; color: var(--text-muted);">
          <li>Full Name</li>
          <li>Phone Number and WhatsApp contact details</li>
          <li>Service required (e.g. Elderly Care, Patient Care, Bedridden Care, Nursing Services)</li>
          <li>Preferred contact timings and specific care requirements</li>
          <li>Locality in Chennai or district in Tamil Nadu for assessing staff availability</li>
          <li>Standard web analytics data (such as IP address, browser type, and Google Ads referral parameters).</li>
        </ul>

        <h3 style="color: var(--color-primary); margin-top: 2rem;">3. How We Use Your Information</h3>
        <p>The information you submit is used solely for the following legitimate business purposes:</p>
        <ul style="list-style: disc; padding-left: 1.5rem; margin-bottom: 1rem; color: var(--text-muted);">
          <li>To respond to your service enquiry and arrange telephone consultations.</li>
          <li>To coordinate care requirements and assess staff availability in your locality.</li>
          <li>To follow up on requested service arrangements and maintain service records.</li>
          <li>We <strong>do not sell, rent, or trade</strong> your personal contact details to any third-party marketing companies.</li>
        </ul>

        <h3 style="color: var(--color-primary); margin-top: 2rem;">4. Data Security</h3>
        <p>We implement appropriate technical and administrative safeguards to protect your personal contact details from unauthorized access, loss, or misuse.</p>

        <h3 style="color: var(--color-primary); margin-top: 2rem;">5. Contact Us Regarding Privacy</h3>
        <p>If you have any questions or wish to request the deletion of your enquiry data, please contact us at:</p>
        <p style="color: var(--text-main); font-weight: 600;">
          Sugam Home Care Services<br>
          No. 123/12, Kattabomman Street, Kamaraj Nagar, New Perungalathur, Chennai – 600063, Tamil Nadu, India.<br>
          Email: <span data-config="email">sugamhomecare35@gmail.com</span><br>
          Phone: <span data-config="phoneDisplay">+91 84388 61636</span>
        </p>
      </div>
    </div>
  </section>
</main>

{footer}

</body>
</html>'''

    write_file("privacy-policy/index.html", html)

# ---------------------------------------------------------------------------
# 5. TERMS AND CONDITIONS PAGE
# ---------------------------------------------------------------------------
def generate_terms_page():
    header = get_header("/terms-and-conditions/", depth=1)
    footer = get_footer(depth=1)
    rel = "../"

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
{GOOGLE_ADS_HEAD}
  <title>Terms and Conditions | Sugam Home Care Services</title>
  <meta name="description" content="Terms and Conditions governing the use of Sugam Home Care Services website and home care coordination services.">
  <link rel="canonical" href="https://sugamhomecareservices.in/terms-and-conditions/">
  <link rel="icon" type="image/svg+xml" href="{rel}assets/images/favicon.svg">
  <link rel="stylesheet" href="{rel}assets/css/style.css?v=5">
  <link rel="stylesheet" href="{rel}assets/css/components.css?v=5">
</head>
<body>

{header}

<main>
  <section class="service-hero-section">
    <div class="container">
      <nav class="breadcrumbs" aria-label="Breadcrumbs">
        <a href="{rel}">Home</a>
        <span class="breadcrumbs-separator">/</span>
        <span>Terms and Conditions</span>
      </nav>
      <div class="section-header text-left" style="max-width: 800px; margin-bottom: 0;">
        <span class="badge-tag">Service Agreement</span>
        <h1>Terms and Conditions</h1>
        <p class="section-subtitle">Last Updated: October 2026</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container-narrow">
      <div style="background-color: #FFFFFF; border-radius: var(--radius-lg); padding: 2.5rem; border: 1px solid var(--border-light); line-height: 1.8;">
        <h3 style="color: var(--color-primary); margin-top: 1rem;">1. Agreement to Terms</h3>
        <p>By using the website of Sugam Home Care Services (https://sugamhomecareservices.in/) or engaging our home care coordination services, you agree to comply with and be bound by these Terms and Conditions.</p>

        <h3 style="color: var(--color-primary); margin-top: 2rem;">2. Scope of Services</h3>
        <p>Sugam Home Care Services coordinates home-based assistance including baby care, elderly care, patient care, senior citizen support, bedridden care, dementia care, cancer home care, and qualified nursing. Submitting an enquiry does not constitute a guaranteed binding contract until service terms, hours, charges, and caregiver availability are mutually confirmed.</p>

        <h3 style="color: var(--color-primary); margin-top: 2rem;">3. Service Locations Policy</h3>
        <p>Primary services are available across 35+ designated localities in Chennai on part-time, 12-hour, or 24-hour shifts. Outside primary Chennai coverage areas across Tamil Nadu, services are provided exclusively on a One-Day Full (24-Hour) basis.</p>

        <h3 style="color: var(--color-primary); margin-top: 2rem;">4. Clinical Nursing &amp; Prescription Requirement</h3>
        <p>Clinical procedures (including injections, IV fluids, wound dressing, and catheterization) require a valid, signed prescription from a registered medical practitioner. Sugam Home Care Services does not provide independent medical diagnosis or prescribe pharmaceutical drugs.</p>

        <h3 style="color: var(--color-primary); margin-top: 2rem;">5. Emergency Medical Disclaimer</h3>
        <p>Sugam Home Care Services is <strong>not an emergency medical service</strong>. In the event of acute respiratory distress, cardiac symptoms, severe trauma, or life-threatening emergencies, clients must contact 108 or proceed immediately to the nearest emergency hospital.</p>

        <h3 style="color: var(--color-primary); margin-top: 2rem;">6. Governing Law &amp; Jurisdiction</h3>
        <p>These Terms shall be governed by and construed in accordance with the laws of India, and any disputes shall be subject to the exclusive jurisdiction of the competent courts in Chennai, Tamil Nadu.</p>
      </div>
    </div>
  </section>
</main>

{footer}

</body>
</html>'''

    write_file("terms-and-conditions/index.html", html)

# ---------------------------------------------------------------------------
# 6. THANK YOU PAGE
# ---------------------------------------------------------------------------
def generate_thank_you_page():
    header = get_header("/thank-you/", depth=1)
    footer = get_footer(depth=1)
    rel = "../"

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
{GOOGLE_ADS_HEAD}
  <!-- Event snippet for Submit lead form conversion page -->
  <script>
    gtag('event', 'conversion', {{
        'send_to': 'AW-18536226621/A80wCLajtqodEL2-4YZF',
        'value': 1.0,
        'currency': 'INR'
    }});
  </script>
  <title>Thank You | Sugam Home Care Services</title>
  <meta name="description" content="Thank you for contacting Sugam Home Care Services. Our care coordinator will call you back shortly.">
  <meta name="robots" content="noindex, follow">
  <link rel="canonical" href="https://sugamhomecareservices.in/thank-you/">
  <link rel="icon" type="image/svg+xml" href="{rel}assets/images/favicon.svg">
  <link rel="stylesheet" href="{rel}assets/css/style.css?v=5">
  <link rel="stylesheet" href="{rel}assets/css/components.css?v=5">

  <script>
    window.addEventListener('DOMContentLoaded', () => {{
      try {{
        const lead = JSON.parse(sessionStorage.getItem('sugam_latest_lead'));
        if (lead) {{
          const leadNotice = document.getElementById('lead-summary-notice');
          if (leadNotice) {{
            leadNotice.innerHTML = `<strong>Enquiry Details:</strong> Name: <em>${{lead.fullName}}</em> | Service: <em>${{lead.service}}</em>`;
            leadNotice.style.display = 'block';
          }}
        }}
      }} catch (e) {{}}
    }});
  </script>
</head>
<body>

{header}

<main>
  <section class="section" style="padding: 5rem 0; min-height: 70vh; display: flex; align-items: center;">
    <div class="container-narrow" style="text-align: center;">
      <div style="width: 80px; height: 80px; border-radius: 50%; background-color: #ECFDF5; color: #059669; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem auto; box-shadow: 0 4px 14px rgba(5, 150, 105, 0.2);">
        <svg style="width: 44px; height: 44px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="20 6 9 17 4 12"></polyline>
        </svg>
      </div>

      <span class="badge-tag" style="background-color: #ECFDF5; color: #059669; margin-bottom: 1rem;">Enquiry Successfully Received</span>
      <h1 style="font-size: clamp(2rem, 3.5vw, 2.75rem); color: var(--color-primary); margin-bottom: 1rem;">
        Thank You for Reaching Out to Sugam Home Care Services!
      </h1>
      
      <p style="font-size: 1.15rem; color: var(--text-muted); line-height: 1.6; max-width: 600px; margin: 0 auto 1.5rem auto;">
        We have received your home care enquiry. Our care coordinator will review your requirements and call you back during our consultation hours.
      </p>

      <div id="lead-summary-notice" style="display: none; background-color: var(--bg-surface); border: 1px solid var(--border-light); padding: 0.85rem 1.25rem; border-radius: var(--radius-md); font-size: 0.9rem; color: var(--color-primary); margin: 0 auto 2rem auto; max-width: 500px;"></div>

      <!-- What happens next box -->
      <div style="background-color: var(--bg-warm); border-radius: var(--radius-lg); border: 1px solid var(--border-light); padding: 2rem; max-width: 650px; margin: 0 auto 2.5rem auto; text-align: left;">
        <h3 style="font-size: 1.2rem; color: var(--color-primary); margin-bottom: 1rem;">What Happens Next?</h3>
        <div style="display: flex; flex-direction: column; gap: 0.85rem;">
          <div style="display: flex; gap: 0.75rem; align-items: flex-start;">
            <span style="background-color: var(--color-primary); color: #FFF; width: 24px; height: 24px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.75rem; font-weight: 700; flex-shrink: 0;">1</span>
            <span style="font-size: 0.95rem; color: var(--text-main);"><strong>Requirement Review:</strong> Our care team reviews your requested service, shift hours, and locality.</span>
          </div>
          <div style="display: flex; gap: 0.75rem; align-items: flex-start;">
            <span style="background-color: var(--color-primary); color: #FFF; width: 24px; height: 24px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.75rem; font-weight: 700; flex-shrink: 0;">2</span>
            <span style="font-size: 0.95rem; color: var(--text-main);"><strong>Direct Phone Call:</strong> A coordinator will call you to discuss specific care requirements, charges, and schedule.</span>
          </div>
          <div style="display: flex; gap: 0.75rem; align-items: flex-start;">
            <span style="background-color: var(--color-primary); color: #FFF; width: 24px; height: 24px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.75rem; font-weight: 700; flex-shrink: 0;">3</span>
            <span style="font-size: 0.95rem; color: var(--text-main);"><strong>Confirmation:</strong> Once you are satisfied with the care plan and terms, service commences.</span>
          </div>
        </div>
      </div>

      <!-- Immediate Actions -->
      <p style="font-size: 0.95rem; color: var(--text-muted); margin-bottom: 1rem;">Need an immediate update or have an urgent query?</p>
      <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
        <a href="tel:+918438861636" data-config="phoneTel" class="btn btn-primary btn-lg">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"></path></svg>
          Call Us Now
        </a>
        <a href="https://wa.me/918438861636" data-config="whatsappLink" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp btn-lg">
          <svg class="icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0012.04 2zm5.79 14.07c-.24.67-1.39 1.29-1.93 1.37-.5.08-1.12.11-3.56-.88-3.09-1.28-5.06-4.42-5.21-4.63-.16-.2-1.24-1.66-1.24-3.16 0-1.51.78-2.25 1.06-2.55.28-.3.61-.38.81-.38.2 0 .41 0 .59.01.19.01.44-.07.69.52.25.6.86 2.1.94 2.25.08.16.14.34.03.55-.11.21-.16.34-.32.53-.16.19-.34.42-.48.56-.16.16-.33.33-.14.65.19.32.84 1.38 1.8 2.24 1.24 1.11 2.28 1.45 2.61 1.61.32.16.51.14.7-.08.19-.22.82-.95 1.04-1.28.22-.32.44-.27.75-.16.3.11 1.93.91 2.26 1.08.33.16.55.25.63.39.08.13.08.77-.16 1.44z"></path></svg>
          WhatsApp Us
        </a>
        <a href="{rel}" class="btn btn-outline-primary btn-lg">Return to Homepage</a>
      </div>
    </div>
  </section>
</main>

{footer}

</body>
</html>'''

    write_file("thank-you/index.html", html)

# ---------------------------------------------------------------------------
# 7. SITEMAP.XML & ROBOTS.TXT
# ---------------------------------------------------------------------------
def generate_sitemap_and_robots():
    urls = [
        "https://sugamhomecareservices.in/",
        "https://sugamhomecareservices.in/about-us/",
        "https://sugamhomecareservices.in/contact-us/",
        "https://sugamhomecareservices.in/services/",
        "https://sugamhomecareservices.in/baby-care-services/",
        "https://sugamhomecareservices.in/elderly-care-services/",
        "https://sugamhomecareservices.in/patient-care-services/",
        "https://sugamhomecareservices.in/senior-citizen-care-services/",
        "https://sugamhomecareservices.in/bedridden-patient-care-services/",
        "https://sugamhomecareservices.in/home-health-care-for-seniors/",
        "https://sugamhomecareservices.in/dementia-care-for-the-elderly/",
        "https://sugamhomecareservices.in/home-care-for-cancer-patients/",
        "https://sugamhomecareservices.in/caretaker-services-at-home/",
        "https://sugamhomecareservices.in/home-nurse-services/",
        "https://sugamhomecareservices.in/nursing-services/",
        "https://sugamhomecareservices.in/privacy-policy/",
        "https://sugamhomecareservices.in/terms-and-conditions/"
    ]
    
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        priority = "1.0" if u.endswith(".in/") else ("0.9" if "services" in u or "care" in u or "nurse" in u else "0.8")
        sitemap.append(f'  <url>\n    <loc>{u}</loc>\n    <lastmod>2026-10-26</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>{priority}</priority>\n  </url>')
    sitemap.append('</urlset>')

    write_file("sitemap.xml", "\n".join(sitemap))

    robots = '''User-agent: *
Allow: /
Disallow: /thank-you/

Sitemap: https://sugamhomecareservices.in/sitemap.xml
'''
    write_file("robots.txt", robots)

if __name__ == "__main__":
    generate_about_page()
    generate_contact_page()
    generate_services_directory()
    generate_privacy_page()
    generate_terms_page()
    generate_thank_you_page()
    generate_sitemap_and_robots()
    print("All other pages generated successfully!")
