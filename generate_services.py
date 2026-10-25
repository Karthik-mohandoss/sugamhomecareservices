#!/usr/bin/env python3
import os
from site_templates import get_header, get_footer

ROOT_DIR = "/Users/karthik/.gemini/antigravity/scratch/sugam-home-care"

# Service Definitions
SERVICES = [
    {
        "id": "maid-services",
        "folder": "maid-services",
        "title": "Reliable Maid Services for Your Home in Chennai",
        "meta_title": "Reliable Maid Services in Chennai | Sugam Home Care Services",
        "meta_desc": "Looking for dependable maid services in Chennai? Sugam Home Care provides trusted household help for sweeping, mopping, kitchen cleaning, dishwashing, and tidying.",
        "headline": "Reliable Maid Services for Your Home",
        "tagline": "Keep your home clean, organized, and stress-free with reliable everyday household assistance.",
        "icon": "🧹",
        "image": "assets/images/service-maid.svg",
        "badge": "Household Assistance",
        "who_benefits": [
            {"title": "Dual-Income Working Couples", "desc": "Free up valuable evening and weekend time by having daily sweeping, mopping, and kitchen upkeep handled reliably."},
            {"title": "Busy Families with Young Children", "desc": "Keep floors, play areas, and kitchen countertops hygienically sanitized for toddlers and active kids."},
            {"title": "Senior Citizens Living at Home", "desc": "Remove the physical strain of heavy sweeping, bending, mopping, and utensil cleaning for elderly parents."},
            {"title": "Individuals Recovering from Illness", "desc": "Maintain a spotless, dust-free home environment while you rest and regain your strength."}
        ],
        "scope": [
            {"title": "Daily Sweeping & Wet Mopping", "desc": "Thorough dust removal and wet mopping of all living areas, bedrooms, and balconies with disinfectants."},
            {"title": "Kitchen Slab & Stove Cleaning", "desc": "Wiping down kitchen countertops, grease removal from cooking surfaces, and sink hygiene maintenance."},
            {"title": "Utensil Washing & Dish Drying", "desc": "Scrubbing, washing, rinsing, and organizing daily cookware, plates, and dining utensils."},
            {"title": "Dusting & Surface Tidying", "desc": "Regular wiping of dining tables, center tables, accessible shelves, and keeping rooms organized."},
            {"title": "Laundry & Clothes Care", "desc": "Assistance with machine washing, drying clothes on lines, and folding clean dry clothes."},
            {"title": "Waste Disposal & Bin Sanitization", "desc": "Daily clearance of kitchen and bathroom dustbins into designated collection zones."}
        ],
        "why_us": [
            {"title": "Respectful & Honest Approach", "desc": "We understand that welcoming someone into your home requires utmost trust and respect for household privacy."},
            {"title": "Predictable Daily Routines", "desc": "Establish a consistent morning or evening timing that fits seamlessly into your family's schedule."},
            {"title": "Customized Task Lists", "desc": "Agree on exact daily and weekly chores upfront so expectations are crystal clear on both sides."}
        ],
        "faqs": [
            {"q": "What tasks are included in standard daily maid services?", "a": "Standard tasks typically include floor sweeping, wet mopping, kitchen slab wipe-down, utensil washing, and basic household tidying. Additional chores like laundry folding or balcony cleaning can be coordinated based on agreed hours."},
            {"q": "Are maid services available for morning or evening timings?", "a": "Yes, we coordinate maid services according to your family's preferred time slots — typically morning visits (7 AM to 11 AM) or afternoon/evening visits (3 PM to 7 PM)."},
            {"q": "Which areas in Chennai do you provide maid services?", "a": "We primarily serve New Perungalathur, Perungalathur, Tambaram, Chromepet, Pallavaram, Vandalur, Guduvanchery, Medavakkam, and neighboring South Chennai localities."},
            {"q": "How are monthly charges calculated?", "a": "Charges are based on the size of your home (e.g. 2 BHK, 3 BHK), the specific chores requested, and the daily time duration. Contact us for a transparent, no-obligation quote."},
            {"q": "What should we do if our maid is on leave?", "a": "Please notify our care coordinator. Where possible and depending on availability, we assist in coordinating alternative support for extended leaves."}
        ],
        "related": ["caretaker-services", "home-health-care-services", "elderly-care-services"]
    },
    {
        "id": "home-health-care-services",
        "folder": "home-health-care-services",
        "title": "Comprehensive Home Health Care Services in Chennai",
        "meta_title": "Home Health Care Services Chennai | Sugam Home Care Services",
        "meta_desc": "Personalized home health care services in Chennai. Routine vitals monitoring, medication supervision, and convalescence support in the comfort of home.",
        "headline": "Comprehensive Home Health Care Services",
        "tagline": "Personalized health support, vitals monitoring, and recovery assistance in the comfort of your home.",
        "icon": "🩺",
        "image": "assets/images/service-home-health.svg",
        "badge": "Health Monitoring & Recovery",
        "who_benefits": [
            {"title": "Patients Recently Discharged from Hospital", "desc": "Smooth transition from hospital to home with structured daily health monitoring and recovery support."},
            {"title": "Individuals with Chronic Conditions", "desc": "Consistent tracking of blood pressure, blood glucose, and medication schedules for hypertension or diabetes."},
            {"title": "Seniors Needing Health Supervision", "desc": "Routine health oversight ensuring elders adhere to doctor recommendations and maintain steady wellness."},
            {"title": "Families Seeking Peace of Mind", "desc": "Continuous monitoring and family communication so working children know their parents are well cared for."}
        ],
        "scope": [
            {"title": "Vital Signs Monitoring", "desc": "Regular recording of blood pressure, pulse, oxygen saturation (SpO2), body temperature, and blood glucose levels."},
            {"title": "Medication Schedule Supervision", "desc": "Ensuring doctor-prescribed medications are taken at the right doses and correct times with meals."},
            {"title": "Post-Discharge Recovery Care", "desc": "Assisting patients with resting routines, hydration, mobility precautions, and recuperation steps."},
            {"title": "Dietary & Hydration Tracking", "desc": "Monitoring patient fluid intake and supporting nutritious, doctor-recommended meal schedules."},
            {"title": "Caregiver Coordination with Family", "desc": "Maintaining daily health logs and communicating vital observations with family members."},
            {"title": "Comfort & Mobility Assistance", "desc": "Assisting with gentle movement, postural comfort, and encouraging prescribed physiotherapy exercises."}
        ],
        "why_us": [
            {"title": "Healing in Familiar Surroundings", "desc": "Clinical studies show patients recover faster and with lower anxiety when recuperating at home with family."},
            {"title": "Structured Daily Health Routines", "desc": "Eliminate the confusion of complex medication charts with disciplined, attentive home health coordination."},
            {"title": "Clear Distinction of Care Levels", "desc": "We clearly outline non-clinical health monitoring and coordinate qualified clinical nurses when medical procedures are prescribed."}
        ],
        "faqs": [
            {"q": "What is the difference between home health care and home nursing?", "a": "Home health care focuses on routine health supervision, vitals tracking, medication reminders, and general convalescence support. Home nursing specifically involves clinical procedures (such as injections, IV drips, wound dressings, and catheterization) performed by qualified nurses."},
            {"q": "Can your staff coordinate with our family doctor?", "a": "Yes, our team follows the discharge instructions and health guidelines provided by your attending physician or hospital team."},
            {"q": "How frequently are vital signs recorded?", "a": "Depending on the patient's condition, vitals can be recorded once or twice daily, or before and after medication schedules as recommended."},
            {"q": "What shifts are available for home health care?", "a": "We offer flexible arrangements including 12-hour day shifts, 12-hour night shifts, or continuous 24-hour home health assistance."},
            {"q": "How quickly can home health care support begin?", "a": "We recommend contacting us 24 to 48 hours prior to hospital discharge so we can review requirements and arrange suitable support."}
        ],
        "related": ["patient-care-services", "nursing-services-at-home", "elderly-care-services"]
    },
    {
        "id": "caretaker-services",
        "folder": "caretaker-services",
        "title": "Compassionate Caretaker Services in Chennai",
        "meta_title": "Compassionate Caretaker Services Chennai | Sugam Home Care",
        "meta_desc": "Dedicated caretaker services in Chennai for daily living assistance, personal grooming, mobility, feeding, and reassuring companionship at home.",
        "headline": "Compassionate Caretaker Services for Your Loved Ones",
        "tagline": "Attentive assistance with everyday living, personal grooming, mobility, and companionship.",
        "icon": "🤝",
        "image": "assets/images/service-caretaker.svg",
        "badge": "Everyday Living Support",
        "who_benefits": [
            {"title": "Senior Citizens Needing Daily Help", "desc": "Gentle assistance with morning routines, bathing, dressing, and walking safely around the house."},
            {"title": "Adults with Mobility Restrictions", "desc": "Dependable support for individuals recovering from fractures, joint surgeries, or chronic stiffness."},
            {"title": "Individuals Needing Daytime Companionship", "desc": "Preventing isolation and loneliness with warm conversation, shared activities, and attentive presence."},
            {"title": "Families Balancing Work & Caregiving", "desc": "Reliable support ensuring your loved one is safe, fed, and comfortable while you are at work."}
        ],
        "scope": [
            {"title": "Personal Grooming & Bathing Support", "desc": "Respectful, safe assistance with morning baths, hair combing, oral hygiene, and dressing."},
            {"title": "Mobility & Walking Assistance", "desc": "Supporting safe walking, chair-to-bed transfers, and helping prevent accidental trips and falls."},
            {"title": "Meal Preparation Support & Feeding", "desc": "Serving warm meals on time, assisting with feeding where required, and encouraging hydration."},
            {"title": "Medication Reminders", "desc": "Prompting loved ones to take prescribed medicines on time according to the family doctor's schedule."},
            {"title": "Companionship & Emotional Comfort", "desc": "Active listening, conversation, reading newspapers, and accompanying on gentle evening strolls."},
            {"title": "Living Space Tidiness", "desc": "Keeping the loved one's immediate room, bedsheets, and personal items neat, clean, and organized."}
        ],
        "why_us": [
            {"title": "Empathy & Dignity First", "desc": "We train our caretakers to treat every individual with the warmth, patience, and respect they deserve."},
            {"title": "Flexible Shift Arrangements", "desc": "Choose between daytime care, nighttime vigilance, or comprehensive 24-hour live-in caretaker support."},
            {"title": "Language & Cultural Comfort", "desc": "Caregivers who understand local Tamil customs, dietary habits, and respectful communication."}
        ],
        "faqs": [
            {"q": "Can caretakers administer injections or dress surgical wounds?", "a": "No. Caretakers provide non-clinical personal care and mobility assistance. For clinical procedures like injections, IV fluids, or wound dressings, please enquire for our Nursing Services at Home."},
            {"q": "What shift options are available?", "a": "We provide 10 to 12-hour daytime assistance, 12-hour night care, and 24-hour round-the-clock live-in arrangements."},
            {"q": "How do you match a caretaker to our family?", "a": "We assess your family member's age, physical mobility, gender preference, language comfort, and required daily duties to suggest the most suitable match."},
            {"q": "Can caretakers accompany loved ones to doctor appointments?", "a": "Yes, caretakers can accompany family members to hospital check-ups, diagnostic labs, or neighborhood walks when agreed upon."},
            {"q": "How do we get started?", "a": "Simply call our team or submit the enquiry form. We will discuss your exact requirements and explain available options."}
        ],
        "related": ["elderly-care-services", "patient-care-services", "maid-services"]
    },
    {
        "id": "baby-care-taker",
        "folder": "baby-care-taker",
        "title": "Gentle & Trustworthy Baby Care Taker Services in Chennai",
        "meta_title": "Baby Care Taker in Chennai | Newborn & Infant Care | Sugam Home Care",
        "meta_desc": "Loving, dependable baby care taker services in Chennai. Newborn massage, gentle bathing, bottle feeding assistance, diaper changing, and mother support.",
        "headline": "Gentle & Trustworthy Baby Care Taker Services",
        "tagline": "Nurturing support for newborns, infants, and toddlers, helping new mothers rest and recover.",
        "icon": "👶",
        "image": "assets/images/service-baby-care.svg",
        "badge": "Infant & Mother Support",
        "who_benefits": [
            {"title": "New Mothers Recovering Postpartum", "desc": "Essential physical relief and rest following normal or caesarean delivery while baby is gently cared for."},
            {"title": "Working Parents Resuming Careers", "desc": "Dependable, attentive daytime infant care allowing parents to focus on work with complete peace of mind."},
            {"title": "Families with Infant Twins", "desc": "Extra pairs of experienced hands to manage simultaneous feeding, diaper changes, and soothing routines."},
            {"title": "First-Time Parents", "desc": "Practical guidance with baby burping, massage, bathing, and establishing comfortable sleep cycles."}
        ],
        "scope": [
            {"title": "Traditional Baby Massage & Bathing", "desc": "Gentle, experienced oil massage techniques followed by warm water baby bathing at the right temperature."},
            {"title": "Feeding Assistance & Burping", "desc": "Assisting with formula preparation, expressed breast milk bottle feeding, and thorough burping after meals."},
            {"title": "Diapering & Skin Hygiene", "desc": "Timely diaper changes, gentle cleaning, application of barrier creams, and maintaining rash-free baby skin."},
            {"title": "Soothing & Sleep Settling", "desc": "Gentle rocking, singing, swaddling, and comforting fussy babies to support regular sleep routines."},
            {"title": "Sanitizing Baby Accessories", "desc": "Washing and sterilizing feeding bottles, nipples, pacifiers, baby utensils, and bibs."},
            {"title": "Baby Clothes Washing & Tidying", "desc": "Washing baby clothes with gentle detergents, sun drying, and keeping baby nursery items organized."}
        ],
        "why_us": [
            {"title": "Gentle, Patient & Caring Nature", "desc": "Handling infants requires boundless patience, clean habits, and genuine love for little ones."},
            {"title": "Strict Hygiene Standards", "desc": "Regular handwashing, clean attire, and hygienic preparation of all baby feeding tools."},
            {"title": "Supportive of Mother's Choices", "desc": "We adapt to your family's parenting philosophy, feeding schedules, and household traditions."}
        ],
        "faqs": [
            {"q": "At what age can baby care assistance start?", "a": "We can arrange assistance starting from newborn stage (first few days after hospital discharge) up to toddlers."},
            {"q": "Does the caretaker know traditional newborn massage and bath?", "a": "Yes, our experienced baby caretakers are well-versed in gentle oil massage and traditional warm water bathing for infants."},
            {"q": "Can the baby caretaker assist overnight?", "a": "Yes, we coordinate night-shift baby caretakers so exhausted parents can get uninterrupted sleep while baby is fed and soothed."},
            {"q": "What should the family provide for baby care?", "a": "The family provides all baby consumables (massage oil, soap, diapers, wipes, formula, bottles, sterilizer, and baby clothing)."},
            {"q": "How do we enquire and confirm a baby caretaker?", "a": "Contact us with your baby's age, location in Chennai, and expected start date. We recommend booking in advance before delivery where possible."}
        ],
        "related": ["maid-services", "caretaker-services", "home-health-care-services"]
    },
    {
        "id": "elderly-care-services",
        "folder": "elderly-care-services",
        "title": "Dignified Elderly Care Services at Home in Chennai",
        "meta_title": "Elderly Care Services Chennai | Senior Home Care | Sugam Home Care",
        "meta_desc": "Dignified elderly care services in Chennai. In-home assistance for seniors: mobility, medication reminders, bathing, fall prevention, and loving companionship.",
        "headline": "Dignified Elderly Care Services at Home",
        "tagline": "Empowering senior parents to live safely, comfortably, and happily in their own cherished homes.",
        "icon": "🧓",
        "image": "assets/images/service-elderly-care.svg",
        "badge": "Senior Well-Being & Dignity",
        "who_benefits": [
            {"title": "Seniors Living Independently in Chennai", "desc": "Support for elderly parents while sons or daughters live in another city or abroad, ensuring daily well-being."},
            {"title": "Elders with Age-Related Mobility Issues", "desc": "Safe walking support and fall prevention for seniors with arthritis, Parkinson's, or joint stiffness."},
            {"title": "Seniors with Memory Loss or Dementia", "desc": "Calm, reassuring presence providing gentle orientation, familiar routines, and continuous safety oversight."},
            {"title": "Families Seeking Respite Care", "desc": "Dedicated support allowing family caregivers time to rest, work, or attend to personal commitments."}
        ],
        "scope": [
            {"title": "Fall Prevention & Walking Support", "desc": "Steadying hands during walking, navigating stairs, using walking aids, and securing bathroom visits."},
            {"title": "Bathing, Toileting & Grooming", "desc": "Patient, respectful assistance with personal hygiene, sponge/shower baths, oral care, and clean clothes."},
            {"title": "Medication Timing Reminders", "desc": "Ensuring seniors take their daily cardiac, diabetic, or general health tablets strictly on schedule."},
            {"title": "Nutritious Senior Meal Assistance", "desc": "Serving warm, easily digestible meals, monitoring fluid intake, and helping with feeding if required."},
            {"title": "Companionship & Cognitive Engagement", "desc": "Meaningful conversations, reading devotional books or newspapers, and sharing stories to uplift spirits."},
            {"title": "Daily Health Observation", "desc": "Noting daily mood, sleep quality, appetite, and alerting family members to any noticeable changes."}
        ],
        "why_us": [
            {"title": "Respecting Senior Independence", "desc": "We assist without taking away dignity, encouraging seniors to remain active and engaged in their daily lives."},
            {"title": "Tamil & Local Cultural Familiarity", "desc": "Caregivers who understand traditional South Indian senior preferences, vegetarian habits, and regional dialects."},
            {"title": "Transparent Communication with Children", "desc": "Regular check-ins and updates for family members, whether residing in Chennai or overseas."}
        ],
        "faqs": [
            {"q": "Can care be arranged for elderly parents living alone in Chennai?", "a": "Yes. A significant number of families we support have children living in other cities or overseas. We provide structured daily care and maintain close phone/WhatsApp coordination with family."},
            {"q": "How do you ensure bathroom safety and fall prevention?", "a": "Our caretakers are trained to remain physically alongside seniors during bathroom visits, bed-to-chair transfers, and walking routines to avoid slips and trips."},
            {"q": "Can we arrange elder care on a trial basis?", "a": "Yes, we encourage families to start with an initial period to ensure comfortable rapport between your elderly parent and the caregiver."},
            {"q": "What shift timings can we choose from?", "a": "We offer 12-hour day shifts, 12-hour night shifts, and comprehensive 24-hour live-in elderly care."},
            {"q": "How do we initiate senior care?", "a": "Call us or submit the enquiry form. We will discuss your parent's mobility level, medical history, and daily routine to recommend the right plan."}
        ],
        "related": ["caretaker-services", "home-health-care-services", "patient-care-services"]
    },
    {
        "id": "patient-care-services",
        "folder": "patient-care-services",
        "title": "Dedicated Patient Care Services at Home in Chennai",
        "meta_title": "Patient Care Services Chennai | Bedside Patient Care | Sugam Home Care",
        "meta_desc": "Bedside patient care services in Chennai. Attentive support for bedridden patients, stroke recovery, post-surgical care, and hygiene maintenance at home.",
        "headline": "Dedicated Bedside Patient Care Services",
        "tagline": "Attentive bedside support for bedridden or recovering individuals in Chennai.",
        "icon": "🛏️",
        "image": "assets/images/service-patient-care.svg",
        "badge": "Bedside Recovery Support",
        "who_benefits": [
            {"title": "Bedridden or Immobilized Individuals", "desc": "Specialized bed care focusing on pressure point relief, comfort positioning, and meticulous hygiene."},
            {"title": "Post-Operative Recovery Patients", "desc": "Gentle assistance following major orthopedic, spine, or general surgery during the initial recovery weeks."},
            {"title": "Stroke & Neurological Recovery", "desc": "Supporting patients with hemiplegia or weakness with transfers, eating assistance, and daily care routines."},
            {"title": "Critically Dependent Patients", "desc": "Continuous monitoring and physical support for individuals unable to perform self-care independently."}
        ],
        "scope": [
            {"title": "Repositioning & Bedsore Prevention", "desc": "Regular 2-hour position turning, air mattress maintenance, and skin inspection to prevent pressure sores."},
            {"title": "Bed Bathing & Personal Hygiene", "desc": "Thorough warm sponge bathing in bed, mouth care, hair hygiene, and prompt linen changes."},
            {"title": "Adult Diaper & Underpad Care", "desc": "Timely diaper changes, thorough perineal cleaning, and application of protective barrier creams."},
            {"title": "Non-Clinical Catheter & Tube Support", "desc": "Monitoring urine output, emptying catheter drainage bags hygienically, and keeping tubes untangled."},
            {"title": "Feeding Support (Oral / Liquid)", "desc": "Patient feeding assistance with pureed diets, soups, or assisting family with Ryle's tube feeding timings."},
            {"title": "Safe Transfers & Bed Exercises", "desc": "Gentle assistance transferring to wheelchairs or commode chairs and supporting passive limb movements."}
        ],
        "why_us": [
            {"title": "Trained Bedside Attendants", "desc": "Experienced in safe lifting techniques, infection avoidance, and respectful handling of vulnerable patients."},
            {"title": "Reduced Hospital Readmissions", "desc": "Consistent hygiene and attentive skin care prevent common post-discharge complications like UTIs and bedsores."},
            {"title": "Relief for Family Caregivers", "desc": "Lifting and turning a heavy bedridden patient takes an immense physical toll. Our attendants bear that weight."}
        ],
        "faqs": [
            {"q": "What is the difference between a patient care attendant and a registered nurse?", "a": "A patient care attendant handles hands-on physical care: turning, bed bathing, diapering, feeding assistance, and comfort. A registered nurse performs clinical procedures: administering IV medications, sterile dressing, and clinical catheterization."},
            {"q": "How do you manage bedsores for bedridden individuals?", "a": "Our attendants focus on regular body turning, keeping skin clean and dry, using moisture barrier creams, and ensuring smooth, wrinkle-free bedsheets on air mattresses."},
            {"q": "Can patient care be provided 24 hours a day?", "a": "Yes, we provide 24-hour round-the-clock patient care arrangements with dedicated day and night attendants."},
            {"q": "What equipment is helpful to have at home?", "a": "Depending on the patient's condition, an adjustable hospital bed, ripple air mattress, adult diapers, wet wipes, and a wheelchair or commode chair are very helpful."},
            {"q": "How quickly can patient care be arranged?", "a": "We encourage contacting us 24 to 48 hours before hospital discharge so we can assign an attendant ready for the patient's arrival home."}
        ],
        "related": ["nursing-services-at-home", "home-health-care-services", "elderly-care-services"]
    },
    {
        "id": "nursing-services-at-home",
        "folder": "nursing-services-at-home",
        "title": "Qualified Nursing Services at Home in Chennai",
        "meta_title": "Home Nursing Services Chennai | Qualified Nurses at Home | Sugam Home Care",
        "meta_desc": "Qualified nursing services at home in Chennai. Injections, IV infusions, surgical wound dressings, catheterization, and post-operative clinical nursing.",
        "headline": "Qualified Nursing Services at Home",
        "tagline": "Clinical nursing procedures delivered at your doorstep under medical prescription.",
        "icon": "👩‍⚕️",
        "image": "assets/images/service-nursing.svg",
        "badge": "Qualified Clinical Care",
        "who_benefits": [
            {"title": "Patients Requiring Clinical Injections", "desc": "Safe administration of prescribed intramuscular (IM), subcutaneous (SC), or IV injections without hospital visits."},
            {"title": "Post-Surgical Wound Dressing", "desc": "Aseptic dressing changes for surgical incisions, diabetic foot ulcers, bedsores, and suture removal."},
            {"title": "Patients on IV Fluid Therapy", "desc": "Professional IV cannula insertion, IV infusion monitoring, and sterile line maintenance at home."},
            {"title": "Patients with Catheters or Ryle's Tubes", "desc": "Urinary catheterization, bladder wash, and nasogastric tube insertion/feeding management by qualified nurses."}
        ],
        "scope": [
            {"title": "Doctor-Prescribed Injection Administration", "desc": "Administering antibiotics, insulin, pain management, or vitamin injections strictly per valid prescription."},
            {"title": "Aseptic Wound Dressing & Suture Care", "desc": "Sterile dressing changes for post-op wounds, chronic ulcers, burns, and removal of surgical stitches/staples."},
            {"title": "IV Infusions & Cannula Management", "desc": "IV line insertion, fluid infusion, antibiotic drips, and careful monitoring for phlebitis or infiltration."},
            {"title": "Urinary Catheter Insertion & Care", "desc": "Foley's catheter insertion, replacement, regular bladder irrigation, and aseptic catheter maintenance."},
            {"title": "Nasogastric (Ryle's) Tube Care", "desc": "Ryle's tube insertion, positioning verification, aspiration checks, and feeding protocol administration."},
            {"title": "Tracheostomy & Respiratory Care", "desc": "Sterile suctioning, inner cannula cleaning, stoma dressing, and oxygen saturation management."}
        ],
        "why_us": [
            {"title": "Qualified Nursing Professionals", "desc": "Trained nurses with clinical credentials, understanding aseptic techniques and doctor's orders."},
            {"title": "Strict Medical Protocol Adherence", "desc": "We administer medications and clinical procedures only upon verification of a valid doctor's prescription."},
            {"title": "Avoid Hospital Travel & Infection Risks", "desc": "Receiving clinical nursing at home eliminates painful travel for fragile patients and reduces hospital-acquired infection risks."}
        ],
        "faqs": [
            {"q": "Do I need a doctor's prescription for home nursing services?", "a": "Yes, absolutely. For all clinical procedures including injections, IV infusions, wound dressings, and catheter insertion, a valid, signed prescription from your attending physician is mandatory."},
            {"q": "Can a nurse visit for single clinical procedures like an injection or dressing?", "a": "Yes, we coordinate procedure-based nurse visits (such as a single daily visit for wound dressing or antibiotic injections) as well as continuous shifts."},
            {"q": "Are emergency medical services included?", "a": "No. Our home nursing is intended for scheduled, prescribed clinical care. In case of an acute medical emergency, please call 108 or proceed to the nearest hospital emergency department."},
            {"q": "What medical consumables must the patient provide?", "a": "The patient's family should provide the prescribed medications, IV fluids, sterile dressing packets, disposable gloves, syringes, and catheters as prescribed by the doctor."},
            {"q": "How can I request a home nurse in Chennai?", "a": "Call our team or submit the enquiry form with your doctor's prescription details and location in Chennai for prompt coordination."}
        ],
        "related": ["patient-care-services", "home-health-care-services", "elderly-care-services"]
    }
]

