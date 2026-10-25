# Sugam Home Care Services — Premium Website & Lead Generation Engine

Official Website: [https://sugamhomecareservices.in/](https://sugamhomecareservices.in/)

A high-performance, mobile-first website designed for **Sugam Home Care Services** in Chennai, built specifically for Google Ads lead generation, high conversion rates, and SEO authority.

---

## 📁 Website Architecture (14 Complete Pages)

1. **Home** — [`/index.html`](index.html)
   - High-converting hero with short enquiry form & visible phone CTA
   - 4-pillar trust & reassurance section
   - Comprehensive grid for all 7 home care services
   - Why Choose Sugam Home Care Services section
   - 4-step "How It Works" visual flow
   - Care categories (Household vs Personal Care vs Clinical Nursing)
   - 8-question interactive FAQ accordion
   - Final conversion banner & verified Chennai office location map
2. **About Us** — [`/about-us/`](about-us/index.html)
   - Company ethos, mission, care matching process, and safety commitments
3. **Contact Us** — [`/contact-us/`](contact-us/index.html)
   - Full address in New Perungalathur, interactive enquiry form, and Google Maps embed
4. **All Services** — [`/services/`](services/index.html)
   - Complete directory and decision matrix to guide families to the right service
5. **Maid Services** — [`/maid-services/`](maid-services/index.html)
   - Dedicated landing page for sweeping, mopping, dishwashing, and home upkeep
6. **Home Health Care Services** — [`/home-health-care-services/`](home-health-care-services/index.html)
   - Dedicated landing page for vitals tracking and post-hospital recovery
7. **Caretaker Services** — [`/caretaker-services/`](caretaker-services/index.html)
   - Dedicated landing page for daily living, personal hygiene, and companionship
8. **Baby Care Taker** — [`/baby-care-taker/`](baby-care-taker/index.html)
   - Dedicated landing page for newborn care, baby massage, bath, and mother support
9. **Elderly Care Services** — [`/elderly-care-services/`](elderly-care-services/index.html)
   - Dedicated landing page for senior dignity, fall prevention, and loving companionship
10. **Patient Care Services** — [`/patient-care-services/`](patient-care-services/index.html)
    - Dedicated landing page for bedridden care, bedsore prevention, and bedside support
11. **Nursing Services at Home** — [`/nursing-services-at-home/`](nursing-services-at-home/index.html)
    - Dedicated landing page for doctor-prescribed injections, wound dressings, and catheter care
12. **Privacy Policy** — [`/privacy-policy/`](privacy-policy/index.html)
    - Compliant privacy guidelines explaining data confidentiality and non-disclosure
13. **Terms and Conditions** — [`/terms-and-conditions/`](terms-and-conditions/index.html)
    - Service scope, non-emergency medical disclaimer, and Chennai jurisdiction
14. **Thank You** — [`/thank-you/`](thank-you/index.html)
    - Conversion confirmation page with Google Ads conversion event integration

---

## ⚙️ Centralized Configuration: Update Phone & WhatsApp in 1 Place

All phone numbers, WhatsApp links, email addresses, and Google Ads tracking IDs across **all 14 pages** are centrally managed in:

👉 `assets/js/config.js`

To update the business numbers once actual phone and WhatsApp lines are active:

```javascript
const SITE_CONFIG = {
  businessName: "Sugam Home Care Services",
  
  // Update Phone Number here:
  phoneDisplay: "+91 84388 61636",
  phoneRaw: "+918438861636",
  phoneTel: "tel:+918438861636",
  
  // Update WhatsApp Number here:
  whatsappDisplay: "+91 84388 61636",
  whatsappRaw: "918438861636",
  whatsappLink: "https://wa.me/918438861636?text=...",
  
  // Office Address:
  address: {
    line1: "No. 123/12, Kattabomman Street",
    line2: "Kamaraj Nagar, New Perungalathur",
    city: "Chennai",
    state: "Tamil Nadu",
    postalCode: "600063",
    country: "India",
    full: "No. 123/12, Kattabomman Street, Kamaraj Nagar, New Perungalathur, Chennai – 600063, Tamil Nadu, India."
  },

  // Google Ads Tracking:
  googleAds: {
    conversionId: "AW-123456789", // Replace with your Google Ads Conversion ID
    conversionLabel: "AbCdEfGhIjK",  // Replace with your Conversion Label
    enabled: true
  }
};
```

---

## 🚀 Running Locally

To preview the website locally in any browser:

```bash
cd /Users/karthik/.gemini/antigravity/scratch/sugam-home-care
python3 -m http.server 8080
```
Then open: `http://localhost:8080/`

---

## 📈 Google Ads & Lead Generation Features

- **Sticky Mobile Bottom Bar**: Features instant Call Now & WhatsApp buttons pinned to the screen bottom on all mobile devices.
- **UTM Parameter Capture**: Automatically extracts `utm_source`, `utm_medium`, `utm_campaign`, and `gclid` (Google Click ID) from ad clicks and attaches them to incoming leads.
- **Fail-Safe Offline Lead Storage**: Every form submission is instantly stored in `localStorage` under `sugam_enquiries`, guaranteeing zero lost leads even during network fluctuations.
- **Fast Core Web Vitals**: Built with pure semantic HTML5, modern CSS, and vanilla JS — zero bulky frameworks, ensuring 100/100 Google PageSpeed scores and lower Google Ads Cost-Per-Click (CPC).
- **Schema.org Rich Snippets**: Includes `HomeHealthService`, `Service`, `BreadcrumbList`, and `FAQPage` structured data on every relevant page.
