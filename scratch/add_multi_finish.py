with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update HTML in form: Replace static finish radios with dynamic finish selection
old_form_finish_html = """<fieldset class="qty fin"><legend>Finish</legend>
<label><input type="radio" name="finish" value="Walnut" checked><span><i class="sw-dot w"></i>Walnut</span></label>
<label><input type="radio" name="finish" value="Beech"><span><i class="sw-dot b"></i>Beech</span></label></fieldset>"""

new_form_finish_html = """<!-- 1 piece single finish selection -->
<fieldset class="qty fin" id="fin-single"><legend>Finish</legend>
<label><input type="radio" name="finish" value="Walnut" checked><span><i class="sw-dot w"></i>Walnut</span></label>
<label><input type="radio" name="finish" value="Beech"><span><i class="sw-dot b"></i>Beech</span></label></fieldset>

<!-- Multi-piece custom mix selection (for 2 or 3 pieces) -->
<div class="fin-multi" id="fin-multi" style="display:none">
  <div class="fin-multi-head">
    <label class="fin-legend">Select Finishes (<span id="fin-count-needed">2</span> Pieces)</label>
    <small class="fin-sub">Customize your mix of Walnut and Beech:</small>
  </div>
  <div class="fin-rows">
    <div class="fin-row">
      <div class="fin-info"><i class="sw-dot w"></i><b>Walnut</b><span>Deep natural wood</span></div>
      <div class="stepper" data-finish="walnut">
        <button type="button" class="step-btn minus" aria-label="Decrease Walnut">&minus;</button>
        <span class="step-val" id="val-walnut">1</span>
        <button type="button" class="step-btn plus" aria-label="Increase Walnut">+</button>
      </div>
    </div>
    <div class="fin-row">
      <div class="fin-info"><i class="sw-dot b"></i><b>Beech</b><span>Warm golden wood</span></div>
      <div class="stepper" data-finish="beech">
        <button type="button" class="step-btn minus" aria-label="Decrease Beech">&minus;</button>
        <span class="step-val" id="val-beech">1</span>
        <button type="button" class="step-btn plus" aria-label="Increase Beech">+</button>
      </div>
    </div>
  </div>
  <div class="fin-summary" id="fin-summary">
    <b>Selected:</b> <span id="fin-summary-text">1 Walnut + 1 Beech</span>
  </div>
</div>"""

assert old_form_finish_html in html, "Could not find old_form_finish_html"
html = html.replace(old_form_finish_html, new_form_finish_html)

# 2. Add CSS styles for the stepper and multi-finish controls
multi_finish_css = """
/* Multi-piece finish customizer */
.fin-multi {
  background: #faf8f5;
  border: 1px solid var(--line);
  border-radius: 4px;
  padding: 18px 20px;
  margin-bottom: 22px;
}
.fin-multi-head {
  margin-bottom: 14px;
}
.fin-legend {
  display: block;
  font: 700 12px/1 var(--f);
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--cu);
  margin-bottom: 4px;
}
.fin-sub {
  color: var(--mu);
  font-size: 13px;
}
.fin-rows {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.fin-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: #fff;
  border: 1px solid rgba(50,40,30,.15);
  padding: 12px 16px;
  border-radius: 3px;
  transition: border-color .25s, box-shadow .25s;
}
.fin-row:hover {
  border-color: var(--cu);
}
.fin-info {
  display: flex;
  align-items: center;
  gap: 12px;
}
.fin-info b {
  font: 700 15px/1 var(--f);
  color: var(--ow);
}
.fin-info span {
  font-size: 13px;
  color: var(--mu);
}
.stepper {
  display: inline-flex;
  align-items: center;
  gap: 2px;
  background: #f2ede4;
  border: 1px solid rgba(50,40,30,.18);
  border-radius: 3px;
  padding: 3px;
}
.step-btn {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #fff;
  border: 1px solid rgba(50,40,30,.15);
  border-radius: 2px;
  font-size: 18px;
  font-weight: 700;
  color: var(--ow);
  cursor: pointer;
  user-select: none;
  transition: all .2s;
}
.step-btn:hover:not(:disabled) {
  background: var(--cu);
  color: #fff;
  border-color: var(--cu);
}
.step-btn:disabled {
  opacity: .35;
  cursor: not-allowed;
}
.step-val {
  min-width: 36px;
  text-align: center;
  font: 700 16px/1 var(--fn);
  color: var(--cp);
}
.fin-summary {
  margin-top: 14px;
  padding-top: 12px;
  border-top: 1px dashed rgba(50,40,30,.18);
  font-size: 13px;
  color: var(--mu);
}
.fin-summary b {
  color: var(--ow);
}
.fin-summary span {
  color: var(--cu);
  font-weight: 700;
}
"""

