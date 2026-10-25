#!/usr/bin/env python3
import os
import re

ROOT_DIR = "/Users/karthik/.gemini/antigravity/scratch/sugam-home-care"

REQUIRED_PAGES = [
    "index.html",
    "about-us/index.html",
    "contact-us/index.html",
    "services/index.html",
    "maid-services/index.html",
    "home-health-care-services/index.html",
    "caretaker-services/index.html",
    "baby-care-taker/index.html",
    "elderly-care-services/index.html",
    "patient-care-services/index.html",
    "nursing-services-at-home/index.html",
    "privacy-policy/index.html",
    "terms-and-conditions/index.html",
    "thank-you/index.html"
]

FORBIDDEN_PATTERNS = [
    r"\b15\+?\s*years\b",
    r"\b10\+?\s*years\b",
    r"\b5000\+?\s*clients\b",
    r"\b1000\+?\s*families\b",
    r"\b100%\s*cure\b",
    r"\baward[\s-]?winning\s*hospital\b",
    r"\bcertified\s*doctors\s*on\s*call\b"
]

all_passed = True

print("=== CHECKING PAGE EXISTENCE & INTEGRITY ===")
for page in REQUIRED_PAGES:
    path = os.path.join(ROOT_DIR, page)
    if not os.path.exists(path):
        print(f"❌ MISSING: {page}")
        all_passed = False
        continue
    
    size = os.path.getsize(path)
    if size < 500:
        print(f"❌ TOO SMALL ({size} bytes): {page}")
        all_passed = False
        continue
    
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Title check
    if "<title>" not in content:
        print(f"❌ MISSING <title> in {page}")
        all_passed = False

    # Meta description check
    if 'name="description"' not in content:
        print(f"❌ MISSING meta description in {page}")
        all_passed = False

    # Viewport check
    if 'name="viewport"' not in content:
        print(f"❌ MISSING viewport meta tag in {page}")
        all_passed = False

    # Canonical link check
    if 'rel="canonical"' not in content:
        print(f"❌ MISSING canonical link in {page}")
        all_passed = False

    # Check for forbidden fabricated claims
    for pat in FORBIDDEN_PATTERNS:
        match = re.search(pat, content, re.IGNORECASE)
        if match:
            print(f"⚠️ FORBIDDEN FABRICATED PATTERN MATCHED '{match.group(0)}' in {page}")
            all_passed = False

    print(f"✓ Validated: {page} ({size} bytes)")

print("\n=== CHECKING ASSETS ===")
assets = [
    "assets/css/style.css",
    "assets/css/components.css",
    "assets/js/config.js",
    "assets/js/main.js",
    "assets/js/form.js",
    "assets/images/logo.svg",
    "assets/images/favicon.svg",
    "assets/images/hero-home.svg",
    "assets/images/service-maid.svg",
    "assets/images/service-home-health.svg",
    "assets/images/service-caretaker.svg",
    "assets/images/service-baby-care.svg",
    "assets/images/service-elderly-care.svg",
    "assets/images/service-patient-care.svg",
    "assets/images/service-nursing.svg",
    "sitemap.xml",
    "robots.txt"
]

for a in assets:
    p = os.path.join(ROOT_DIR, a)
    if not os.path.exists(p):
        print(f"❌ MISSING ASSET: {a}")
        all_passed = False
    else:
        print(f"✓ Found asset: {a} ({os.path.getsize(p)} bytes)")

if all_passed:
    print("\n🎉 ALL CHECKS PASSED PERFECTLY!")
else:
    print("\n⚠️ SOME CHECKS FAILED. Please review output above.")
