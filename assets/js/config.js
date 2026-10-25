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
  email: "care@sugamhomecareservices.in",
  
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
  
  // Primary Service Areas in Chennai
  serviceAreas: [
    "New Perungalathur",
    "Perungalathur",
    "Tambaram",
    "Chromepet",
    "Pallavaram",
    "Vandalur",
    "Guduvanchery",
    "Medavakkam",
    "Velachery",
    "Greater Chennai"
  ],
  
  // 7 Individual Services
  services: [
    {
      id: "maid-services",
      name: "Maid Services",
      slug: "/maid-services/",
      shortDesc: "Reliable household assistance including daily sweeping, mopping, kitchen cleaning, dishwashing, and tidying.",
      icon: "🧹"
    },
    {
      id: "home-health-care-services",
      name: "Home Health Care Services",
      slug: "/home-health-care-services/",
      shortDesc: "Personalized home healthcare support, vitals monitoring, routine health tracking, and post-hospital recovery assistance.",
      icon: "🩺"
    },
    {
      id: "caretaker-services",
      name: "Caretaker Services",
      slug: "/caretaker-services/",
      shortDesc: "Attentive everyday assistance with mobility, feeding, hygiene, medication reminders, and reassuring companionship.",
      icon: "🤝"
    },
    {
      id: "baby-care-taker",
      name: "Baby Care Taker",
      slug: "/baby-care-taker/",
      shortDesc: "Tender, dependable infant care support, feeding assistance, diaper changing, baby massage, and newborn assistance.",
      icon: "👶"
    },
    {
      id: "elderly-care-services",
      name: "Elderly Care Services",
      slug: "/elderly-care-services/",
      shortDesc: "Dignified, compassionate care for seniors, helping with daily routines, mobility, emotional well-being, and companionship.",
      icon: "🧓"
    },
    {
      id: "patient-care-services",
      name: "Patient Care Services",
      slug: "/patient-care-services/",
      shortDesc: "Dedicated bedside support for bedridden or recovering patients, hygiene maintenance, and comfortable home care.",
      icon: "🛏️"
    },
    {
      id: "nursing-services-at-home",
      name: "Nursing Services at Home",
      slug: "/nursing-services-at-home/",
      shortDesc: "Qualified home nursing assistance for clinical procedures, injections, wound dressing, catheter care, and post-op care.",
      icon: "👩‍⚕️"
    }
  ],
  
  // Google Ads Tracking Configuration (Set these when launching your Google Ads campaign)
  googleAds: {
    conversionId: "AW-CONVERSION_ID_PLACEHOLDER",
    conversionLabel: "CONVERSION_LABEL_PLACEHOLDER",
    enabled: false // Set to true once Google Ads IDs are added
  }
};

// Export for Node or browser
if (typeof module !== "undefined" && module.exports) {
  module.exports = SITE_CONFIG;
}
