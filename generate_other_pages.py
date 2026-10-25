#!/usr/bin/env python3
import os
from site_templates import get_header, get_footer

ROOT_DIR = "/Users/karthik/.gemini/antigravity/scratch/sugam-home-care"

def write_file(rel_path, content):
    full = os.path.join(ROOT_DIR, rel_path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Generated: {rel_path}")

# ---------------------------------------------------------------------------
# 1. ABOUT US PAGE (/about-us/index.html)
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
  <title>About Us | Sugam Home Care Services Chennai</title>
  <meta name="description" content="Learn about Sugam Home Care Services in Chennai. Our mission, values, and commitment to compassionate, reliable home care, elder care, and patient care.">
  <link rel="canonical" href="https://sugamhomecareservices.in/about-us/">
  <link rel="icon" type="image/svg+xml" href="{rel}assets/images/favicon.svg">
  <link rel="stylesheet" href="{rel}assets/css/style.css">
  <link rel="stylesheet" href="{rel}assets/css/components.css">
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
        <span class="badge-tag">Our Story & Mission</span>
        <h1 style="font-size: clamp(2.2rem, 3.5vw, 3rem); margin-bottom: 1rem;">
          Compassionate Care for Chennai Families in the Comfort of Home
        </h1>
        <p class="lead" style="color: var(--text-muted); font-size: 1.15rem;">
          Sugam Home Care Services was founded with a straightforward purpose: to provide families with dependable, respectful, and compassionate care assistance for their loved ones right at home.
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
          <h3>Dignity & Respect</h3>
          <p>Whether assisting an elderly grandparent, a recovering patient, or an infant, we treat every individual with warmth, honor, and deep respect.</p>
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
          <h3>Safety & Reliability</h3>
          <p>We verify identities, understand previous care background, and ensure caregivers are attentive, clean, and dedicated to their duties.</p>
        </div>

        <div class="benefit-item">
          <div class="benefit-number">05</div>
          <h3>Chennai Rooted</h3>
          <p>Headquartered in New Perungalathur, we understand the specific neighborhood requirements and linguistic preferences across Greater Chennai.</p>
        </div>

        <div class="benefit-item">
          <div class="benefit-number">06</div>
          <h3>Clear Care Boundaries</h3>
          <p>We clearly delineate non-medical domestic and caregiving help from clinical nursing, ensuring patients receive the appropriate level of care safely.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- How We Match Caregivers -->
  <section class="section section-bg-surface">
    <div class="container">
      <div class="section-header">
        <span class="badge-tag">Our Careful Process</span>
        <h2>How We Coordinate Care for Your Loved One</h2>
        <p class="section-subtitle">A thoughtful, personalized approach to matching the right caregiver with your household.</p>
      </div>

      <div class="steps-grid">
        <div class="step-card">
          <div class="step-badge">1</div>
          <h3>Requirement Assessment</h3>
          <p>We listen to your loved one’s daily routine, medical history, mobility needs, and your family’s preferred timings.</p>
        </div>

        <div class="step-card">
          <div class="step-badge">2</div>
          <h3>Caregiver Selection</h3>
          <p>We identify caregivers whose temperament, experience, language skills, and availability align with your home.</p>
        </div>

        <div class="step-card">
          <div class="step-badge">3</div>
          <h3>Household Orientation</h3>
          <p>The caregiver is introduced to your home, daily tasks are reviewed, and comfort between the client and caregiver is established.</p>
        </div>

        <div class="step-card">
          <div class="step-badge">4</div>
          <h3>Continuous Support</h3>
          <p>We remain available to receive your feedback, address scheduling adjustments, and ensure smooth care continuity.</p>
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
# 2. CONTACT US PAGE (/contact-us/index.html)
# ---------------------------------------------------------------------------
def generate_contact_page():
    header = get_header("/contact-us/", depth=1)
    footer = get_footer(depth=1)
    rel = "../"

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contact Us | Sugam Home Care Services Chennai</title>
  <meta name="description" content="Contact Sugam Home Care Services in New Perungalathur, Chennai. Call, WhatsApp, or submit an enquiry for home care, maid, elderly, or nursing services.">
  <link rel="canonical" href="https://sugamhomecareservices.in/contact-us/">
  <link rel="icon" type="image/svg+xml" href="{rel}assets/images/favicon.svg">
  <link rel="stylesheet" href="{rel}assets/css/style.css">
  <link rel="stylesheet" href="{rel}assets/css/components.css">
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
                <a href="mailto:care@sugamhomecareservices.in" data-config="email" style="color:var(--color-secondary); font-weight:600;">
                  care@sugamhomecareservices.in
                </a>
              </p>
            </div>
          </div>

          <div class="contact-info-item">
            <div class="contact-icon-wrapper">🗺️</div>
            <div class="contact-info-content">
              <h4>Chennai Service Coverage</h4>
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

        <!-- Right: Contact Form -->
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
              <label class="form-label">Preferred Contact Time</label>
              <select name="preferredTime" class="form-control form-select">
                <option value="Anytime (As soon as possible)">Anytime (As soon as possible)</option>
                <option value="Morning (9 AM - 12 PM)">Morning (9 AM - 12 PM)</option>
                <option value="Afternoon (12 PM - 4 PM)">Afternoon (12 PM - 4 PM)</option>
                <option value="Evening (4 PM - 8 PM)">Evening (4 PM - 8 PM)</option>
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
# 3. ALL SERVICES DIRECTORY (/services/index.html)
# ---------------------------------------------------------------------------
def generate_services_directory():
    header = get_header("/services/", depth=1)
    footer = get_footer(depth=1)
    rel = "../"

    services_cards = [
        {"name": "Maid Services", "slug": "maid-services", "icon": "🧹", "badge": "Household Assistance", "img": "service-maid.svg", "desc": "Reliable daily sweeping, mopping, kitchen dishwashing, and tidying for a sparkling home."},
        {"name": "Home Health Care Services", "slug": "home-health-care-services", "icon": "🩺", "badge": "Health Monitoring", "img": "service-home-health.svg", "desc": "Structured vitals monitoring (BP, sugar, pulse), medication supervision, and convalescence support."},
        {"name": "Caretaker Services", "slug": "caretaker-services", "icon": "🤝", "badge": "Everyday Living", "img": "service-caretaker.svg", "desc": "Attentive everyday assistance with daily routines, mobility, feeding, hygiene, and companionship."},
        {"name": "Baby Care Taker", "slug": "baby-care-taker", "icon": "👶", "badge": "Mother & Child", "img": "service-baby-care.svg", "desc": "Loving, experienced care for newborns and infants: massage, warm bath, feeding, and resting support for mothers."},
        {"name": "Elderly Care Services", "slug": "elderly-care-services", "icon": "🧓", "badge": "Senior Well-Being", "img": "service-elderly-care.svg", "desc": "Dignified, warm care empowering senior parents with fall prevention, mobility, hygiene, and companionship."},
        {"name": "Patient Care Services", "slug": "patient-care-services", "icon": "🛏️", "badge": "Bedside Recovery", "img": "service-patient-care.svg", "desc": "Attentive bedside support for bedridden or post-surgical recovery, bedsore prevention, and hygiene."},
        {"name": "Nursing Services at Home", "slug": "nursing-services-at-home", "icon": "👩‍⚕️", "badge": "Clinical Procedures", "img": "service-nursing.svg", "desc": "Qualified home nursing for prescribed injections, sterile wound dressing, IV fluids, and catheter care."}
    ]

    cards_html = ""
    for s in services_cards:
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
        </article>
        '''

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>All Home Care Services | Sugam Home Care Services Chennai</title>
  <meta name="description" content="Explore all home care services provided by Sugam Home Care Services in Chennai: Maid, Home Health Care, Caretaker, Baby Care, Elderly Care, Patient Care, and Nursing.">
  <link rel="canonical" href="https://sugamhomecareservices.in/services/">
  <link rel="icon" type="image/svg+xml" href="{rel}assets/images/favicon.svg">
  <link rel="stylesheet" href="{rel}assets/css/style.css">
  <link rel="stylesheet" href="{rel}assets/css/components.css">
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
          Our Home Care Services in Chennai
        </h1>
        <p class="lead" style="color: var(--text-muted); font-size: 1.15rem;">
          From daily household chores to clinical nursing at your bedside, discover dedicated care tailored to every stage of family life.
        </p>
      </div>
    </div>
  </section>

  <!-- Service Cards Grid -->
  <section class="section">
    <div class="container">
      <div class="services-grid">
        {cards_html}
      </div>
    </div>
  </section>

  <!-- How to Choose the Right Service -->
  <section class="section section-bg-surface">
    <div class="container">
      <div class="section-header">
        <span class="badge-tag">Service Selection Guide</span>
        <h2>Which Service Fits Your Family's Needs?</h2>
        <p class="section-subtitle">A quick comparison to help you choose the right level of support.</p>
      </div>

      <div class="highlights-grid">
        <div class="highlight-box">
          <div class="highlight-icon">🧹</div>
          <h3>Household Help</h3>
          <p><strong>Maid Services:</strong> Best when you need hands for daily floor cleaning, kitchen dishes, and organizing without personal care duties.</p>
        </div>

        <div class="highlight-box teal-accent">
          <div class="highlight-icon">🤝</div>
          <h3>Personal Caregiving</h3>
          <p><strong>Caretaker / Elderly Care:</strong> Best for elders or recovering family members needing daily physical mobility, feeding, hygiene, and companionship.</p>
        </div>

        <div class="highlight-box amber-accent">
          <div class="highlight-icon">👩‍⚕️</div>
          <h3>Clinical Nursing</h3>
          <p><strong>Nursing Services at Home:</strong> Best when a doctor has prescribed specific medical procedures such as injections, IV fluids, or sterile wound dressings.</p>
        </div>
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
# 4. PRIVACY POLICY PAGE (/privacy-policy/index.html)
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
  <title>Privacy Policy | Sugam Home Care Services</title>
  <meta name="description" content="Privacy Policy for Sugam Home Care Services. Explaining how we collect, use, and protect your personal contact information.">
  <link rel="canonical" href="https://sugamhomecareservices.in/privacy-policy/">
  <link rel="icon" type="image/svg+xml" href="{rel}assets/images/favicon.svg">
  <link rel="stylesheet" href="{rel}assets/css/style.css">
  <link rel="stylesheet" href="{rel}assets/css/components.css">
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
        <span class="badge-tag">Legal & Data Protection</span>
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
          <li>Service required (e.g. Maid Services, Elderly Care, Nursing at Home)</li>
          <li>Preferred contact timings and specific care requirements</li>
          <li>Locality or address in Chennai for assessing service availability</li>
          <li>Standard web analytics data (such as IP address, browser type, and Google Ads referral parameters).</li>
        </ul>

        <h3 style="color: var(--color-primary); margin-top: 2rem;">3. How We Use Your Information</h3>
        <p>The information you submit is used solely for the following legitimate business purposes:</p>
        <ul style="list-style: disc; padding-left: 1.5rem; margin-bottom: 1rem; color: var(--text-muted);">
          <li>To respond to your service enquiry and arrange telephone consultations.</li>
          <li>To coordinate care requirements and assess staff availability in your Chennai locality.</li>
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
          Email: <span data-config="email">care@sugamhomecareservices.in</span><br>
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
# 5. TERMS AND CONDITIONS (/terms-and-conditions/index.html)
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
  <title>Terms and Conditions | Sugam Home Care Services</title>
  <meta name="description" content="Terms and Conditions governing the use of Sugam Home Care Services website and home care coordination services.">
  <link rel="canonical" href="https://sugamhomecareservices.in/terms-and-conditions/">
  <link rel="icon" type="image/svg+xml" href="{rel}assets/images/favicon.svg">
  <link rel="stylesheet" href="{rel}assets/css/style.css">
  <link rel="stylesheet" href="{rel}assets/css/components.css">
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
        <p>Sugam Home Care Services coordinates home-based assistance including maid services, caretaker support, baby care, elderly care, patient care, and qualified home nursing. Submitting an enquiry via website, phone, or WhatsApp does not constitute a guaranteed binding contract until service terms, hours, charges, and caregiver availability are mutually confirmed.</p>

        <h3 style="color: var(--color-primary); margin-top: 2rem;">3. Clinical Nursing & Prescription Requirement</h3>
        <p>Clinical procedures (including injections, IV fluids, wound dressing, and catheterization) require a valid, signed prescription from a registered medical practitioner. Sugam Home Care Services does not provide independent medical diagnosis or prescribe pharmaceutical drugs.</p>

        <h3 style="color: var(--color-primary); margin-top: 2rem;">4. Emergency Medical Disclaimer</h3>
        <p>Sugam Home Care Services is <strong>not an emergency medical service</strong>. In the event of acute respiratory distress, cardiac symptoms, severe trauma, or life-threatening emergencies, clients must contact 108 or proceed immediately to the nearest emergency hospital.</p>

        <h3 style="color: var(--color-primary); margin-top: 2rem;">5. Safe & Respectful Working Environment</h3>
        <p>Clients are expected to maintain a safe, hygienic, and respectful working environment for caregivers. Any form of harassment or unsafe conditions will result in immediate termination of service.</p>

        <h3 style="color: var(--color-primary); margin-top: 2rem;">6. Governing Law & Jurisdiction</h3>
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
# 6. THANK YOU / CONVERSION PAGE (/thank-you/index.html)
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
  <title>Thank You | Sugam Home Care Services</title>
  <meta name="description" content="Thank you for contacting Sugam Home Care Services. Our care coordinator will call you back shortly.">
  <meta name="robots" content="noindex, follow">
  <link rel="canonical" href="https://sugamhomecareservices.in/thank-you/">
  <link rel="icon" type="image/svg+xml" href="{rel}assets/images/favicon.svg">
  <link rel="stylesheet" href="{rel}assets/css/style.css">
  <link rel="stylesheet" href="{rel}assets/css/components.css">

  <!-- Google Ads Conversion Tracking Snippet (Triggered on Thank You) -->
  <script>
    window.addEventListener('DOMContentLoaded', () => {{
      // Retrieve lead info from sessionStorage if available
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
      <!-- Success Icon -->
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
        We have received your home care enquiry. Our care coordinator will review your requirements and call you back during our regular consultation hours.
      </p>

      <div id="lead-summary-notice" style="display: none; background-color: var(--bg-surface); border: 1px solid var(--border-light); padding: 0.85rem 1.25rem; border-radius: var(--radius-md); font-size: 0.9rem; color: var(--color-primary); margin: 0 auto 2rem auto; max-width: 500px;"></div>

      <!-- What happens next box -->
      <div style="background-color: var(--bg-warm); border-radius: var(--radius-lg); border: 1px solid var(--border-light); padding: 2rem; max-width: 650px; margin: 0 auto 2.5rem auto; text-align: left;">
        <h3 style="font-size: 1.2rem; color: var(--color-primary); margin-bottom: 1rem;">What Happens Next?</h3>
        <div style="display: flex; flex-direction: column; gap: 0.85rem;">
          <div style="display: flex; gap: 0.75rem; align-items: flex-start;">
            <span style="background-color: var(--color-primary); color: #FFF; width: 24px; height: 24px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.75rem; font-weight: 700; flex-shrink: 0;">1</span>
            <span style="font-size: 0.95rem; color: var(--text-main);"><strong>Requirement Review:</strong> Our care team reviews your requested service, shift hours, and Chennai locality.</span>
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
        "https://sugamhomecareservices.in/maid-services/",
        "https://sugamhomecareservices.in/home-health-care-services/",
        "https://sugamhomecareservices.in/caretaker-services/",
        "https://sugamhomecareservices.in/baby-care-taker/",
        "https://sugamhomecareservices.in/elderly-care-services/",
        "https://sugamhomecareservices.in/patient-care-services/",
        "https://sugamhomecareservices.in/nursing-services-at-home/",
        "https://sugamhomecareservices.in/privacy-policy/",
        "https://sugamhomecareservices.in/terms-and-conditions/"
    ]
    
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        priority = "1.0" if u.endswith(".in/") else ("0.9" if "services/" in u or u.endswith("-services/") or "baby-care" in u or "nursing" in u else "0.8")
        sitemap.append(f'  <url>\n    <loc>{u}</loc>\n    <lastmod>2026-10-22</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>{priority}</priority>\n  </url>')
    sitemap.append('</urlset>')

    write_file("sitemap.xml", "\n".join(sitemap))

    robots = '''User-agent: *
Allow: /
Disallow: /thank-you/

Sitemap: https://sugamhomecareservices.in/sitemap.xml
'''
    write_file("robots.txt", robots)

# Run all generators
generate_about_page()
generate_contact_page()
generate_services_directory()
generate_privacy_page()
generate_terms_page()
generate_thank_you_page()
generate_sitemap_and_robots()

print("All additional pages, sitemap, and robots.txt built successfully!")
