import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect line by line and replace cleanly
replacements = [
    (
        'Nova Mart Aone — Portable Wood &amp; Metal Car Ashtray | Free Delivery',
        'Nova Mart Aone: Portable Wood and Metal Car Ashtray with Free Delivery'
    ),
    (
        'A compact portable ashtray with a premium wood-and-metal finish. 1 piece $11, 2 pieces $18, 3 pieces $24. Free delivery in 2–4 days.',
        'Compact car ashtray in wood and metal. 1 piece for $11, 2 for $18, 3 for $24. Free delivery in 2 to 4 days.'
    ),
    (
        'Regular · Medium · Slim',
        'Regular, Medium, and Slim'
    ),
    (
        '<p class="eyebrow">Nova Mart Aone<span class="lg">&nbsp;· Portable Car Ashtray</span></p>',
        '<p class="eyebrow">Nova Mart Aone<span class="lg">&nbsp;|&nbsp;Car Ashtray</span></p>'
    ),
    (
        '<span><i>Keep your car</i></span><span><i>cleaner.</i></span><span><i class="cu">Look better.</i></span>',
        '<span><i>Keep ash off</i></span><span><i>your seats</i></span><span><i class="cu">and console.</i></span>'
    ),
    (
        '<p class="lede">A compact portable ashtray designed to keep ash and cigarette waste contained — with a premium wood-and-metal finish that looks at home in any car.</p>',
        '<p class="lede">A pocket-sized cylinder that holds cigarette ash and butts while you drive, finished in real wood and brushed metal.</p>'
    ),
    (
        '<p class="ship"><em class="dot"></em>Free Delivery <span>· Delivery in 2–4 days</span></p>',
        '<p class="ship"><em class="dot"></em>Free Delivery <span>| Arrives in 2 to 4 days</span></p>'
    ),
    (
        '<p class="ship c"><em class="dot"></em>Free Delivery <span>· Delivery: 2–4 Days</span></p>',
        '<p class="ship c"><em class="dot"></em>Free Delivery <span>| Arrives in 2 to 4 days</span></p>'
    ),
    (
        '<h2>Built to belong<br>in your car.</h2><p>Compact, cylindrical, finished in real wood tones with a metal collar.</p>',
        '<h2>Sits right<br>in your cup holder.</h2><p>Solid wood body with a metal collar that matches modern car interiors.</p>'
    ),
    (
        '<h2>Ash stays<br>here.</h2><p>The opening keeps ash and cigarette waste contained inside the body.</p>',
        '<h2>Traps ash<br>inside.</h2><p>The top opening drops ash and cigarette ends directly into the canister, so wind won\'t blow them around.</p>'
    ),
    (
        '<h2>Three tip<br>sizes.</h2><p>Regular, Medium and Slim inserts — swap to fit your cigarette.</p>',
        '<h2>Three tip<br>adapters.</h2><p>Comes with silicone inserts for standard, medium, and slim cigarettes.</p>'
    ),
    (
        '<h2>Made to<br>travel.</h2><p>Small enough for a cup holder, door pocket or bag.</p>',
        '<h2>Easy to<br>carry along.</h2><p>Drop it into a door pocket, cup slot, or your jacket pocket when you step out.</p>'
    ),
    (
        '<h2>Wood.<br>Metal.<br>Clean design.</h2><p>Natural grain, machined metal detailing, black inserts.</p>',
        '<h2>Real wood.<br>Threaded metal.<br>No plastic rattle.</h2><p>Turned wood sleeve with a metal inner core that unscrews easily for emptying.</p>'
    ),
    (
        '<span>Anatomy · Anatomy · Anatomy</span>',
        '<span>Anatomy / Specs / Anatomy</span>'
    ),
    (
        '<span><i>Every part</i></span><span><i>has a job.</i></span>',
        '<span><i>How it is</i></span><span><i>put together.</i></span>'
    ),
    (
        '<span>Three fits · Three fits · Three fits</span>',
        '<span>Three Sizes / Universal Fit</span>'
    ),
    (
        '<span><i>One design.</i></span><span><i class="cu">Three fits.</i></span>',
        '<span><i>Fits whatever</i></span><span><i class="cu">you smoke.</i></span>'
    ),
    (
        '<p class="muted">Pick the insert that matches your cigarette and press it into the collar.</p>',
        '<p class="muted">Press the matching silicone collar into the top opening so your cigarette seals firmly while smoking.</p>'
    ),
    (
        '<h3>Fits your grip.<br>Fits your routine.</h3>',
        '<h3>Easy to hold while driving.</h3>'
    ),
    (
        '<h3>Ash goes in.<br>Not on the floor.</h3>',
        '<h3>Catches falling ash so your car floor stays clean.</h3>'
    ),
    (
        '<h3>Comes with<br>its accessories.</h3>',
        '<h3>Includes all three silicone gaskets and cleaning accessories.</h3>'
    ),
    (
        '<span>Why it works · Why it works · Why it works</span>',
        '<span>Daily Use / Practical Details</span>'
    ),
    (
        '<h3>Less ash<br><em>inside the car.</em></h3>',
        '<h3>Stops flying ash<br><em>from landing on upholstery.</em></h3>'
    ),
    (
        '<h3>One place<br><em>for cigarette waste.</em></h3>',
        '<h3>Holds butts safely<br><em>until you find a trash bin.</em></h3>'
    ),
    (
        '<h3>Compact<br><em>and portable.</em></h3>',
        '<h3>Slips into a cup holder<br><em>or backpack with ease.</em></h3>'
    ),
    (
        '<h3>Designed<br><em>to look good.</em></h3>',
        '<h3>Looks like clean woodwork,<br><em>not an open garbage tray.</em></h3>'
    ),
    (
        '<span>Choose your set · Choose your set · Choose your set</span>',
        '<span>Order Packs / Free Shipping</span>'
    ),
    (
        '<p class="muted"><span class="ofin">Finish: <b id="ofin">Walnut</b> · </span>Fill in your details — we confirm every order with you on WhatsApp. Free delivery in 2–4 days.</p>',
        '<p class="muted"><span class="ofin">Finish: <b id="ofin">Walnut</b>, </span>fill in your delivery details below. We confirm every order with you on WhatsApp before shipping. Delivery takes 2 to 4 days.</p>'
    ),
    (
        '<span>1 · $11</span>',
        '<span>1 piece ($11)</span>'
    ),
    (
        '<span>2 · $18</span>',
        '<span>2 pieces ($18)</span>'
    ),
    (
        '<span>3 · $24</span>',
        '<span>3 pieces ($24)</span>'
    ),
    (
        '<span>Up close · Up close · Up close</span>',
        '<span>Photo Gallery / Up Close</span>'
    ),
    (
        '<summary>What sizes are available?</summary><p>Regular, Medium and Slim tip sizes.</p>',
        '<summary>What cigarette sizes fit this ashtray?</summary><p>Every order includes three interchangeable silicone collars: 7.8 mm for regular cigarettes, 6.7 mm for medium brands, and 5.2 mm for slim cigarettes.</p>'
    ),
    (
        '<summary>How long does delivery take?</summary><p>2–4 days.</p>',
        '<summary>How long does delivery take?</summary><p>Orders arrive in 2 to 4 business days anywhere across the country.</p>'
    ),
    (
        '<summary>Is delivery free?</summary><p>Yes.</p>',
        '<summary>Are there any delivery charges?</summary><p>No. Delivery is completely free whether you order one piece or three.</p>'
    ),
    (
        '<summary>How do I order?</summary><p>Order directly through the site or WhatsApp.</p>',
        '<summary>How does checkout work?</summary><p>Submit the short form above or message us directly on WhatsApp. We message you back to confirm your address before sending your package.</p>'
    ),
    (
        '<summary>How many pieces can I order?</summary><p>The current offers are for 1, 2 or 3 pieces.</p>',
        '<summary>Can I order multiple pieces with different finishes?</summary><p>Yes. Select 2 or 3 pieces in the order form, and let us know on WhatsApp if you want a mix of Walnut and Beech.</p>'
    ),
    (
        '<ul><li>Free Delivery</li><li>Delivery: 2–4 Days</li></ul>',
        '<ul><li>Free Delivery</li><li>Arrives in 2 to 4 business days</li></ul>'
    )
]

applied = 0
for src, dst in replacements:
    if src in text:
        text = text.replace(src, dst)
        applied += 1
    else:
        # Check without non-standard unicode characters
        print("Note: didn't match exact substring:", src[:35])

print(f"Total replacements applied: {applied} / {len(replacements)}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

with open('nova-mart-aone.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated index.html and nova-mart-aone.html successfully.")