html = html.replace("</style></head>", multi_finish_css + "\n</style></head>")

# 3. Update JavaScript logic for handling multi-piece custom mixes
old_js_block = """  // quantity / pricing sync
  const form = $('#form'), total = $('#total'), err = $('#err');
  // finish: hero toggle <-> form <-> storage
  const setF = (f, save = true) => {
    f = f === 'beech' ? 'beech' : 'walnut'; const F = f[0].toUpperCase() + f.slice(1);
    document.body.dataset.f = f;
    $$('.sw button').forEach(b => b.setAttribute('aria-checked', b.dataset.f === f));
    $('#fw').textContent = F; $('#ofin').textContent = F; $$('.fn').forEach(e => e.textContent = F + ' finish');
    const r = $(`input[name=finish][value=${F}]`); if (r) r.checked = true;
    if (save) try { localStorage.setItem('nm-finish', f) } catch (e) {}
    if (typeof sync === 'function' && form) sync();
  };
  $$('.sw button').forEach(b => b.addEventListener('click', () => setF(b.dataset.f)));
  const qty = () => +form.querySelector('input[name=qty]:checked').value;
  const msg = (d) => {
    const q = qty();
    d = d || {name:'',phone:'',address:''};
    const pay = form.querySelector('input[name=payment]:checked')?.value || 'Cash on Delivery';
    const m = `Hello Nova Mart,\\nI would like to order the portable ashtray.\\n\\nName: ${d.name}\\nPhone: ${d.phone}\\nAddress: ${d.address}\\nQuantity: ${q}\\nFinish: ${form.querySelector('input[name=finish]:checked').value}\\nPayment: ${pay}`;
    return `https://wa.me/${WA}?text=${encodeURIComponent(m)}`;
  };
  const sync = () => {
    const q = qty(); total.textContent = '$' + PRICES[q];
    $$('.plan').forEach(p => p.classList.toggle('on', +p.dataset.q === q));
    const d = Object.fromEntries(['name', 'phone', 'address'].map(k => [k, form[k].value.trim()]));
    $('#wa-order').href = msg(d.name || d.phone || d.address ? d : null);
  };"""