def generate_service_page(svc):
    header = get_header(f"/{svc['folder']}/", depth=1)
    footer = get_footer(depth=1)
    rel = "../"
    
    # Who benefits cards
    benefits_html = ""
    for item in svc["who_benefits"]:
        benefits_html += f'''
        <div class="trust-card">
          <div class="trust-icon-box">✓</div>
          <h3>{item["title"]}</h3>
          <p>{item["desc"]}</p>
        </div>
        '''

    # Scope of assistance cards
    scope_html = ""
    for s in svc["scope"]:
        scope_html += f'''
        <div class="scope-item-card">
          <div class="scope-icon-wrap">✓</div>
          <div class="scope-content">
            <h4>{s["title"]}</h4>
            <p>{s["desc"]}</p>
          </div>
        </div>
        '''

    # Why us cards
    why_html = ""
    for idx, w in enumerate(svc["why_us"], 1):
        why_html += f'''
        <div class="benefit-item">
          <div class="benefit-number">0{idx}</div>
          <h3>{w["title"]}</h3>
          <p>{w["desc"]}</p>
        </div>
        '''

    # FAQs accordion
    faq_html = ""
    faq_schema = []
    for f in svc["faqs"]:
        faq_html += f'''
        <div class="faq-item">
          <button type="button" class="faq-question">
            <span>{f["q"]}</span>
            <svg class="faq-icon-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </button>
          <div class="faq-answer">
            <div class="faq-answer-inner">{f["a"]}</div>
          </div>
        </div>
        '''
        faq_schema.append(f'''{{
          "@type": "Question",
          "name": "{f["q"]}",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "{f["a"]}"
          }}
        }}''')

    # Related services cards
    related_html = ""
    svc_map = {s["id"]: s for s in SERVICES}
    for rel_id in svc["related"]:
        if rel_id in svc_map:
            r = svc_map[rel_id]
            related_html += f'''
            <article class="service-card">
              <div class="service-card-media">
                <img src="{rel}{r["image"]}" alt="{r["title"]}" class="service-card-img" width="600" height="400" loading="lazy">
                <span class="service-card-badge">{r["badge"]}</span>
              </div>
              <div class="service-card-body">
                <div class="service-card-header">
                  <span class="service-card-icon">{r["icon"]}</span>
                  <h3 class="service-card-title"><a href="{rel}{r["folder"]}/">{r["headline"]}</a></h3>
                </div>
                <p class="service-card-text">{r["tagline"]}</p>
                <div class="service-card-actions">
                  <a href="{rel}{r["folder"]}/" class="btn btn-outline-primary">View Details</a>
                  <button type="button" class="btn btn-primary btn-open-modal" data-service="{r["headline"]}">Enquire</button>
                </div>
              </div>
            </article>
            '''

    faq_schema_str = ",\n        ".join(faq_schema)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{svc["meta_title"]}</title>
  <meta name="description" content="{svc["meta_desc"]}">
  <link rel="canonical" href="https://sugamhomecareservices.in/{svc["folder"]}/">
  <link rel="icon" type="image/svg+xml" href="{rel}assets/images/favicon.svg">

  <!-- Open Graph -->
  <meta property="og:title" content="{svc["meta_title"]}">
  <meta property="og:description" content="{svc["meta_desc"]}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://sugamhomecareservices.in/{svc["folder"]}/">
  <meta property="og:image" content="https://sugamhomecareservices.in/{svc["image"]}">

  <!-- Styles -->
  <link rel="stylesheet" href="{rel}assets/css/style.css">
  <link rel="stylesheet" href="{rel}assets/css/components.css">

  <!-- Structured Data: Service + BreadcrumbList + FAQPage -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Service",
        "name": "{svc["headline"]}",
        "provider": {{
          "@type": "HomeHealthService",
          "name": "Sugam Home Care Services",
          "telephone": "+918438861636",
          "url": "https://sugamhomecareservices.in/",
          "address": {{
            "@type": "PostalAddress",
            "streetAddress": "No. 123/12, Kattabomman Street, Kamaraj Nagar, New Perungalathur",
            "addressLocality": "Chennai",
            "postalCode": "600063",
            "addressRegion": "Tamil Nadu",
            "addressCountry": "IN"
          }}
        }},
        "areaServed": "Chennai",
        "description": "{svc["meta_desc"]}"
      }},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{
            "@type": "ListItem",
            "position": 1,
            "name": "Home",
            "item": "https://sugamhomecareservices.in/"
          }},
          {{
            "@type": "ListItem",
            "position": 2,
            "name": "Services",
            "item": "https://sugamhomecareservices.in/services/"
          }},
          {{
            "@type": "ListItem",
            "position": 3,
            "name": "{svc["headline"]}",
            "item": "https://sugamhomecareservices.in/{svc["folder"]}/"
          }}
        ]
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
          {faq_schema_str}
        ]
      }}
    ]
  }}
  </script>
