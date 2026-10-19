import re

for filename in ['index.html', 'nova-mart-aone.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Update the Marquee ticker to include Cash on Delivery and Whish Pay
    old_ticker_item = '<b>FREE DELIVERY</b><span>CASH & WHATSAPP CONFIRMATION</span>'
    new_ticker_item = '<b>PAYMENT OPTIONS</b><span>CASH ON DELIVERY OR WHISH MONEY</span>'
    text = text.replace(old_ticker_item, new_ticker_item)

    # 2. Add payment method selector in the order form right below Finish
    # Old Finish fieldset:
    # <fieldset class="qty fin"><legend>Finish</legend>
    # <label><input type="radio" name="finish" value="Walnut" checked><span><i class="sw-dot w"></i>Walnut</span></label>
    # <label><input type="radio" name="finish" value="Beech"><span><i class="sw-dot b"></i>Beech</span></label></fieldset>
    old_finish_fieldset = '<fieldset class="qty fin"><legend>Finish</legend>\n<label><input type="radio" name="finish" value="Walnut" checked><span><i class="sw-dot w"></i>Walnut</span></label>\n<label><input type="radio" name="finish" value="Beech"><span><i class="sw-dot b"></i>Beech</span></label></fieldset>'

    payment_fieldset = '''<fieldset class="qty fin"><legend>Finish</legend>
<label><input type="radio" name="finish" value="Walnut" checked><span><i class="sw-dot w"></i>Walnut</span></label>
<label><input type="radio" name="finish" value="Beech"><span><i class="sw-dot b"></i>Beech</span></label></fieldset>

<fieldset class="qty fin pay-opts"><legend>Payment Method</legend>
<label><input type="radio" name="payment" value="Cash on Delivery" checked><span><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-right:8px;vertical-align:middle"><rect x="2" y="5" width="20" height="14" rx="2"/><line x1="2" y1="10" x2="22" y2="10"/></svg>Cash on Delivery</span></label>
<label><input type="radio" name="payment" value="Whish Pay" id="pay-whish"><span><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" style="margin-right:8px;vertical-align:middle;color:#d92d20"><circle cx="12" cy="12" r="10"/><path d="M7 12l3 3 7-7" stroke="#fff" stroke-width="2.5" fill="none"/></svg>Whish Pay</span></label></fieldset>
<div class="whish-note" id="whish-note" style="display:none;background:#fbf3e6;border:1px solid #ebd2b0;border-radius:4px;padding:12px 14px;margin-bottom:18px;font-size:13px;line-height:1.45;color:#5a3f25">
  <b>Whish Money transfer:</b> After clicking place order, our Whish account details will be sent directly to your WhatsApp to complete the transfer before dispatch.
</div>'''

    text = text.replace(old_finish_fieldset, payment_fieldset)

    # 3. Update the JavaScript msg() generator and form change listener
    old_msg = "const m = `Hello Nova Mart,\\nI would like to order the portable ashtray.\\n\\nName: ${d.name}\\nPhone: ${d.phone}\\nAddress: ${d.address}\\nQuantity: ${q}\\nFinish: ${form.querySelector('input[name=finish]:checked').value}`;"
    new_msg = "const pay = form.querySelector('input[name=payment]:checked')?.value || 'Cash on Delivery';\n    const m = `Hello Nova Mart,\\nI would like to order the portable ashtray.\\n\\nName: ${d.name}\\nPhone: ${d.phone}\\nAddress: ${d.address}\\nQuantity: ${q}\\nFinish: ${form.querySelector('input[name=finish]:checked').value}\\nPayment: ${pay}`;"
    text = text.replace(old_msg, new_msg)

    # In form change listener: toggle whish-note
    old_change = "form.addEventListener('change', e => { if (e.target.name === 'finish') setF(e.target.value.toLowerCase()); else sync(); });"
    new_change = """form.addEventListener('change', e => {
    if (e.target.name === 'finish') setF(e.target.value.toLowerCase());
    else if (e.target.name === 'payment') {
      const isWhish = e.target.value === 'Whish Pay';
      const wn = $('#whish-note'); if (wn) wn.style.display = isWhish ? 'block' : 'none';
      sync();
    } else sync();
  });"""
    text = text.replace(old_change, new_change)

    # 4. Also add a question in the FAQ about payment methods:
    old_faq_item = "<details><summary>Are there any delivery charges?</summary><p>No. Delivery is completely free whether you order one piece or three.</p></details>"
    new_faq_item = """<details><summary>What payment methods do you accept?</summary><p>You can pay Cash on Delivery when you receive your package, or pay digitally through Whish Pay (Whish Money). Select your preferred option at checkout.</p></details>
<details><summary>Are there any delivery charges?</summary><p>No. Delivery is completely free whether you order one piece or three.</p></details>"""
    text = text.replace(old_faq_item, new_faq_item)

    # 5. In Order Left column text:
    old_order_text = "fill in your delivery details below. We confirm every order with you on WhatsApp before shipping. Delivery takes 2 to 4 days."
    new_order_text = "fill in your delivery details below. Choose Cash on Delivery or Whish Pay. We confirm every order with you on WhatsApp before shipping."
    text = text.replace(old_order_text, new_order_text)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"Added Cash on Delivery and Whish Pay to {filename}.")