new_js_block = """  // quantity / pricing sync
  const form = $('#form'), total = $('#total'), err = $('#err');
  
  // Custom multi-finish state: tracks quantities of Walnut & Beech
  const finCounts = { walnut: 1, beech: 1 };

  const getFinishText = () => {
    const q = qty();
    if (q === 1) {
      const radio = form.querySelector('input[name=finish]:checked');
      return radio ? radio.value : 'Walnut';
    }
    const parts = [];
    if (finCounts.walnut > 0) parts.push(`${finCounts.walnut} Walnut`);
    if (finCounts.beech > 0) parts.push(`${finCounts.beech} Beech`);
    return parts.join(' + ');
  };

  const updateFinishUI = () => {
    const q = qty();
    const singleBox = $('#fin-single');
    const multiBox = $('#fin-multi');
    const ofin = $('#ofin');
    
    if (q === 1) {
      if (singleBox) singleBox.style.display = 'grid';
      if (multiBox) multiBox.style.display = 'none';
      const f = form.querySelector('input[name=finish]:checked')?.value || 'Walnut';
      if (ofin) ofin.textContent = f;
    } else {
      if (singleBox) singleBox.style.display = 'none';
      if (multiBox) multiBox.style.display = 'block';
      
      // Ensure sum equals q
      const totalSelected = finCounts.walnut + finCounts.beech;
      if (totalSelected !== q) {
        if (q === 2) { finCounts.walnut = 1; finCounts.beech = 1; }
        else if (q === 3) { finCounts.walnut = 2; finCounts.beech = 1; }
      }
      
      const countNeeded = $('#fin-count-needed');
      if (countNeeded) countNeeded.textContent = q;
      
      const valW = $('#val-walnut'), valB = $('#val-beech');
      if (valW) valW.textContent = finCounts.walnut;
      if (valB) valB.textContent = finCounts.beech;
      
      // Update minus/plus disabled states
      const minusW = $('.stepper[data-finish=walnut] .minus');
      const plusW = $('.stepper[data-finish=walnut] .plus');
      const minusB = $('.stepper[data-finish=beech] .minus');
      const plusB = $('.stepper[data-finish=beech] .plus');
      
      if (minusW) minusW.disabled = finCounts.walnut <= 0;
      if (plusW) plusW.disabled = finCounts.walnut >= q;
      if (minusB) minusB.disabled = finCounts.beech <= 0;
      if (plusB) plusB.disabled = finCounts.beech >= q;
      
      const summaryText = $('#fin-summary-text');
      const finishDesc = getFinishText();
      if (summaryText) summaryText.textContent = finishDesc;
      if (ofin) ofin.textContent = finishDesc;
    }
  };

  // Stepper handlers for Walnut & Beech mix
  $$('.step-btn').forEach(btn => {
    btn.addEventListener('click', e => {
      e.preventDefault();
      const stepper = btn.closest('.stepper');
      const targetFinish = stepper.dataset.finish;
      const otherFinish = targetFinish === 'walnut' ? 'beech' : 'walnut';
      const isPlus = btn.classList.contains('plus');
      const q = qty();

      if (isPlus) {
        if (finCounts[targetFinish] < q) {
          finCounts[targetFinish]++;
          finCounts[otherFinish] = q - finCounts[targetFinish];
        }
      } else {
        if (finCounts[targetFinish] > 0) {
          finCounts[targetFinish]--;
          finCounts[otherFinish] = q - finCounts[targetFinish];
        }
      }
      updateFinishUI();
      sync();
    });
  });

  // finish: hero toggle <-> form <-> storage
  const setF = (f, save = true) => {
    f = f === 'beech' ? 'beech' : 'walnut'; const F = f[0].toUpperCase() + f.slice(1);
    document.body.dataset.f = f;
    $$('.sw button').forEach(b => b.setAttribute('aria-checked', b.dataset.f === f));
    $('#fw').textContent = F; $$('.fn').forEach(e => e.textContent = F + ' finish');
    const r = $(`input[name=finish][value=${F}]`); if (r) r.checked = true;
    if (save) try { localStorage.setItem('nm-finish', f) } catch (e) {}
    updateFinishUI();
    if (typeof sync === 'function' && form) sync();
  };
  $$('.sw button').forEach(b => b.addEventListener('click', () => setF(b.dataset.f)));
  const qty = () => +form.querySelector('input[name=qty]:checked').value;
  const msg = (d) => {
    const q = qty();
    d = d || {name:'',phone:'',address:''};
    const pay = form.querySelector('input[name=payment]:checked')?.value || 'Cash on Delivery';
    const finishDesc = getFinishText();
    const m = `Hello Nova Mart,\\nI would like to order the portable ashtray.\\n\\nName: ${d.name}\\nPhone: ${d.phone}\\nAddress: ${d.address}\\nQuantity: ${q}\\nFinish: ${finishDesc}\\nPayment: ${pay}`;
    return `https://wa.me/${WA}?text=${encodeURIComponent(m)}`;
  };
  const sync = () => {
    const q = qty(); total.textContent = '$' + PRICES[q];
    $$('.plan').forEach(p => p.classList.toggle('on', +p.dataset.q === q));
    updateFinishUI();
    const d = Object.fromEntries(['name', 'phone', 'address'].map(k => [k, form[k].value.trim()]));
    $('#wa-order').href = msg(d.name || d.phone || d.address ? d : null);
  };"""

assert old_js_block in html, "Could not find old_js_block"
html = html.replace(old_js_block, new_js_block)

# Save both index.html and nova-mart-aone.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("nova-mart-aone.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully added custom Walnut/Beech mix picker for multi-piece orders!")
