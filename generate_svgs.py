#!/usr/bin/env python3
import os

images_dir = "/Users/karthik/.gemini/antigravity/scratch/sugam-home-care/assets/images"
os.makedirs(images_dir, exist_ok=True)

svgs = {
    "hero-home.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="100%" height="100%">
  <defs>
    <linearGradient id="heroBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F0FDF4"/>
      <stop offset="50%" stop-color="#F8FAFC"/>
      <stop offset="100%" stop-color="#E2E8F0"/>
    </linearGradient>
    <linearGradient id="primaryGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F2C59"/>
      <stop offset="100%" stop-color="#1E3A8A"/>
    </linearGradient>
    <linearGradient id="tealGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0D9488"/>
      <stop offset="100%" stop-color="#14B8A6"/>
    </linearGradient>
    <filter id="cardShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#0F2C59" flood-opacity="0.12"/>
    </filter>
  </defs>

  <!-- Background Canvas -->
  <rect width="800" height="600" rx="24" fill="url(#heroBg)"/>
  
  <!-- Architectural Home Accents -->
  <circle cx="700" cy="120" r="180" fill="#0D9488" fill-opacity="0.08"/>
  <circle cx="120" cy="500" r="140" fill="#0F2C59" fill-opacity="0.05"/>
  <rect x="520" y="80" width="220" height="320" rx="16" fill="#FFFFFF" fill-opacity="0.6"/>
  <line x1="630" y1="80" x2="630" y2="400" stroke="#CBD5E1" stroke-width="2"/>
  <line x1="520" y1="240" x2="740" y2="240" stroke="#CBD5E1" stroke-width="2"/>

  <!-- Indoor Plants & Cozy Elements -->
  <path d="M120 480 Q100 420 80 400 Q110 410 130 460 Q150 400 170 380 Q160 430 140 480" fill="#10B981" opacity="0.7"/>
  <rect x="100" y="480" width="50" height="60" rx="8" fill="#D97706" opacity="0.8"/>

  <!-- Main Illustration Group: Caregiver and Senior -->
  <g transform="translate(180, 70)">
    <!-- Cozy Living Armchair -->
    <path d="M160 380 C130 380 110 350 110 300 C110 240 130 200 170 200 C200 200 230 200 260 200 C300 200 320 240 320 300 C320 350 300 380 270 380 Z" fill="#E2E8F0"/>
    <rect x="140" y="290" width="150" height="90" rx="16" fill="#CBD5E1"/>

    <!-- Senior Sitting in Comfort -->
    <!-- Head -->
    <circle cx="215" cy="165" r="32" fill="#FBBF24" opacity="0.9"/>
    <!-- Hair (Silver/Grey) -->
    <path d="M190 160 C190 135 240 135 240 160 C235 145 220 142 215 142 C205 142 195 148 190 160 Z" fill="#94A3B8"/>
    <!-- Traditional Indian Kurta / Soft Attire -->
    <path d="M180 200 C180 195 250 195 250 200 L265 310 C265 320 165 320 165 310 Z" fill="#F1F5F9" stroke="#E2E8F0" stroke-width="2"/>
    <path d="M195 200 L215 250 L235 200" stroke="#0D9488" stroke-width="2" fill="none"/>

    <!-- Professional Caregiver Standing with Compassion -->
    <!-- Uniform - Scrub Teal -->
    <!-- Head -->
    <circle cx="340" cy="140" r="30" fill="#F59E0B" opacity="0.9"/>
    <!-- Neat Hair Bun -->
    <circle cx="355" cy="125" r="14" fill="#1E293B"/>
    <path d="M315 135 C315 115 365 115 365 135 C360 125 330 122 315 135 Z" fill="#1E293B"/>
    <!-- Professional Healthcare Scrub / Uniform -->
    <path d="M305 175 C315 170 365 170 375 175 L390 320 C390 330 290 330 290 320 Z" fill="url(#tealGrad)"/>
    <!-- ID Card / Badge -->
    <rect x="345" y="200" width="16" height="24" rx="3" fill="#FFFFFF"/>
    <line x1="353" y1="180" x2="353" y2="200" stroke="#0F2C59" stroke-width="1.5"/>
    <circle cx="353" cy="208" r="3" fill="#0D9488"/>
    <line x1="348" y1="216" x2="358" y2="216" stroke="#94A3B8" stroke-width="2"/>
    
    <!-- Caring Arm Rested Comfortingly -->
    <path d="M310 210 Q280 230 260 250" stroke="#F59E0B" stroke-width="14" stroke-linecap="round" fill="none"/>
    <path d="M310 210 Q280 230 260 250" stroke="url(#tealGrad)" stroke-width="10" stroke-linecap="round" fill="none"/>
    <!-- Hand holding senior's hand gently -->
    <circle cx="260" cy="250" r="10" fill="#F59E0B"/>
  </g>

  <!-- Floating Trust Badge 1: 100% Verified Caregivers -->
  <g transform="translate(60, 160)" filter="url(#cardShadow)">
    <rect width="210" height="75" rx="14" fill="#FFFFFF"/>
    <circle cx="38" cy="38" r="22" fill="#ECFDF5"/>
    <path d="M28 38L35 45L48 30" stroke="#059669" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
    <text x="70" y="32" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" font-weight="700" fill="#0F2C59">Compassionate Care</text>
    <text x="70" y="52" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="500" fill="#64748B">Personalized Support</text>
  </g>

  <!-- Floating Trust Badge 2: In-Home Assistance -->
  <g transform="translate(530, 420)" filter="url(#cardShadow)">
    <rect width="210" height="75" rx="14" fill="#FFFFFF"/>
    <circle cx="38" cy="38" r="22" fill="#EFF6FF"/>
    <path d="M38 26L26 36H30V48H46V36H50L38 26Z" fill="#2563EB"/>
    <text x="70" y="32" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" font-weight="700" fill="#0F2C59">Comfort of Home</text>
    <text x="70" y="52" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="500" fill="#64748B">Family-Centered Care</text>
  </g>
</svg>''',

    "service-maid.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <defs>
    <linearGradient id="maidBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F8FAFC"/>
      <stop offset="100%" stop-color="#E2E8F0"/>
    </linearGradient>
    <linearGradient id="maidAccent" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F2C59"/>
      <stop offset="100%" stop-color="#0D9488"/>
    </linearGradient>
  </defs>
  <rect width="600" height="400" rx="16" fill="url(#maidBg)"/>
  <circle cx="480" cy="100" r="120" fill="#0D9488" fill-opacity="0.1"/>
  
  <!-- Kitchen/Living Counter -->
  <rect x="80" y="260" width="440" height="100" rx="12" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
  <line x1="80" y1="285" x2="520" y2="285" stroke="#E2E8F0" stroke-width="2"/>
  
  <!-- Sparkling Utensils / Tidying Visuals -->
  <circle cx="160" cy="220" r="30" fill="#F1F5F9" stroke="#94A3B8" stroke-width="2"/>
  <rect x="220" y="200" width="40" height="60" rx="6" fill="#0D9488" opacity="0.8"/>
  <circle cx="240" cy="180" r="10" fill="#14B8A6"/>
  
  <!-- Spray Bottle & Sparkles -->
  <path d="M400 190 L420 190 L430 260 L390 260 Z" fill="#0F2C59"/>
  <rect x="395" y="170" width="20" height="20" rx="4" fill="#0D9488"/>
  <path d="M390 170 Q370 160 380 180" stroke="#0D9488" stroke-width="3" fill="none"/>
  
  <!-- Sparkles -->
  <path d="M460 160 L465 175 L480 180 L465 185 L460 200 L455 185 L440 180 L455 175 Z" fill="#F59E0B"/>
  <path d="M320 120 L323 130 L333 133 L323 136 L320 146 L317 136 L307 133 L317 130 Z" fill="#0D9488"/>
  
  <!-- Cleanliness & Household Care Badge -->
  <g transform="translate(180, 60)">
    <rect width="240" height="50" rx="25" fill="#FFFFFF" stroke="#0D9488" stroke-width="1.5"/>
    <circle cx="25" cy="25" r="15" fill="#ECFDF5"/>
    <path d="M19 25L23 29L31 20" stroke="#059669" stroke-width="2.5" stroke-linecap="round" fill="none"/>
    <text x="50" y="31" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700" fill="#0F2C59">Reliable Maid Services</text>
  </g>
</svg>''',

    "service-home-health.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <defs>
    <linearGradient id="hhBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#EFF6FF"/>
      <stop offset="100%" stop-color="#E0E7FF"/>
    </linearGradient>
  </defs>
  <rect width="600" height="400" rx="16" fill="url(#hhBg)"/>
  
  <!-- Stethoscope & Vitals Visual -->
  <circle cx="300" cy="200" r="140" fill="#FFFFFF" fill-opacity="0.8"/>
  
  <!-- Pulse Line (ECG) in circle -->
  <path d="M180 200 L240 200 L255 160 L275 240 L295 180 L310 215 L320 200 L420 200" stroke="#0D9488" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
  
  <!-- Stethoscope Outline -->
  <path d="M220 130 C220 280 380 280 380 130" stroke="#0F2C59" stroke-width="6" stroke-linecap="round" fill="none"/>
  <circle cx="220" cy="130" r="10" fill="#0F2C59"/>
  <circle cx="380" cy="130" r="10" fill="#0F2C59"/>
  <path d="M300 245 L300 300" stroke="#0F2C59" stroke-width="6" fill="none"/>
  <circle cx="300" cy="315" r="22" fill="#0D9488"/>
  <circle cx="300" cy="315" r="10" fill="#FFFFFF"/>
  
  <!-- Medical Cross Badge -->
  <g transform="translate(180, 40)">
    <rect width="240" height="50" rx="25" fill="#FFFFFF" stroke="#0F2C59" stroke-width="1.5"/>
    <circle cx="25" cy="25" r="15" fill="#EEF2FF"/>
    <path d="M25 17V33M17 25H33" stroke="#2563EB" stroke-width="3" stroke-linecap="round"/>
    <text x="50" y="31" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700" fill="#0F2C59">Home Health Care</text>
  </g>
</svg>''',

    "service-caretaker.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <defs>
    <linearGradient id="ctBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F0FDF4"/>
      <stop offset="100%" stop-color="#DCFCE7"/>
    </linearGradient>
  </defs>
  <rect width="600" height="400" rx="16" fill="url(#ctBg)"/>
  
  <!-- Compassionate Caregiver Silhouette & Warm Hands -->
  <g transform="translate(150, 100)">
    <!-- Holding Hands / Support symbol -->
    <circle cx="150" cy="120" r="80" fill="#FFFFFF"/>
    <!-- Hands holding heart -->
    <path d="M150 90 C140 75 120 78 120 95 C120 115 150 135 150 135 C150 135 180 115 180 95 C180 78 160 75 150 90 Z" fill="#EF4444"/>
    <!-- Cradling Hands -->
    <path d="M100 130 C120 160 180 160 200 130" stroke="#0D9488" stroke-width="6" stroke-linecap="round" fill="none"/>
    <path d="M120 150 L100 180 M180 150 L200 180" stroke="#0F2C59" stroke-width="4" stroke-linecap="round"/>
  </g>
  
  <g transform="translate(170, 40)">
    <rect width="260" height="50" rx="25" fill="#FFFFFF" stroke="#0D9488" stroke-width="1.5"/>
    <circle cx="25" cy="25" r="15" fill="#ECFDF5"/>
    <path d="M18 25L23 30L32 19" stroke="#059669" stroke-width="2.5" stroke-linecap="round" fill="none"/>
    <text x="50" y="31" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700" fill="#0F2C59">Attentive Caretaker Support</text>
  </g>
</svg>''',

    "service-baby-care.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bcBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFBEB"/>
      <stop offset="100%" stop-color="#FEF3C7"/>
    </linearGradient>
  </defs>
  <rect width="600" height="400" rx="16" fill="url(#bcBg)"/>
  
  <!-- Baby Crib / Nursery visual -->
  <g transform="translate(180, 110)">
    <circle cx="120" cy="110" r="90" fill="#FFFFFF"/>
    <!-- Gentle Baby Carriage / Cradle -->
    <path d="M60 110 C60 70 110 70 120 110 L180 110 C180 145 150 170 110 170 C70 170 60 145 60 110 Z" fill="#FDE68A" stroke="#D97706" stroke-width="3"/>
    <circle cx="90" cy="170" r="14" fill="#0F2C59"/>
    <circle cx="90" cy="170" r="6" fill="#FFFFFF"/>
    <circle cx="150" cy="170" r="14" fill="#0F2C59"/>
    <circle cx="150" cy="170" r="6" fill="#FFFFFF"/>
    <!-- Handle -->
    <path d="M180 110 L200 80" stroke="#0F2C59" stroke-width="4" stroke-linecap="round"/>
    <!-- Sleeping Baby moon/star -->
    <path d="M90 75 Q95 65 105 70 Q98 75 90 75 Z" fill="#0D9488"/>
  </g>

  <g transform="translate(180, 40)">
    <rect width="240" height="50" rx="25" fill="#FFFFFF" stroke="#D97706" stroke-width="1.5"/>
    <circle cx="25" cy="25" r="15" fill="#FEF3C7"/>
    <circle cx="25" cy="25" r="7" fill="#D97706"/>
    <text x="50" y="31" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700" fill="#0F2C59">Baby Care Taker</text>
  </g>
</svg>''',

    "service-elderly-care.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <defs>
    <linearGradient id="ecBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F8FAFC"/>
      <stop offset="100%" stop-color="#E2E8F0"/>
    </linearGradient>
  </defs>
  <rect width="600" height="400" rx="16" fill="url(#ecBg)"/>
  
  <g transform="translate(170, 90)">
    <!-- Shield of Respect & Senior Care -->
    <circle cx="130" cy="120" r="90" fill="#FFFFFF"/>
    <!-- Walking Cane & Helping Hand -->
    <path d="M100 80 C100 65 125 65 125 80 L125 180" stroke="#0F2C59" stroke-width="6" stroke-linecap="round" fill="none"/>
    <path d="M125 80 C125 90 145 90 145 80" stroke="#0F2C59" stroke-width="6" stroke-linecap="round" fill="none"/>
    <!-- Heart of Compassion -->
    <path d="M160 110 C155 95 135 98 135 115 C135 135 160 155 160 155 C160 155 185 135 185 115 C185 98 165 95 160 110 Z" fill="#0D9488"/>
  </g>

  <g transform="translate(180, 40)">
    <rect width="240" height="50" rx="25" fill="#FFFFFF" stroke="#0F2C59" stroke-width="1.5"/>
    <circle cx="25" cy="25" r="15" fill="#EEF2FF"/>
    <path d="M19 25L23 29L31 20" stroke="#0F2C59" stroke-width="2.5" stroke-linecap="round" fill="none"/>
    <text x="50" y="31" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700" fill="#0F2C59">Elderly Care Services</text>
  </g>
</svg>''',

    "service-patient-care.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <defs>
    <linearGradient id="pcBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#EFF6FF"/>
      <stop offset="100%" stop-color="#DBEAFE"/>
    </linearGradient>
  </defs>
  <rect width="600" height="400" rx="16" fill="url(#pcBg)"/>
  
  <g transform="translate(150, 100)">
    <circle cx="150" cy="110" r="90" fill="#FFFFFF"/>
    <!-- Hospital / Recovery Bed -->
    <rect x="70" y="130" width="160" height="16" rx="4" fill="#0F2C59"/>
    <rect x="70" y="110" width="50" height="20" rx="4" fill="#94A3B8"/>
    <!-- Bed Legs -->
    <line x1="85" y1="146" x2="85" y2="175" stroke="#0F2C59" stroke-width="5" stroke-linecap="round"/>
    <line x1="215" y1="146" x2="215" y2="175" stroke="#0F2C59" stroke-width="5" stroke-linecap="round"/>
    <!-- Medical Heartbeat Screen Above -->
    <rect x="110" y="60" width="80" height="50" rx="8" fill="#1E293B"/>
    <path d="M120 85 L135 85 L142 75 L150 95 L158 85 L180 85" stroke="#10B981" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
  </g>

  <g transform="translate(180, 40)">
    <rect width="240" height="50" rx="25" fill="#FFFFFF" stroke="#2563EB" stroke-width="1.5"/>
    <circle cx="25" cy="25" r="15" fill="#DBEAFE"/>
    <path d="M25 17V33M17 25H33" stroke="#1D4ED8" stroke-width="3" stroke-linecap="round"/>
    <text x="50" y="31" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700" fill="#0F2C59">Patient Care Services</text>
  </g>
</svg>''',

    "service-nursing.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <defs>
    <linearGradient id="nsBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F0FDF4"/>
      <stop offset="100%" stop-color="#CCFBF1"/>
    </linearGradient>
  </defs>
  <rect width="600" height="400" rx="16" fill="url(#nsBg)"/>
  
  <g transform="translate(160, 100)">
    <circle cx="140" cy="110" r="90" fill="#FFFFFF"/>
    <!-- Nursing Cross & Clinical Injection / Care Badge -->
    <circle cx="140" cy="110" r="50" fill="#ECFDF5"/>
    <path d="M140 85V135M115 110H165" stroke="#0D9488" stroke-width="8" stroke-linecap="round"/>
    <!-- Stethoscope arc -->
    <path d="M90 70 C70 120 70 160 120 170" stroke="#0F2C59" stroke-width="4" stroke-linecap="round" fill="none"/>
    <circle cx="90" cy="70" r="6" fill="#0F2C59"/>
  </g>

  <g transform="translate(170, 40)">
    <rect width="260" height="50" rx="25" fill="#FFFFFF" stroke="#0D9488" stroke-width="1.5"/>
    <circle cx="25" cy="25" r="15" fill="#CCFBF1"/>
    <path d="M25 17V33M17 25H33" stroke="#0D9488" stroke-width="3" stroke-linecap="round"/>
    <text x="50" y="31" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700" fill="#0F2C59">Nursing Services at Home</text>
  </g>
</svg>'''
}

for filename, content in svgs.items():
    path = os.path.join(images_dir, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {filename}")

print("All SVGs successfully created!")
