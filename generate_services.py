#!/usr/bin/env python3
import os
from site_templates import get_header, get_footer

ROOT_DIR = "/Users/karthik/.gemini/antigravity/scratch/sugam-home-care"

# 11 Approved Services
SERVICES = [
    {
        "id": "baby-care-services",
        "folder": "baby-care-services",
        "title": "Gentle & Loving Baby Care Services in Chennai & Tamil Nadu",
        "meta_title": "Baby Care Services in Chennai | Newborn & Infant Care | Sugam Home Care",
        "meta_desc": "Loving, dependable baby care services in Chennai & Tamil Nadu. Newborn massage, warm bathing, bottle feeding assistance, diaper changing, and new mother support.",
        "headline": "Baby Care Services",
        "tagline": "Nurturing support for newborns, infants, and toddlers, helping new mothers rest and recover.",
        "icon": "👶",
        "image": "assets/images/service-baby-care.svg",
        "badge": "Infant & Mother Support",
        "who_benefits": [
            {"title": "New Mothers Recovering Postpartum", "desc": "Essential physical relief and rest following normal or caesarean delivery while baby is gently cared for."},
            {"title": "Working Parents Resuming Careers", "desc": "Dependable, attentive daytime infant care allowing parents to focus on work with complete peace of mind."},
            {"title": "Families with Infant Twins", "desc": "Extra pairs of experienced hands to manage simultaneous feeding, diaper changes, and soothing routines."},
            {"title": "First-Time Parents", "desc": "Practical guidance with baby burping, oil massage, warm bath, and establishing comfortable sleep cycles."}
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
            {"q": "At what age can baby care assistance start?", "a": "We arrange assistance starting from newborn stage (first few days after hospital discharge) up to toddlers."},
            {"q": "Does the caretaker know traditional newborn massage and bath?", "a": "Yes, our experienced baby caretakers are well-versed in gentle oil massage and traditional warm water bathing for infants."},
            {"q": "Can the baby caretaker assist overnight?", "a": "Yes, we coordinate night-shift baby caretakers so exhausted parents can get uninterrupted sleep while baby is fed and soothed."},
            {"q": "What locations do you cover for baby care?", "a": "We cover 35+ prime locations across Chennai. Outside Chennai across Tamil Nadu, services are provided on a One-Day Full (24-Hour) basis."},
            {"q": "How do we enquire and confirm a baby caretaker?", "a": "Contact us with your baby's age, location, and expected start date. We recommend booking in advance before delivery where possible."}
        ],
        "related": ["caretaker-services-at-home", "home-health-care-for-seniors", "elderly-care-services"]
    },
    {
        "id": "elderly-care-services",
        "folder": "elderly-care-services",
        "title": "Dignified Elderly Care Services at Home in Chennai & Tamil Nadu",
        "meta_title": "Elderly Care Services Chennai | Senior Home Care | Sugam Home Care",
        "meta_desc": "Dignified elderly care services in Chennai & Tamil Nadu. In-home assistance for seniors: mobility, medication reminders, bathing, fall prevention, and loving companionship.",
        "headline": "Elderly Care Services",
        "tagline": "Empowering senior parents to live safely, comfortably, and happily in their own cherished homes.",
        "icon": "🧓",
        "image": "assets/images/service-elderly-care.svg",
        "badge": "Senior Well-Being & Dignity",
        "who_benefits": [
            {"title": "Seniors Living Independently", "desc": "Support for elderly parents while sons or daughters live in another city or abroad, ensuring daily well-being."},
            {"title": "Elders with Age-Related Mobility Issues", "desc": "Safe walking support and fall prevention for seniors with arthritis, Parkinson's, or joint stiffness."},
            {"title": "Seniors with Memory Concerns", "desc": "Calm, reassuring presence providing gentle orientation, familiar routines, and continuous safety oversight."},
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
            {"title": "Tamil Nadu Wide Service Availability", "desc": "Full-time shift care available across Chennai and on a 24-Hour full-day basis all over Tamil Nadu."}
        ],
        "faqs": [
            {"q": "Can care be arranged for elderly parents living alone in Chennai?", "a": "Yes. A significant number of families we support have children living in other cities or overseas. We provide structured daily care and maintain close phone/WhatsApp coordination with family."},
            {"q": "How do you address safety and fall prevention at home?", "a": "Our caretakers remain physically alongside seniors during bathroom visits, bed-to-chair transfers, and walking routines to avoid slips and trips."},
            {"q": "Can we arrange elder care on a trial period before committing long-term?", "a": "Yes, we encourage families to start with an initial period to ensure comfortable rapport between your elderly parent and the caregiver."},
            {"q": "What shift timings can we choose from?", "a": "We offer 12-hour day shifts, 12-hour night shifts, and comprehensive 24-hour live-in elderly care."},
            {"q": "Are services available outside Chennai?", "a": "Yes, we provide elder care across all districts of Tamil Nadu on a One-Day Full (24-Hour) basis."}
        ],
        "related": ["senior-citizen-care-services", "dementia-care-for-the-elderly", "caretaker-services-at-home"]
    },
    {
        "id": "patient-care-services",
        "folder": "patient-care-services",
        "title": "Dedicated Patient Care Services at Home in Chennai & Tamil Nadu",
        "meta_title": "Patient Care Services Chennai | Bedside Patient Care | Sugam Home Care",
        "meta_desc": "Dedicated patient care services in Chennai & Tamil Nadu. Attentive support for recovering patients, mobility assistance, sponge bathing, feeding, and personal hygiene.",
        "headline": "Patient Care Services",
        "tagline": "Attentive bedside support and physical assistance for recovering individuals at home.",
        "icon": "🛏️",
        "image": "assets/images/service-patient-care.svg",
        "badge": "Bedside Recovery Support",
        "who_benefits": [
            {"title": "Post-Operative Recovery Patients", "desc": "Gentle assistance following major orthopedic, spine, or general surgery during initial recovery weeks."},
            {"title": "Stroke & Neurological Recovery", "desc": "Supporting patients with hemiplegia or weakness with transfers, eating assistance, and daily care routines."},
            {"title": "Immobilized & Weak Individuals", "desc": "Specialized bed care focusing on comfort positioning, assisted movement, and meticulous personal hygiene."},
            {"title": "Family Caregiver Relief", "desc": "Providing dependable hands-on physical assistance so family members can rest and manage other duties."}
        ],
        "scope": [
            {"title": "Bed Bathing & Personal Hygiene", "desc": "Thorough warm sponge bathing in bed, oral care, hair grooming, and prompt linen changes."},
            {"title": "Assisted Transfers & Mobility", "desc": "Safe assistance transferring between bed, commode chair, and wheelchair, avoiding sudden strain."},
            {"title": "Diaper & Underpad Care", "desc": "Timely adult diaper changes, thorough perineal cleaning, and application of protective barrier creams."},
            {"title": "Feeding Support (Oral / Pureed)", "desc": "Assistance with soft diet feeding, soups, juices, and monitoring hydration levels."},
            {"title": "Medication & Doctor Reminders", "desc": "Timely administration of oral medicines as prescribed in the hospital discharge summary."},
            {"title": "Post-Surgical Convalescence Support", "desc": "Keeping resting posture comfortable and monitoring patient comfort throughout day or night."}
        ],
        "why_us": [
            {"title": "Trained Bedside Attendants", "desc": "Experienced in safe lifting techniques, infection avoidance, and respectful handling of vulnerable patients."},
            {"title": "Reduced Hospital Readmissions", "desc": "Consistent hygiene and attentive skin care prevent common post-discharge complications."},
            {"title": "Tamil Nadu Wide Full-Day Care", "desc": "Available across Chennai and on a 24-Hour full-day basis all over Tamil Nadu."}
        ],
        "faqs": [
            {"q": "What is the difference between a patient care attendant and a registered nurse?", "a": "A patient care attendant handles hands-on physical care: turning, bed bathing, diapering, feeding assistance, and comfort. A registered nurse performs clinical procedures: administering IV medications, sterile dressing, and clinical catheterization."},
            {"q": "Can a patient care attendant help immediately after hospital discharge?", "a": "Yes. We coordinate attendants ready to assist from the day of hospital discharge."},
            {"q": "Can patient care be provided 24 hours a day?", "a": "Yes, we provide 24-hour round-the-clock patient care arrangements with dedicated day and night attendants."},
            {"q": "What equipment is helpful to have at home?", "a": "Depending on patient condition, an adjustable hospital bed, air mattress, adult diapers, wet wipes, and a wheelchair or commode chair are helpful."},
            {"q": "Do you cover outside Chennai?", "a": "Yes, patient care services are available all over Tamil Nadu on a 24-Hour One-Day Full basis."}
        ],
        "related": ["bedridden-patient-care-services", "home-care-for-cancer-patients", "nursing-services"]
    },
    {
        "id": "senior-citizen-care-services",
        "folder": "senior-citizen-care-services",
        "title": "Comprehensive Senior Citizen Care Services in Chennai & Tamil Nadu",
        "meta_title": "Senior Citizen Care Services Chennai | Elderly Companion Care | Sugam Home Care",
        "meta_desc": "Compassionate senior citizen care services in Chennai & Tamil Nadu. Daily living support, walking assistance, nutritious meal help, and empathetic companion care.",
        "headline": "Senior Citizen Care Services",
        "tagline": "Empowering senior citizens with active daily living assistance, walking support, meal assistance, and social engagement.",
        "icon": "👴",
        "image": "assets/images/service-senior-citizen.svg",
        "badge": "Senior Citizen Support",
        "who_benefits": [
            {"title": "Independent Seniors Needing Daytime Help", "desc": "Safe assistance with morning walks, reading, meal serving, and managing daily domestic routines."},
            {"title": "Seniors with Joint Pain & Arthritis", "desc": "Hands-on support steadying seniors during walking, sitting, and navigating household steps."},
            {"title": "Seniors Living Alone in Chennai", "desc": "Dependable daily visits or live-in companions ensuring emergency safety and emotional reassurance."},
            {"title": "Sons & Daughters Working Overseas", "desc": "Peace of mind knowing your parents receive attentive, respectful daily care with transparent communication."}
        ],
        "scope": [
            {"title": "Daily Living & Mobility Support", "desc": "Assisting with morning wake-up routines, walking support, and gentle physical movement."},
            {"title": "Nutritious Meal Assistance", "desc": "Serving warm, freshly prepared senior-friendly meals on time and encouraging adequate water intake."},
            {"title": "Prescription Medication Reminders", "desc": "Keeping daily medicine boxes organized and ensuring tablets are taken strictly on time."},
            {"title": "Accompaniment on Walks & Outings", "desc": "Accompanying seniors to neighborhood temples, parks, evening walks, or clinic appointments."},
            {"title": "Social Engagement & Conversation", "desc": "Active conversation in Tamil or English, reading newspapers, playing games, and uplifting senior morale."},
            {"title": "Emergency Vigilance", "desc": "Immediate alerting of family members or doctors in case of sudden weakness, dizziness, or distress."}
        ],
        "why_us": [
            {"title": "Empathy, Patience & Respect", "desc": "Our caretakers are trained to value senior wisdom, honor their routines, and provide gentle companionship."},
            {"title": "Local Cultural Understanding", "desc": "Familiarity with South Indian vegetarian routines, traditional prayers, and respectful habits."},
            {"title": "Flexible 12-Hour & 24-Hour Shifts", "desc": "Arrangements tailored to your family's exact daytime, nighttime, or full-day requirements."}
        ],
        "faqs": [
            {"q": "How does senior citizen care differ from patient care?", "a": "Senior citizen care focuses on active daily living, mobility, companionship, meal assistance, and lifestyle support for relatively mobile elders, while patient care focuses on bedside recovery and physical convalescence."},
            {"q": "Can the caregiver prepare light meals for my parents?", "a": "Yes, our senior caregivers can assist with serving, warming, or preparing light wholesome meals such as kanji, idli, upma, or fruits."},
            {"q": "Do your caregivers speak Tamil?", "a": "Yes, our caregivers speak Tamil and understand regional Chennai and Tamil Nadu household culture."},
            {"q": "Are senior citizen services available outside Chennai?", "a": "Yes, across all districts of Tamil Nadu on a One-Day Full (24-Hour) care basis."},
            {"q": "How do we get started?", "a": "Call us at +91 84388 61636 or submit the enquiry form with your parents' location and care needs."}
        ],
        "related": ["elderly-care-services", "home-health-care-for-seniors", "dementia-care-for-the-elderly"]
    },
    {
        "id": "bedridden-patient-care-services",
        "folder": "bedridden-patient-care-services",
        "title": "Specialized Bedridden Patient Care Services in Chennai & Tamil Nadu",
        "meta_title": "Bedridden Patient Care Services Chennai | Bedsore Prevention | Sugam Home Care",
        "meta_desc": "Specialized bedridden patient care services in Chennai & Tamil Nadu. 2-hour repositioning, bedsore prevention, sponge bathing, adult diaper hygiene, and gentle feeding.",
        "headline": "Bedridden Patient Care Services",
        "tagline": "Specialized, gentle bedside assistance for bedridden individuals, focusing on bedsore prevention and dignity.",
        "icon": "🛌",
        "image": "assets/images/service-bedridden.svg",
        "badge": "Intensive Bedside Care",
        "who_benefits": [
            {"title": "Completely Bedridden Seniors", "desc": "Patients unable to turn or get out of bed independently, requiring dedicated 24-hour hands-on care."},
            {"title": "Paralysis & Severe Stroke Patients", "desc": "Attentive positioning, passive limb movement, and specialized feeding assistance for hemiplegia patients."},
            {"title": "Spine & Hip Fracture Recovery", "desc": "Immobilized patients needing gentle bed bathing, bedpan assistance, and zero-strain posture care."},
            {"title": "End-Stage Palliative Care", "desc": "Compassionate, peaceful bedside care keeping patients clean, pain-managed, and comforted at home."}
        ],
        "scope": [
            {"title": "2-Hour Position Turning", "desc": "Strict scheduled body repositioning between left lateral, back, and right lateral to prevent pressure ulcers."},
            {"title": "Bedsore Prevention & Skin Care", "desc": "Inspecting pressure points (sacrum, heels, elbows), applying barrier creams, and ensuring wrinkle-free linen."},
            {"title": "Daily Sponge Bathing in Bed", "desc": "Warm, gentle head-to-toe sponge bathing, hair cleaning, mouth hygiene, and skin moisturizing in bed."},
            {"title": "Adult Diaper & Incontinence Hygiene", "desc": "Frequent diaper inspections, prompt cleaning with wet wipes, and maintaining sterile perineal hygiene."},
            {"title": "Catheter & Drainage Bag Care", "desc": "Emptying urinary drainage bags hygienically, monitoring output volume, and preventing tube entanglement."},
            {"title": "Assisted Feeding & Hydration", "desc": "Careful elevated feeding of pureed diets, soups, or assisting family with Ryle's tube feeding timings."}
        ],
        "why_us": [
            {"title": "Trained in Safe Bedside Techniques", "desc": "Attendants trained in safe turning, infection prevention, and dignified handling of immobilized patients."},
            {"title": "Zero Compromise on Hygiene", "desc": "Strict cleanliness routines preventing urinary tract infections and skin breakdown."},
            {"title": "Round-the-Clock (24/7) Shifts", "desc": "Dedicated day and night attendants ensuring uninterrupted bedside vigilance."}
        ],
        "faqs": [
            {"q": "How do your caregivers prevent bedsores in bedridden patients?", "a": "We maintain strict 2-hour turning schedules, use ripple air mattresses, keep skin completely clean and dry, apply medical barrier creams, and inspect bony prominences daily."},
            {"q": "Can your attendants manage Ryle's tube feeding?", "a": "Yes, our attendants assist with preparing and administering prescribed liquid feeds at the recommended head-elevated angle and schedule."},
            {"q": "Is bedridden patient care available on a 24-hour basis?", "a": "Yes, 24-hour live-in or day/night shifts are our primary format for bedridden patient care."},
            {"q": "Do you provide this service outside Chennai in Tamil Nadu?", "a": "Yes, bedridden patient care is available all over Tamil Nadu on a 24-Hour One-Day Full care basis."},
            {"q": "What should the family arrange at home?", "a": "An adjustable hospital bed, air mattress, adult diapers, wet wipes, and skin barrier ointment are highly recommended."}
        ],
        "related": ["patient-care-services", "home-care-for-cancer-patients", "nursing-services"]
    },
    {
        "id": "home-health-care-for-seniors",
        "folder": "home-health-care-for-seniors",
        "title": "Home Health Care Services for Seniors in Chennai & Tamil Nadu",
        "meta_title": "Home Health Care for Seniors Chennai | Geriatric Health Monitoring | Sugam Home Care",
        "meta_desc": "Structured home health care services for seniors in Chennai & Tamil Nadu. Routine vital signs monitoring (BP, sugar, pulse), medication supervision, and convalescence.",
        "headline": "Home Health Care for Seniors",
        "tagline": "Personalized health support, vitals monitoring, and recovery assistance in the comfort of your home.",
        "icon": "🩺",
        "image": "assets/images/service-home-health.svg",
        "badge": "Senior Health Monitoring",
        "who_benefits": [
            {"title": "Seniors with Hypertension & Diabetes", "desc": "Consistent recording of blood pressure and glucose levels, preventing sudden spikes or drops."},
            {"title": "Post-Hospital Discharge Recovery", "desc": "Smooth transition from hospital to home with structured daily health monitoring and recovery guidance."},
            {"title": "Elders with Multiple Prescriptions", "desc": "Eliminating missed or duplicate doses with disciplined medication schedule supervision."},
            {"title": "Families Seeking Preventive Oversight", "desc": "Early detection of health fluctuations, avoiding emergency hospital admissions."}
        ],
        "scope": [
            {"title": "Vital Signs Monitoring", "desc": "Regular recording of blood pressure, pulse, oxygen saturation (SpO2), body temperature, and blood glucose levels."},
            {"title": "Medication Schedule Supervision", "desc": "Ensuring doctor-prescribed medications are taken at the right doses and correct times with meals."},
            {"title": "Post-Discharge Recovery Care", "desc": "Assisting seniors with resting routines, hydration, mobility precautions, and recuperation steps."},
            {"title": "Dietary & Hydration Tracking", "desc": "Monitoring senior fluid intake and supporting nutritious, doctor-recommended meal schedules."},
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
            {"q": "How frequently are vital signs recorded?", "a": "Depending on the senior's condition, vitals can be recorded once or twice daily, or before and after medication schedules as recommended."},
            {"q": "What locations do you serve?", "a": "We serve 35+ locations in Chennai, and all over Tamil Nadu on a 24-Hour One-Day Full care basis."},
            {"q": "How quickly can senior health care support begin?", "a": "We recommend contacting us 24 to 48 hours prior to hospital discharge or required start date so we can arrange suitable personnel."}
        ],
        "related": ["elderly-care-services", "senior-citizen-care-services", "home-nurse-services"]
    },
    {
        "id": "dementia-care-for-the-elderly",
        "folder": "dementia-care-for-the-elderly",
        "title": "Compassionate Dementia Care for the Elderly in Chennai & Tamil Nadu",
        "meta_title": "Dementia Care for the Elderly Chennai | Alzheimer's Home Care | Sugam Home Care",
        "meta_desc": "Specialized dementia care for the elderly in Chennai & Tamil Nadu. Memory support, wandering safety, reassuring routines, and loving patience for Alzheimer's patients.",
        "headline": "Dementia Care for the Elderly",
        "tagline": "Specialized cognitive support, calm daily routines, reassurance, and continuous safety oversight for seniors with memory loss.",
        "icon": "🧠",
        "image": "assets/images/service-dementia.svg",
        "badge": "Specialized Memory Care",
        "who_benefits": [
            {"title": "Seniors with Alzheimer's Disease", "desc": "Specialized care addressing memory loss, disorientation, and confusion with endless patience and calm presence."},
            {"title": "Elders Prone to Wandering", "desc": "24/7 attentive supervision preventing seniors from leaving home unaccompanied or getting lost."},
            {"title": "Seniors Experiencing Sundowning", "desc": "Gentle soothing routines during late afternoons and evenings to reduce anxiety, pacing, and restlessness."},
            {"title": "Exhausted Family Caregivers", "desc": "Much-needed respite care relieving emotional and physical burnout for family members."}
        ],
        "scope": [
            {"title": "Wandering Prevention & Home Safety", "desc": "Continuous vigilance ensuring doors are secured and potential home hazards (stoves, sharp items, water) are safe."},
            {"title": "Predictable Daily Routines", "desc": "Establishing consistent morning, meal, and bedtime routines to provide emotional stability and comfort."},
            {"title": "Gentle Bathing & Grooming Assistance", "desc": "Patient, step-by-step guidance for personal hygiene, avoiding agitation through soothing, non-confrontational communication."},
            {"title": "Nutritious Eating Encouragement", "desc": "Assisting seniors who forget to eat or drink, serving easily manageable finger foods and maintaining hydration."},
            {"title": "Cognitive Engagement & Reminiscence", "desc": "Looking through old family photos, listening to favorite Carnatic music, and recalling positive cherished memories."},
            {"title": "De-Escalation & Validation", "desc": "Validating the senior's emotions rather than arguing, gently redirecting focus to calm anxiety and frustration."}
        ],
        "why_us": [
            {"title": "Trained in Dementia Communication", "desc": "Caregivers understand the psychology of memory decline, practicing validation, gentle eye contact, and patience."},
            {"title": "Home Environment Preservation", "desc": "Keeping dementia patients in their familiar home surroundings significantly reduces disorientation and distress."},
            {"title": "Tamil Nadu Wide 24-Hour Coverage", "desc": "Available across Chennai and on a 24-Hour live-in basis all over Tamil Nadu."}
        ],
        "faqs": [
            {"q": "Why is in-home care better than an institution for dementia patients?", "a": "Familiar sights, sounds, family photos, and home bedrooms provide grounding reassurance. Moving a dementia patient to an unfamiliar facility often increases agitation, confusion, and cognitive decline."},
            {"q": "How do your caregivers handle agitation or stubbornness?", "a": "We use de-escalation techniques: validating their feelings, speaking in a calm warm tone in Tamil, redirecting attention with music or a favorite drink, and never arguing."},
            {"q": "Can dementia care be arranged 24 hours a day?", "a": "Yes, 24-hour continuous oversight is strongly recommended for dementia and Alzheimer's patients to prevent nighttime wandering and falls."},
            {"q": "Do you cover locations outside Chennai?", "a": "Yes, across all districts of Tamil Nadu on a 24-Hour One-Day Full care basis."},
            {"q": "How do we get started?", "a": "Call our care team at +91 84388 61636 to discuss your family member's stage of dementia and behavioral patterns."}
        ],
        "related": ["elderly-care-services", "senior-citizen-care-services", "home-health-care-for-seniors"]
    },
    {
        "id": "home-care-for-cancer-patients",
        "folder": "home-care-for-cancer-patients",
        "title": "Compassionate Home Care for Cancer Patients in Chennai & Tamil Nadu",
        "meta_title": "Home Care for Cancer Patients Chennai | Oncology Palliative Care | Sugam Home Care",
        "meta_desc": "Compassionate home care for cancer patients in Chennai & Tamil Nadu. Post-chemotherapy recovery support, comfort positioning, nutrition tracking, and palliative care.",
        "headline": "Home Care for Cancer Patients",
        "tagline": "Supportive post-chemotherapy recovery, comfort positioning, nutritional hydration tracking, and palliative companionship.",
        "icon": "🎗️",
        "image": "assets/images/service-cancer-care.svg",
        "badge": "Supportive Oncology Care",
        "who_benefits": [
            {"title": "Patients Undergoing Chemotherapy", "desc": "Attentive bedside care managing extreme fatigue, nausea support, hydration tracking, and resting comfort."},
            {"title": "Post-Radiation Recovery Patients", "desc": "Gentle skin protection, resting posture support, and comfortable daily living assistance at home."},
            {"title": "Advanced Stage Palliative Care", "desc": "Dignified, pain-conscious comfort care, emotional presence, and peaceful home companionship."},
            {"title": "Families Needing Dedicated Support", "desc": "Experienced caregivers who shoulder daily physical care so family can focus on love and emotional strength."}
        ],
        "scope": [
            {"title": "Post-Chemotherapy Rest & Comfort", "desc": "Creating a quiet, sterile, restful environment, adjusting pillows and posture to alleviate body aches and nausea."},
            {"title": "Gentle Nutrition & Hydration Tracking", "desc": "Serving small frequent bland meals, nutrient-rich broths, coconut water, and preventing dehydration."},
            {"title": "Meticulous Infection Prevention", "desc": "Strict hygiene, clean linen, sanitized utensils, and visitor precautions to protect immunocompromised patients."},
            {"title": "Assisted Sponge Bathing & Hygiene", "desc": "Gentle, non-exhausting bed sponge baths, oral mouth rinses for mucositis, and careful skin moisturizing."},
            {"title": "Medication Timing & Prescription Reminders", "desc": "Ensuring pain management, anti-nausea, and antibiotic medications are administered on schedule per doctor's orders."},
            {"title": "Emotional & Palliative Companionship", "desc": "Compassionate listening, soothing presence, and supporting the dignity of the patient at all times."}
        ],
        "why_us": [
            {"title": "Gentle, Dignified Oncology Support", "desc": "We understand the physical and emotional roller coaster of cancer treatment and provide supportive, loving care."},
            {"title": "Avoid Hospital Infection Risks", "desc": "Resting at home protects vulnerable, low-immunity patients from hospital-acquired infections."},
            {"title": "Available Across Chennai & Tamil Nadu", "desc": "Shift care across Chennai and 24-Hour full-day service all over Tamil Nadu."}
        ],
        "faqs": [
            {"q": "Can your staff manage patients with low immunity (neutropenia)?", "a": "Yes. Our caregivers follow strict hand hygiene, mask-wearing, sanitized utensil preparation, and clean linen protocols to protect immunocompromised patients."},
            {"q": "What if the patient needs IV pain medication or saline drips?", "a": "For IV infusions, doctor-prescribed injections, or port flushes, we coordinate qualified nurses through our Nursing Services."},
            {"q": "Is 24-hour bedside care available for cancer patients?", "a": "Yes, we provide 24-hour day-and-night attendant support for continuous comfort and assistance."},
            {"q": "Do you provide oncology care outside Chennai?", "a": "Yes, we serve families across all districts of Tamil Nadu on a 24-Hour One-Day Full care basis."},
            {"q": "How do we arrange cancer home care?", "a": "Call us at +91 84388 61636 with details of your treatment phase and we will arrange experienced attendants promptly."}
        ],
        "related": ["patient-care-services", "bedridden-patient-care-services", "nursing-services"]
    },
    {
        "id": "caretaker-services-at-home",
        "folder": "caretaker-services-at-home",
        "title": "Trusted Caretaker Services at Home in Chennai & Tamil Nadu",
        "meta_title": "Caretaker Services at Home Chennai | Daily Living Assistance | Sugam Home Care",
        "meta_desc": "Trusted caretaker services at home in Chennai & Tamil Nadu. Dedicated assistance with personal grooming, mobility, feeding, medication reminders, and companionship.",
        "headline": "Caretaker Services at Home",
        "tagline": "Attentive everyday assistance with daily living, personal grooming, mobility, and companionship.",
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
            {"q": "Can caretakers administer injections or dress surgical wounds?", "a": "No. Caretakers provide non-clinical personal care and mobility assistance. For clinical procedures like injections, IV fluids, or wound dressings, please enquire for our Nursing Services."},
            {"q": "What shift options are available?", "a": "We provide 10 to 12-hour daytime assistance, 12-hour night care, and 24-hour round-the-clock live-in arrangements."},
            {"q": "How do you match a caretaker to our family?", "a": "We assess your family member's age, physical mobility, gender preference, language comfort, and required daily duties to suggest the most suitable match."},
            {"q": "Are caretaker services available across Tamil Nadu?", "a": "Yes, across all districts of Tamil Nadu on a 24-Hour One-Day Full care basis."},
            {"q": "How do we get started?", "a": "Simply call our team at +91 84388 61636 or submit the enquiry form."}
        ],
        "related": ["elderly-care-services", "patient-care-services", "senior-citizen-care-services"]
    },
    {
        "id": "home-nurse-services",
        "folder": "home-nurse-services",
        "title": "Professional Home Nurse Services in Chennai & Tamil Nadu",
        "meta_title": "Home Nurse Services Chennai | Visiting & 24/7 Nurses | Sugam Home Care",
        "meta_desc": "Professional home nurse services in Chennai & Tamil Nadu. Qualified visiting or shift-based nurses for clinical procedures, injections, wound dressings, and IV therapy.",
        "headline": "Home Nurse Services",
        "tagline": "Qualified visiting or shift-based nurses for clinical procedures, injections, wound care, and recovery supervision.",
        "icon": "👩‍⚕️",
        "image": "assets/images/service-home-nurse.svg",
        "badge": "Professional Home Nursing",
        "who_benefits": [
            {"title": "Patients Requiring Visiting Nurse Care", "desc": "Single or twice-daily nurse visits for injections, blood sugar profiling, and vitals checks."},
            {"title": "Post-Surgical Convalescence Patients", "desc": "12-hour or 24-hour nursing supervision ensuring vitals stability, drainage tube monitoring, and comfort."},
            {"title": "Elderly Patients with Complex Regimens", "desc": "Professional nurse administration of multiple subcutaneous, intramuscular, or nebulized medicines."},
            {"title": "Patients on Continuous Monitoring", "desc": "Attentive nursing care tracking SpO2, pulse, blood pressure, and alerting family to any clinical anomalies."}
        ],
        "scope": [
            {"title": "Doctor-Prescribed Injections", "desc": "Safe administration of intramuscular (IM), subcutaneous (SC), and intravenous (IV) injections."},
            {"title": "Wound Care & Sterile Dressing", "desc": "Aseptic cleaning and dressing changes for surgical incisions, bedsores, diabetic foot ulcers, and drains."},
            {"title": "IV Line Insertion & Infusion", "desc": "Peripheral IV cannula placement, maintenance, and controlled administration of prescribed IV fluids."},
            {"title": "Catheter & Bladder Care", "desc": "Urinary catheterization, bladder irrigation, catheter bag replacement, and hygiene maintenance."},
            {"title": "Clinical Health Record Maintenance", "desc": "Maintaining detailed medical charts recording vitals, fluid balance, and medication times for doctors."},
            {"title": "Nebulization & Oxygen Support", "desc": "Administering doctor-ordered nebulizer treatments and monitoring supplemental oxygen flow."}
        ],
        "why_us": [
            {"title": "Qualified & Verified Nurses", "desc": "Trained nursing personnel holding certified credentials (GNM/B.Sc Nursing) with clinical hospital experience."},
            {"title": "Strict Prescription Protocols", "desc": "All procedures and drugs are administered strictly according to valid signed prescriptions from registered doctors."},
            {"title": "Tamil Nadu Wide Service", "desc": "Visiting or shift nurses across Chennai, and 24-Hour full-day assignments all over Tamil Nadu."}
        ],
        "faqs": [
            {"q": "Do you require a doctor's prescription for home nurse visits?", "a": "Yes. A valid doctor's prescription is required for administering injections, IV fluids, wound dressings, and catheter care."},
            {"q": "Can a nurse visit just once a day for an injection or dressing?", "a": "Yes, we coordinate procedure-based single visits as well as 12-hour day/night or 24-hour continuous nursing shifts."},
            {"q": "Are your home nurses trained in hospital emergency protocols?", "a": "Our nurses are qualified in clinical procedures and basic life support, but for acute medical emergencies, patients must contact 108 or proceed to a hospital."},
            {"q": "Do you cover outside Chennai in Tamil Nadu?", "a": "Yes, across all districts of Tamil Nadu on a 24-Hour One-Day Full care basis."},
            {"q": "How can I book a home nurse?", "a": "Call us at +91 84388 61636 or send your prescription via WhatsApp for prompt nurse assignment."}
        ],
        "related": ["nursing-services", "home-health-care-for-seniors", "patient-care-services"]
    },
    {
        "id": "nursing-services",
        "folder": "nursing-services",
        "title": "Clinical Nursing Services at Home in Chennai & Tamil Nadu",
        "meta_title": "Nursing Services at Home Chennai | Clinical Nursing Procedures | Sugam Home Care",
        "meta_desc": "Qualified clinical nursing services at home in Chennai & Tamil Nadu. IV infusions, surgical wound dressings, catheterization, Ryle's tube care, and post-op care.",
        "headline": "Nursing Services",
        "tagline": "Clinical nursing procedures delivered at your doorstep under medical prescription.",
        "icon": "💉",
        "image": "assets/images/service-nursing.svg",
        "badge": "Clinical Procedures",
        "who_benefits": [
            {"title": "Patients Requiring IV Therapy", "desc": "Professional IV cannula placement, antibiotic drips, and fluid infusions in the comfort of home."},
            {"title": "Complex Surgical Wound Patients", "desc": "Sterile dressing changes for post-operative incisions, deep tissue ulcers, burns, and suture/staple removal."},
            {"title": "Patients with Urinary Catheters", "desc": "Foley's catheter insertion, replacement, and regular bladder wash administered by qualified nurses."},
            {"title": "Ryle's Tube & Tracheostomy Patients", "desc": "Supervision of nasogastric tube feeds, tube re-insertion, tracheostomy suctioning, and stoma dressing."}
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
            {"title": "Avoid Hospital Travel & Infection Risks", "desc": "Receiving clinical nursing at home eliminates painful travel for fragile patients and reduces hospital infection risks."}
        ],
        "faqs": [
            {"q": "Do I need a doctor's prescription for nursing services?", "a": "Yes, absolutely. For all clinical procedures including injections, IV infusions, wound dressings, and catheter insertion, a valid, signed prescription from your attending physician is mandatory."},
            {"q": "Can a nurse visit for single clinical procedures like an injection or dressing?", "a": "Yes, we coordinate procedure-based nurse visits (such as a single daily visit for wound dressing or antibiotic injections) as well as continuous shifts."},
            {"q": "Are emergency medical services included?", "a": "No. Our home nursing is intended for scheduled, prescribed clinical care. In case of an acute medical emergency, please call 108 or proceed to the nearest hospital emergency department."},
            {"q": "What medical consumables must the patient provide?", "a": "The patient's family should provide the prescribed medications, IV fluids, sterile dressing packets, disposable gloves, syringes, and catheters as prescribed by the doctor."},
            {"q": "How can I request a home nurse in Chennai or Tamil Nadu?", "a": "Call our team at +91 84388 61636 or submit the enquiry form with your doctor's prescription details for prompt coordination."}
        ],
        "related": ["home-nurse-services", "patient-care-services", "bedridden-patient-care-services"]
    }
]

