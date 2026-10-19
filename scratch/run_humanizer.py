with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

replacements = [
    # 1. Marquee en-dashes
    ("NATIONWIDE IN 2–4 DAYS", "NATIONWIDE IN 2 TO 4 DAYS"),
    
    # 2. Section edge outline text: replace em-dashes with middle dots / bullets or clean spaced words
    ("<span>Anatomy — Anatomy — Anatomy</span>", "<span>Anatomy • Anatomy • Anatomy</span>"),
    ("<span>Three fits — Three fits — Three fits</span>", "<span>Three fits • Three fits • Three fits</span>"),
    ("<span>Choose your set — Choose your set — Choose your set</span>", "<span>Choose your set • Choose your set • Choose your set</span>"),
    ("<span>Up close — Up close — Up close</span>", "<span>Up close • Up close • Up close</span>"),
    
    # 3. Story text §12: remove "matches modern car interiors" and "plastic rattle" triad
    ("<p>Solid wood body with a metal collar that matches modern car interiors.</p>",
     "<p>Turned wood body with an aluminum collar sized to sit steadily inside vehicle cup holders.</p>"),
    
    ("<p>The top opening drops ash and cigarette ends directly into the canister, so wind won't blow them around.</p>",
     "<p>Ash and cigarette ends drop directly into the metal canister, preventing wind from blowing them across the cabin.</p>"),
     
    ("<h2>Real wood.<br>Threaded metal.<br>No plastic rattle.</h2><p>Turned wood sleeve with a metal inner core that unscrews easily for emptying.</p>",
     "<h2>Turned wood sleeve.<br>Threaded metal core.</h2><p>The wood outer shell unscrews smoothly from the internal chamber when you need to empty ash.</p>"),
     
    # 4. Lifestyle banners: replace triad and passive phrasing
    ("<h3>Includes all three silicone gaskets and cleaning accessories.</h3>",
     "<h3>Comes with three silicone adapters and cleaning accessories.</h3>"),
     
    # 5. Why-it-works §1: "rather than an open plastic ashtray" is a classic Not X But Y (§1)
    ("<p>Crafted with real turned wood and brushed aluminum metal, it blends seamlessly into modern leather and wood interior trim like a piece of crafted woodwork rather than an open plastic ashtray.</p>",
     "<p>Built with turned wood and brushed aluminum to match vehicle interiors, keeping cigarettes and ash out of sight while you drive.</p>"),
     
    ("<p>The sealed cylinder design catches falling ash immediately through the top opening. Even with car windows rolled down or air conditioning on high, wind cannot reach inside to scatter ashes onto your seats, floor, or clothes.</p>",
     "<p>The top opening directs falling ash straight into the inner chamber. Even with open windows or active air conditioning, ash stays contained inside.</p>"),
     
    ("<p>Simply slide the cigarette into the canister. The inner chamber holds the butts safely away from view and traps lingering smoke and odor until you are ready to unscrew and empty it into a trash bin.</p>",
     "<p>Slide the cigarette into the silicone collar. The chamber holds butts securely and limits smoke and odor until you empty it.</p>"),
     
    ("<p>Yes. The compact cylindrical body is engineered specifically to slide smoothly into standard vehicle cup holders, door pockets, center consoles, or backpacks without rolling or wobbling.</p>",
     "<p>Yes. The cylinder fits into standard car cup holders, door pockets, center consoles, and travel bags.</p>"),
     
    # 6. Pricing subtitle: remove vertical bar
    ('<p class="ship c"><em class="dot"></em>Free Delivery <span>| Arrives in 2 to 4 days</span></p>',
     '<p class="ship c"><em class="dot"></em>Free Delivery <span>• Arrives in 2 to 4 days</span></p>'),
     
    # 7. FAQ multi-finish answer: align with new interactive stepper feature
    ("<details><summary>Can I order multiple pieces with different finishes?</summary><p>Yes. Select 2 or 3 pieces in the order form, and let us know on WhatsApp if you want a mix of Walnut and Beech.</p></details>",
     "<details><summary>Can I order multiple pieces with different finishes?</summary><p>Yes. When you choose 2 or 3 pieces, the order form lets you pick the exact combination of Walnut and Beech you want.</p></details>"),
     
    # 8. Order section text: clean and direct
    ('<p class="muted"><span class="ofin">Finish: <b id="ofin">Walnut</b>, </span>fill in your delivery details below. Choose Cash on Delivery or Whish Pay. We confirm every order with you on WhatsApp before shipping.</p>',
     '<p class="muted"><span class="ofin">Finish: <b id="ofin">Walnut</b>. </span>Enter your delivery details below. You can pay with Cash on Delivery or Whish Pay. We confirm your address on WhatsApp before dispatch.</p>'),
     
    # 9. Whish note: clear, active instruction
    ('<b>Whish Money transfer:</b> After clicking place order, our Whish account details will be sent directly to your WhatsApp to complete the transfer before dispatch.',
     '<b>Whish Money transfer:</b> After you submit your order, we send our Whish account details directly on WhatsApp so you can complete the transfer before dispatch.')
]

for old, new in replacements:
    if old in html:
        html = html.replace(old, new)
        print(f"Replaced: {old[:30]}...")
    else:
        print(f"NOT FOUND: {old[:30]}...")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("nova-mart-aone.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Humanization completed on index.html and nova-mart-aone.html!")
