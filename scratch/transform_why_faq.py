import re

for filename in ['index.html', 'nova-mart-aone.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    # Old why section:
    # <section class="why"><div class="edge" aria-hidden="true"><span>Why it works — Why it works — Why it works</span></div><div class="wrap">
    # <ul class="why-l">
    # <li><h3>Stops flying ash<br><em>from landing on upholstery.</em></h3></li>
    # ...
    # </ul></div></section>

    # Replacement: Clean FAQ-style accordion layout with title and expanding details
    new_why_section = """<section class="why" id="why"><div class="wrap faq-in">
<h2 class="lines"><span><i>Why it</i></span><span><i class="cu">works.</i></span></h2>
<div class="why-faq">
<details open><summary>How does it stop ash from flying around the car?</summary><p>The sealed cylinder design catches falling ash immediately through the top opening. Even with car windows rolled down or air conditioning on high, wind cannot reach inside to scatter ashes onto your seats, floor, or clothes.</p></details>
<details><summary>Where do cigarette butts go while driving?</summary><p>Simply slide the cigarette into the canister. The inner chamber holds the butts safely away from view and traps lingering smoke and odor until you are ready to unscrew and empty it into a trash bin.</p></details>
<details><summary>Does it fit standard car cup holders and bags?</summary><p>Yes. The compact cylindrical body is engineered specifically to slide smoothly into standard vehicle cup holders, door pockets, center consoles, or backpacks without rolling or wobbling.</p></details>
<details><summary>How does the natural wood construction look in a modern car?</summary><p>Crafted with real turned wood and brushed aluminum metal, it blends seamlessly into modern leather and wood interior trim like a piece of crafted woodwork rather than an open plastic ashtray.</p></details>
</div></div></section>"""

    # Replace the section
    text = re.sub(r'<section class=["\']why["\'].*?<\/section>', new_why_section, text, flags=re.DOTALL)

    # Clean GSAP animation line if referencing .why-l
    text = text.replace("gsap.from('.why-l h3', { xPercent: -4, opacity: 0, duration: 1, stagger: .12, ease: E,",
                        "gsap.from('.why-faq details', { y: 20, opacity: 0, duration: .8, stagger: .08, ease: E,")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"Transformed Why section into clean FAQ layout in {filename}.")