LOCATIONS = [
    "Tambaram", "Vandalur", "Guduvanchery", "Sholinganallur", "Navalur", "OMR", "ECR", 
    "Adyar", "Velachery", "Nanganallur", "Madipakkam", "Pallavaram", "Chromepet", 
    "Alandur", "Guindy", "Adambakkam", "Taramani", "Nungambakkam", "Kodambakkam", 
    "Chetpet", "Egmore", "Thousand Lights", "Royapettah", "Anna Nagar", "Mogappair", 
    "Ambattur", "Avadi", "Porur", "Iyyappanthangal", "Ayanavaram", "Royapuram", 
    "Purasawalkam", "Panaiyur", "Thoraipakkam", "Perungudi", "T. Nagar", "Ashok Nagar"
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
        </div>'''

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
        </div>'''

    # Why us cards
    why_html = ""
    for idx, w in enumerate(svc["why_us"], 1):
        why_html += f'''
        <div class="benefit-item">
          <div class="benefit-number">0{idx}</div>
          <h3>{w["title"]}</h3>
          <p>{w["desc"]}</p>
        </div>'''

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
        </div>'''
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
            </article>'''

    # Location pills
    loc_pills_html = ""
    for loc in LOCATIONS:
        loc_pills_html += f'<span class="area-pill">{loc}</span>\n                '

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
        "areaServed": ["Chennai", "Tamil Nadu"],
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
            {svc["badge"]} • Chennai &amp; Tamil Nadu
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
              <p class="enquiry-card-subtitle">Connect with our care coordinator to discuss requirements and availability in Chennai or Tamil Nadu.</p>
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
        <span class="badge-tag">Simple &amp; Transparent</span>
        <h2>How the Service Arrangement Process Works</h2>
        <p class="section-subtitle">Four straightforward steps to arrange dependable home care support for your family.</p>
      </div>

      <div class="steps-grid">
        <div class="step-card">
          <div class="step-badge">1</div>
          <h3>Tell Us Your Needs</h3>
          <p>Submit the enquiry form or call our coordinator with your preferred timings and location in Chennai or Tamil Nadu.</p>
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
        <span class="badge-tag">Benefits &amp; Value</span>
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

  <!-- SERVICE COVERAGE LOCATIONS & TAMIL NADU NOTICE -->
  <section class="section">
    <div class="container">
      <div class="section-header">
        <span class="badge-tag">Where We Serve</span>
        <h2>Coverage for {svc["headline"]}</h2>
        <p class="section-subtitle">Available across 35+ major Chennai localities and all over Tamil Nadu.</p>
      </div>

      <div style="background: var(--bg-warm); border: 1px solid var(--border-light); border-radius: var(--radius-xl); padding: 2rem;">
        <div style="background: linear-gradient(135deg, #0F2C59 0%, #163E7D 100%); color: #FFFFFF; border-radius: var(--radius-md); padding: 1.25rem; margin-bottom: 1.5rem;">
          <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.35rem;">
            <span style="font-size:1.25rem;">🚩</span>
            <strong style="color:#2DD4BF; font-size:1rem;">All Over Tamil Nadu Service Availability:</strong>
          </div>
          <p style="color:#E2E8F0; font-size:0.875rem; line-height:1.5; margin-bottom:0;">
            Outside our primary Chennai localities, {svc["headline"]} is provided across all districts of Tamil Nadu on a <strong>One-Day Full (24-Hour)</strong> basis.
          </p>
        </div>

        <h4 style="color:var(--color-primary); margin-bottom:0.75rem;">Primary Chennai Coverage Areas:</h4>
        <div class="service-areas-pills">
          {loc_pills_html}
        </div>
      </div>
    </div>
  </section>

  <!-- 10. RELATED SERVICES -->
  <section class="section section-bg-surface">
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
        Speak directly with our team to discuss timings, availability, and specific care preferences in Chennai or Tamil Nadu.
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

def generate_all_services():
    for s in SERVICES:
        generate_service_page(s)
    print("All 11 service landing pages generated successfully!")

if __name__ == "__main__":
    generate_all_services()