</head>
<body>

{header}

<main>
  <!-- 1-4. SERVICE HERO SECTION -->
  <section class="service-hero-section">
    <div class="container">
      <!-- Breadcrumbs -->
      <nav class="breadcrumbs" aria-label="Breadcrumbs">
        <a href="{rel}">Home</a>
        <span class="breadcrumbs-separator">/</span>
        <a href="{rel}services/">Services</a>
        <span class="breadcrumbs-separator">/</span>
        <span>{svc["headline"]}</span>
      </nav>

      <div class="hero-grid">
        <!-- Left: Service Overview & CTAs -->
        <div class="hero-content">
          <div class="hero-badge">
            <span style="font-size: 1.15rem;">{svc["icon"]}</span>
            {svc["badge"]} • Chennai
          </div>

          <h1 class="hero-headline">{svc["headline"]}</h1>
          <p class="hero-description">{svc["tagline"]}</p>

          <!-- CTAs -->
          <div class="hero-cta-group">
            <a href="tel:+918438861636" data-config="phoneTel" class="btn btn-primary btn-lg">
              <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"></path></svg>
              Call for Enquiry
            </a>
            <a href="https://wa.me/918438861636" data-config="whatsappLink" data-service="{svc["headline"]}" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp btn-lg">
              <svg class="icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0012.04 2zm5.79 14.07c-.24.67-1.39 1.29-1.93 1.37-.5.08-1.12.11-3.56-.88-3.09-1.28-5.06-4.42-5.21-4.63-.16-.2-1.24-1.66-1.24-3.16 0-1.51.78-2.25 1.06-2.55.28-.3.61-.38.81-.38.2 0 .41 0 .59.01.19.01.44-.07.69.52.25.6.86 2.1.94 2.25.08.16.14.34.03.55-.11.21-.16.34-.32.53-.16.19-.34.42-.48.56-.16.16-.33.33-.14.65.19.32.84 1.38 1.8 2.24 1.24 1.11 2.28 1.45 2.61 1.61.32.16.51.14.7-.08.19-.22.82-.95 1.04-1.28.22-.32.44-.27.75-.16.3.11 1.93.91 2.26 1.08.33.16.55.25.63.39.08.13.08.77-.16 1.44z"></path></svg>
              WhatsApp Us
            </a>
          </div>

          <a href="tel:+918438861636" data-config="phoneTel" class="hero-phone-cta">
            <div class="hero-phone-icon-wrap">
              <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"></path></svg>
            </div>
            <span>Call directly: <strong data-config="phoneDisplay">+91 84388 61636</strong></span>
          </a>

          <div style="margin-top: 1rem; border-radius: var(--radius-lg); overflow: hidden; border: 1px solid var(--border-light); max-width: 520px;">
            <img src="{rel}{svc["image"]}" alt="{svc["headline"]}" width="600" height="400" style="width: 100%; height: auto;">
          </div>
        </div>

        <!-- Right: Dedicated Lead Form Preselected -->
        <div class="hero-card-wrapper" id="service-enquiry">
          <div class="enquiry-card">
            <div class="enquiry-card-header">
              <span class="badge-tag">{svc["headline"]}</span>
              <h2 class="enquiry-card-title">Enquire for This Service</h2>
              <p class="enquiry-card-subtitle">Connect with our care coordinator to discuss requirements and availability in Chennai.</p>
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
                  <option value="{svc["headline"]}" selected>{svc["headline"]}</option>
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
                <input type="checkbox" id="svc-consent-{svc["id"]}" name="consent" required checked>
                <label for="svc-consent-{svc["id"]}">I agree to be contacted by Sugam Home Care Services regarding this enquiry.</label>
              </div>

              <button type="submit" class="btn-submit-lead">
                Request a Call Back
              </button>

              <div class="form-security-note">
                <svg class="icon" style="width:14px; height:14px; color:var(--color-secondary);" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0110 0v4"></path></svg>
                Your phone number is confidential and never shared.
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 5. WHO MAY BENEFIT FROM THIS SERVICE -->
  <section class="section section-bg-surface">
    <div class="container">
      <div class="section-header">
        <span class="badge-tag">Who Needs This Service?</span>
        <h2>Who May Benefit from {svc["headline"]}</h2>
        <p class="section-subtitle">Understanding when and how this service provides the greatest comfort and practical support for families.</p>
      </div>

      <div class="trust-grid">
        {benefits_html}
      </div>
    </div>
  </section>

  <!-- 6. TYPES OF ASSISTANCE AVAILABLE (DETAILED SCOPE) -->
  <section class="section">
    <div class="container">
      <div class="section-header">
        <span class="badge-tag">What's Included</span>
        <h2>Types of Assistance Available</h2>
        <p class="section-subtitle">A clear breakdown of duties and care activities covered under our {svc["headline"]}.</p>
      </div>

      <div class="service-scope-grid">
        {scope_html}
      </div>
    </div>
  </section>

  <!-- 7. HOW IT WORKS: ENQUIRY AND ARRANGEMENT PROCESS -->
  <section class="section section-bg-warm">
    <div class="container">
      <div class="section-header">
        <span class="badge-tag">Simple & Transparent</span>
        <h2>How the Service Arrangement Process Works</h2>
        <p class="section-subtitle">Four straightforward steps to arrange dependable home care support for your family.</p>
      </div>

      <div class="steps-grid">
        <div class="step-card">
          <div class="step-badge">1</div>
          <h3>Tell Us Your Needs</h3>
          <p>Submit the enquiry form or call our coordinator with your preferred timings and location in Chennai.</p>
        </div>

        <div class="step-card">
          <div class="step-badge">2</div>
          <h3>Detailed Consultation</h3>
          <p>We review your loved one’s specific requirements, daily routines, and household preferences.</p>
        </div>

        <div class="step-card">
          <div class="step-badge">3</div>
          <h3>Care Matching</h3>
          <p>We select suitable personnel experienced in providing this specific care assistance.</p>
        </div>

        <div class="step-card">
          <div class="step-badge">4</div>
          <h3>Service Commences</h3>
          <p>Service starts with ongoing coordination and regular feedback to ensure complete family satisfaction.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- 8. WHY FAMILIES CONSIDER THIS TYPE OF SUPPORT -->
  <section class="section">
    <div class="container">
      <div class="section-header">
        <span class="badge-tag">Benefits & Value</span>
        <h2>Why Families Choose Sugam for {svc["headline"]}</h2>
        <p class="section-subtitle">Compassionate support that brings peace of mind, reliable routines, and comfort at home.</p>
      </div>

      <div class="benefits-grid">
        {why_html}
      </div>
    </div>
  </section>

  <!-- 9. RELEVANT FREQUENTLY ASKED QUESTIONS -->
  <section class="section section-bg-surface">
    <div class="container">
      <div class="section-header">
        <span class="badge-tag">Common Enquiries</span>
        <h2>Frequently Asked Questions</h2>
        <p class="section-subtitle">Clear, factual answers to help you make an informed decision.</p>
      </div>

      <div class="faq-container">
        {faq_html}
      </div>
    </div>
  </section>

  <!-- 10. RELATED SERVICES -->
  <section class="section">
    <div class="container">
      <div class="section-header">
        <span class="badge-tag">Explore More Services</span>
        <h2>Related Home Care Services</h2>
        <p class="section-subtitle">Families often combine or transition between these supportive care options.</p>
      </div>

      <div class="services-grid">
        {related_html}
      </div>
    </div>
  </section>

  <!-- 11-12. FINAL ENQUIRY CTA & CONTACT INFO -->
  <section class="final-cta-section">
    <div class="container final-cta-box">
      <span class="badge-tag" style="background-color: rgba(255,255,255,0.15); color: #2DD4BF;">Take the First Step</span>
      <h2>Ready to Arrange {svc["headline"]}?</h2>
      <p>
        Speak directly with our team to discuss timings, availability, and specific care preferences in Chennai.
      </p>
      <div class="final-cta-buttons">
        <a href="tel:+918438861636" data-config="phoneTel" class="btn btn-white btn-lg">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"></path></svg>
          Call Now
        </a>
        <a href="https://wa.me/918438861636" data-config="whatsappLink" data-service="{svc["headline"]}" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp btn-lg">
          <svg class="icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0012.04 2zm5.79 14.07c-.24.67-1.39 1.29-1.93 1.37-.5.08-1.12.11-3.56-.88-3.09-1.28-5.06-4.42-5.21-4.63-.16-.2-1.24-1.66-1.24-3.16 0-1.51.78-2.25 1.06-2.55.28-.3.61-.38.81-.38.2 0 .41 0 .59.01.19.01.44-.07.69.52.25.6.86 2.1.94 2.25.08.16.14.34.03.55-.11.21-.16.34-.32.53-.16.19-.34.42-.48.56-.16.16-.33.33-.14.65.19.32.84 1.38 1.8 2.24 1.24 1.11 2.28 1.45 2.61 1.61.32.16.51.14.7-.08.19-.22.82-.95 1.04-1.28.22-.32.44-.27.75-.16.3.11 1.93.91 2.26 1.08.33.16.55.25.63.39.08.13.08.77-.16 1.44z"></path></svg>
          WhatsApp Us
        </a>
        <a href="#service-enquiry" class="btn btn-secondary btn-lg">
          Request a Call Back
        </a>
      </div>
    </div>
  </section>
</main>

{footer}

</body>
</html>'''

    filepath = os.path.join(svc["folder"], "index.html")
    full_path = os.path.join(ROOT_DIR, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(html.strip() + "\n")
    print(f"Generated: {filepath}")

for s in SERVICES:
    generate_service_page(s)

print("All 7 service pages generated successfully!")
