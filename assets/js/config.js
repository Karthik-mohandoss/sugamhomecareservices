/**
 * Sugam Home Care Services - Central Site Configuration
 * 
 * To update contact details (phone, WhatsApp, email, address, or Google Ads IDs)
 * simply edit this file. All pages automatically reflect these values dynamically.
 */
const SITE_CONFIG = {
  businessName: "Sugam Home Care Services",
  tagline: "Compassionate Home Care Services for Your Loved Ones",
  websiteUrl: "https://sugamhomecareservices.in",
  
  // Contact Numbers
  phoneDisplay: "+91 84388 61636",
  phoneRaw: "+918438861636",
  phoneTel: "tel:+918438861636",
  
  // WhatsApp Configuration
  whatsappDisplay: "+91 84388 61636",
  whatsappRaw: "918438861636",
  whatsappLink: "https://wa.me/918438861636?text=Hello%20Sugam%20Home%20Care%20Services,%20I%20would%20like%20to%20enquire%20about%20home%20care%20services.",
  
  // Email
  email: "sugamhomecare35@gmail.com",
  enquiryEmail: "sugamhomecare35@gmail.com",
  enquiryRecipients: ["sugamhomecare35@gmail.com", "akrithmarketer@gmail.com"],
  
  // Office Address (Chennai)
  address: {
    line1: "No. 123/12, Kattabomman Street",
    line2: "Kamaraj Nagar, New Perungalathur",
    city: "Chennai",
    state: "Tamil Nadu",
    postalCode: "600063",
    country: "India",
    full: "No. 123/12, Kattabomman Street, Kamaraj Nagar, New Perungalathur, Chennai – 600063, Tamil Nadu, India."
  },
  
  // Primary Service Locations
  serviceAreas: [
    "Tambaram",
    "Vandalur",
    "Guduvanchery",
    "Sholinganallur",
    "Navalur",
    "OMR",
    "ECR",
    "Adyar",
    "Velachery",
    "Nanganallur",
    "Madipakkam",
    "Pallavaram",
    "Chromepet",
    "Alandur",
    "Guindy",
    "Adambakkam",
    "Taramani",
    "Nungambakkam",
    "Kodambakkam",
    "Chetpet",
    "Egmore",
    "Thousand Lights",
    "Royapettah",
    "Anna Nagar",
    "Mogappair",
    "Ambattur",
    "Avadi",
    "Porur",
    "Iyyappanthangal",
    "Ayanavaram",
    "Royapuram",
    "Purasawalkam",
    "Panaiyur",
    "Thoraipakkam",
    "Perungudi",
    "T. Nagar",
    "Ashok Nagar"
  ],

  // All Over Tamil Nadu Service Policy
  allTamilNaduPolicy: {
    coverage: "All Over Tamil Nadu",
    terms: "Service available across Tamil Nadu. For locations outside our primary Chennai coverage, service is provided on a One-Day Full (24-Hour) basis."
  },
  
  // Exactly 11 Approved Services
  services: [
    {
      id: "baby-care-services",
      name: "Baby care services",
      slug: "/baby-care-services/",
      shortDesc: "Tender infant care, newborn massage, warm bath assistance, bottle feeding, and restful recovery support for new mothers.",
      icon: "👶"
    },
    {
      id: "elderly-care-services",
      name: "Elderly care services",
      slug: "/elderly-care-services/",
      shortDesc: "Dignified, warm senior care supporting daily routines, walking assistance, fall prevention, personal hygiene, and loving companionship.",
      icon: "🧓"
    },
    {
      id: "patient-care-services",
      name: "Patient care services",
      slug: "/patient-care-services/",
      shortDesc: "Dedicated bedside support for recovering patients, mobility assistance, sponge bathing, feeding, and personal hygiene upkeep at home.",
      icon: "🛏️"
    },
    {
      id: "senior-citizen-care-services",
      name: "Senior citizen care services",
      slug: "/senior-citizen-care-services/",
      shortDesc: "Comprehensive senior citizen support promoting healthy daily routines, medication reminders, meal assistance, and empathetic presence.",
      icon: "👴"
    },
    {
      id: "bedridden-patient-care-services",
      name: "Bedridden patient care services",
      slug: "/bedridden-patient-care-services/",
      shortDesc: "Specialized bed care: 2-hour body repositioning, bedsore prevention, bed bathing, adult diaper hygiene, and gentle feeding.",
      icon: "🛌"
    },
    {
      id: "home-health-care-for-seniors",
      name: "Home health care for seniors",
      slug: "/home-health-care-for-seniors/",
      shortDesc: "Structured health monitoring for elders: blood pressure, sugar, pulse tracking, medication adherence, and doctor coordination.",
      icon: "🩺"
    },
    {
      id: "dementia-care-for-the-elderly",
      name: "Dementia care for the elderly",
      slug: "/dementia-care-for-the-elderly/",
      shortDesc: "Specialized cognitive support, calm daily routines, reassurance, and continuous safety oversight for seniors with Alzheimer's and memory loss.",
      icon: "🧠"
    },
    {
      id: "home-care-for-cancer-patients",
      name: "Home care for cancer patients",
      slug: "/home-care-for-cancer-patients/",
      shortDesc: "Compassionate oncology support: post-chemotherapy recovery assistance, comfort positioning, nutrition tracking, and palliative care.",
      icon: "🎗️"
    },
    {
      id: "caretaker-services-at-home",
      name: "Caretaker services at home",
      slug: "/caretaker-services-at-home/",
      shortDesc: "Attentive everyday assistance with bathing, dressing, meal feeding, medication reminders, and comforting companion care.",
      icon: "🤝"
    },
    {
      id: "home-nurse-services",
      name: "Home nurse services",
      slug: "/home-nurse-services/",
      shortDesc: "Qualified visiting or shift-based nurses for clinical procedures, injections, wound dressings, IV therapy, and recovery supervision.",
      icon: "👩‍⚕️"
    },
    {
      id: "nursing-services",
      name: "Nursing Services",
      slug: "/nursing-services/",
      shortDesc: "Clinical nursing at home under medical prescription: sterile dressing, IV line care, catheterization, Ryle's tube, and post-op care.",
      icon: "💉"
    }
  ],
  
  // Google Ads Tracking Configuration
  googleAds: {
    conversionId: "AW-18536226621",
    callConversionLabel: "OU2_CJjguKodEL2-4YZF",
    phoneForwardingLabel: "p8H3CJXguKodEL2-4YZF",
    phoneConversionNumber: "84388 61636",
    enabled: true
  }
};

// Export for Node or browser
if (typeof module !== "undefined" && module.exports) {
  module.exports = SITE_CONFIG;
}
