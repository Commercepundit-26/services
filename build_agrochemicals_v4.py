import re
from bs4 import BeautifulSoup

# 1. Read the solution page to grab the original components
with open('/Users/cp/Ronak/CP/CP Website/servicepages/solution-anti-counterfeiting.html', 'r', encoding='utf-8') as f:
    sol_html = f.read()

sol_soup = BeautifulSoup(sol_html, 'html.parser')

hero_section = sol_soup.find('section', id='hero')
voices_section = sol_soup.find('section', id='voices')
cta_section = sol_soup.find('section', id='cta')

# 2. Extract Header and Footer from current industry template
with open('/Users/cp/Ronak/CP/CP Website/servicepages/industry-template.html', 'r', encoding='utf-8') as f:
    ind_html = f.read()

# We need everything before the <style> block or the first section
header_match = re.search(r'(.*?)(<style>|<section)', ind_html, re.DOTALL | re.IGNORECASE)
footer_match = re.search(r'(<footer class="site-footer".*)', ind_html, re.DOTALL | re.IGNORECASE)

if not header_match or not footer_match:
    print("Could not find boundaries!")
    exit(1)

header_html = header_match.group(1)
footer_html = footer_match.group(1)

# Modify the copied Hero section with new content
if hero_section:
    eyebrow = hero_section.find(class_='eyebrow')
    if eyebrow: eyebrow.string = 'AGROCHEMICALS'

    h1 = hero_section.find('h1')
    if h1: h1.string = 'Every bag verified. Every dealer accountable. Every acre protected.'

    p = hero_section.find('p', class_='hero-lede')
    if p: p.string = "Smart Epsilon gives agrochemical manufacturers plant-to-field visibility, verified authenticity, and dealer accountability — so spurious product, misapplication liability, and channel disputes get caught before they cost you a season's trust."
    
    # Trust chips
    trust_items = hero_section.find_all('span', class_='features-pill-tag')
    if len(trust_items) >= 2:
        trust_items[0].string = 'EPA / FIFRA-ready compliance'
        trust_items[1].string = 'Works with your ERP'
        import copy
        new_tag = copy.copy(trust_items[1])
        new_tag.string = 'Live in ~6 weeks'
        trust_items[1].insert_after(new_tag)

    cta_btn = hero_section.find('a', class_='btn-primary')
    if cta_btn: cta_btn.string = 'Schedule an Agrochemicals Demo'

    # Right side 3-level card
    level_titles = hero_section.find_all('div', class_='level-title')
    level_descs = hero_section.find_all('p', class_='level-desc')
    if len(level_titles) >= 3 and len(level_descs) >= 3:
        level_titles[0].string = 'Plant-to-field visibility'
        level_descs[0].string = 'Track every bag from the moment it leaves the formulation plant to the moment a grower opens it.'
        level_titles[1].string = 'Dealer Accountability'
        level_descs[1].string = 'Automated payouts built on verified sell-through data, not self-reported shipment numbers.'
        level_titles[2].string = 'Brand Protection'
        level_descs[2].string = 'Stop spurious look-alikes from destroying your brand reputation in the field.'
        
    card_header = hero_section.find('h3', class_='card-header-title')
    if card_header: card_header.string = 'Real-world impact'

# Mid-sections with Light CSS
new_css = """
<style>
/* LIGHT/WHITE REDESIGN CSS (Overrides dark mode) */
:root {
  --agro-surface: #ffffff;
  --agro-surface-alt: #f7f7fa;
  --agro-border: rgba(0,0,0,0.06);
  --agro-darker: #111111;
  --agro-text: #4a4a5a;
  --agro-primary: #6862a7;
}

/* Base Sections */
.agro-section {
  padding: 120px 0;
  background: var(--agro-surface);
}
.agro-section.alt {
  background: var(--agro-surface-alt);
}
.agro-section-header {
  text-align: center;
  max-width: 800px;
  margin: 0 auto 60px;
  padding: 0 2rem;
}
.agro-section-header h2 {
  font-size: clamp(2rem, 3.5vw, 3rem);
  font-weight: 800;
  color: var(--agro-darker);
  margin-bottom: 16px;
  line-height: 1.1;
  letter-spacing: -0.02em;
}
.agro-section-header p {
  font-size: 1.125rem;
  color: var(--agro-text);
  line-height: 1.6;
}

/* Masonry/Alternating Grid (Problems) */
.agro-prob-grid {
  display: flex;
  flex-direction: column;
  gap: 24px;
  max-width: 900px;
  margin: 0 auto;
  padding: 0 2rem;
}
.agro-prob-card {
  background: var(--agro-surface);
  border: 1px solid var(--agro-border);
  border-radius: 20px;
  padding: 32px 40px;
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 32px;
  box-shadow: 0 4px 24px rgba(0,0,0,0.02);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  position: relative;
  overflow: hidden;
}
.agro-prob-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; bottom: 0; width: 4px;
  background: #d32f2f;
  transform: scaleY(0.3);
  transform-origin: top;
  transition: transform 0.4s ease;
}
.agro-prob-card:hover::before { transform: scaleY(1); }
.agro-prob-card:hover {
  transform: translateX(4px);
  box-shadow: 0 12px 40px rgba(15,15,37,0.06);
}
.agro-prob-num {
  font-size: 3rem;
  font-weight: 900;
  color: transparent;
  -webkit-text-stroke: 1px rgba(211, 47, 47, 0.3);
  line-height: 1;
}
.agro-prob-content h3 {
  font-size: 1.35rem;
  font-weight: 800;
  margin-bottom: 12px;
  color: var(--agro-darker);
}
.agro-prob-content p {
  font-size: 1rem;
  color: var(--agro-text);
  line-height: 1.6;
}

/* Solutions Grid */
.agro-sol-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 24px;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}
.agro-sol-card {
  background: var(--agro-surface);
  border: 1px solid var(--agro-border);
  border-radius: 16px;
  padding: 32px;
  transition: all 0.3s ease;
  box-shadow: 0 4px 24px rgba(0,0,0,0.02);
}
.agro-sol-card:hover {
  border-color: rgba(104, 98, 167, 0.4);
  box-shadow: 0 12px 40px rgba(15, 15, 37, 0.08);
  transform: translateY(-4px);
}
.agro-sol-num {
  font-size: 14px;
  font-weight: 700;
  color: var(--agro-primary);
  margin-bottom: 16px;
}
.agro-sol-card p {
  font-size: 1.0625rem;
  line-height: 1.6;
  color: var(--agro-text);
  margin: 0;
}

/* Stacked Cards */
.agro-stack-container {
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  flex-direction: column;
  gap: 40px;
}
.agro-stack-card {
  background: var(--agro-surface);
  border: 1px solid var(--agro-border);
  border-radius: 24px;
  overflow: hidden;
  position: sticky;
  top: 120px;
  box-shadow: 0 -10px 40px rgba(0,0,0,0.02);
  transition: transform 0.3s ease;
}
.agro-stack-card:nth-child(1) { top: 120px; }
.agro-stack-card:nth-child(2) { top: 140px; }
.agro-stack-card:nth-child(3) { top: 160px; }
.agro-stack-card:nth-child(4) { top: 180px; }

.agro-stack-header {
  background: var(--agro-surface-alt);
  color: var(--agro-darker);
  padding: 24px 40px;
  border-bottom: 1px solid var(--agro-border);
}
.agro-stack-header h3 {
  font-size: 1.5rem;
  font-weight: 800;
  margin: 0;
}
.agro-stack-body {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0;
}
.agro-stack-col {
  padding: 40px;
}
.agro-stack-col:first-child {
  border-right: 1px solid var(--agro-border);
}
.agro-stack-col h4 {
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: var(--agro-primary);
  margin-bottom: 24px;
  font-weight: 800;
}
.agro-stack-list {
  list-style: none;
  padding: 0; margin: 0;
}
.agro-stack-list li {
  position: relative;
  padding-left: 24px;
  margin-bottom: 16px;
  font-size: 1rem;
  line-height: 1.6;
  color: var(--agro-text);
}
.agro-stack-list li::before {
  content: '•';
  position: absolute;
  left: 0; top: 0;
  color: var(--agro-primary);
  font-size: 1.5rem;
  line-height: 1.2;
}

/* Impact Grid */
.agro-impact-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}
.agro-impact-card {
  background: var(--agro-surface);
  padding: 32px;
  border-radius: 20px;
  border: 1px solid var(--agro-border);
  box-shadow: 0 4px 12px rgba(0,0,0,0.02);
}
.agro-impact-card h3 {
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--agro-darker);
  margin-bottom: 12px;
}
.agro-impact-card p {
  font-size: 1rem;
  color: var(--agro-text);
  line-height: 1.6;
  margin: 0;
}

/* Compliance Sidebar */
.agro-comp-inner {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 60px;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}
.agro-comp-sidebar {
  position: sticky;
  top: 120px;
}
.agro-comp-sidebar h2 {
  font-size: clamp(2rem, 3vw, 2.5rem);
  font-weight: 800;
  margin-bottom: 16px;
  color: var(--agro-darker);
}
.agro-comp-list {
  display: flex;
  flex-direction: column;
  gap: 32px;
}
.agro-comp-item {
  display: flex;
  gap: 20px;
  align-items: flex-start;
}
.agro-comp-icon {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  background: rgba(104, 98, 167, 0.08);
  color: var(--agro-primary);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}
.agro-comp-text h3 {
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--agro-darker);
  margin-bottom: 8px;
}
.agro-comp-text p {
  font-size: 1rem;
  color: var(--agro-text);
  line-height: 1.6;
  margin: 0;
}

/* FAQ (Light Mode) */
.agro-faq-inner {
  max-width: 800px;
  margin: 0 auto;
  padding: 0 2rem;
}
.agro-faq-item {
  border-bottom: 1px solid var(--agro-border);
}
.agro-faq-q {
  padding: 32px 0;
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--agro-darker);
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.agro-faq-q::after {
  content: '+';
  font-size: 24px;
  font-weight: 300;
  transition: transform 0.3s ease;
}
.agro-faq-item.is-open .agro-faq-q::after {
  transform: rotate(45deg);
}
.agro-faq-a {
  padding-bottom: 32px;
  font-size: 1rem;
  color: var(--agro-text);
  line-height: 1.6;
  display: none;
}
.agro-faq-item.is-open .agro-faq-a {
  display: block;
}

@media (max-width: 992px) {
  .agro-comp-inner { grid-template-columns: 1fr; }
  .agro-comp-sidebar { position: static; }
  .agro-stack-body { grid-template-columns: 1fr; }
  .agro-stack-col:first-child { border-right: none; border-bottom: 1px solid var(--agro-border); }
}
@media (max-width: 768px) {
  .agro-prob-card { grid-template-columns: 1fr; gap: 16px; }
  .agro-prob-num { font-size: 2.5rem; }
}
</style>
"""

new_html = f"""
{new_css}

{str(hero_section) if hero_section else ''}

<!-- 2. REAL SUPPLY CHAIN PROBLEMS -->
<section class="agro-section alt">
  <div class="agro-section-header">
    <p class="eyebrow">Real-world risks</p>
    <h2>Real Supply Chain Problems</h2>
    <p>Agrochemical supply chains break in more ways than any one page can cover — here are the five that cost the most, most often.</p>
  </div>
  
  <div class="agro-prob-grid">
    <div class="agro-prob-card">
      <div class="agro-prob-num">01</div>
      <div class="agro-prob-content">
        <h3>Spurious Product in the Channel</h3>
        <p>"Your biggest ag retailer is quietly stocking a look-alike at 20% below your list price. Can you prove to a grower which bag is real?" Unregistered formulators and repackagers sell copies that look right on the shelf — a grower finds out only when the spray fails.</p>
      </div>
    </div>
    
    <div class="agro-prob-card">
      <div class="agro-prob-num">02</div>
      <div class="agro-prob-content">
        <h3>Sell-In Doesn't Equal Sell-Out</h3>
        <p>"Distributor orders looked strong all season. Why is next year's demand forecast already wrong?" What shipped and what actually moved through the dealer network to a grower are different numbers — and production plans get built on the wrong one.</p>
      </div>
    </div>
    
    <div class="agro-prob-card">
      <div class="agro-prob-num">03</div>
      <div class="agro-prob-content">
        <h3>Regulatory Audit, No Notice</h3>
        <p>"A State Lead Agency inspector wants batch-level RUP records and WPS documentation — this week." Reconstructing that from spreadsheets turns a routine inspection into a multi-day scramble.</p>
      </div>
    </div>
    
    <div class="agro-prob-card">
      <div class="agro-prob-num">04</div>
      <div class="agro-prob-content">
        <h3>Misapplication Liability</h3>
        <p>"A grower used the wrong dosage, and now there's a crop-failure claim with your name on it." The liability conversation starts with your brand, whether or not the product was ever the actual problem.</p>
      </div>
    </div>
    
    <div class="agro-prob-card">
      <div class="agro-prob-num">05</div>
      <div class="agro-prob-content">
        <h3>Dealer Trust and Channel Loyalty</h3>
        <p>"Your dealer's incentive payout has been stuck in review for six weeks. Why would they push your product this season?" Slow, disputed rebate programs cost the shelf space the payout was supposed to buy.</p>
      </div>
    </div>
  </div>
</section>

<!-- 3. SOLUTIONS -->
<section class="agro-section">
  <div class="agro-section-header">
    <p class="eyebrow">Platform Capabilities</p>
    <h2>Solutions</h2>
    <p>Ten specific problems Smart Epsilon solves for agrochemical manufacturers.</p>
  </div>
  
  <div class="agro-sol-grid">
    <div class="agro-sol-card">
      <div class="agro-sol-num">01</div>
      <p>Verify a crop protection product's authenticity before purchase — no device required for the first check.</p>
    </div>
    <div class="agro-sol-card">
      <div class="agro-sol-num">02</div>
      <p>Replace shipment-based demand estimates with real, scan-confirmed sell-through data.</p>
    </div>
    <div class="agro-sol-card">
      <div class="agro-sol-num">03</div>
      <p>Produce audit-ready batch records for a state or federal inspection in minutes, not days.</p>
    </div>
    <div class="agro-sol-card">
      <div class="agro-sol-num">04</div>
      <p>Deliver dosage, tank-mix compatibility, and safety guidance at the point of scan, in the applicator's language.</p>
    </div>
    <div class="agro-sol-card">
      <div class="agro-sol-num">05</div>
      <p>Calculate dealer incentive payouts automatically from verified sales — not self-reported invoice volume.</p>
    </div>
    <div class="agro-sol-card">
      <div class="agro-sol-num">06</div>
      <p>Detect counterfeit or diverted product entering regional distribution before it reaches a shelf.</p>
    </div>
    <div class="agro-sol-card">
      <div class="agro-sol-num">07</div>
      <p>Confirm loading and unloading accuracy at regional distribution centers in real time.</p>
    </div>
    <div class="agro-sol-card">
      <div class="agro-sol-num">08</div>
      <p>Monitor temperature compliance for cold-sensitive seed treatments in storage and transit.</p>
    </div>
    <div class="agro-sol-card">
      <div class="agro-sol-num">09</div>
      <p>Flag shrinkage or theft of high-value patented formulations as it happens, not at the next count.</p>
    </div>
    <div class="agro-sol-card">
      <div class="agro-sol-num">10</div>
      <p>Give every dealer real-time visibility into exactly what they've earned, and why.</p>
    </div>
  </div>
</section>

<!-- 4. HOW EACH SOLUTION APPLIES -->
<section class="agro-section alt agro-stack-section">
  <div class="agro-section-header">
    <p class="eyebrow">Agrochemical Implementations</p>
    <h2>How Each Solution Applies</h2>
    <p>Horizontal stacked cards — left side: Agro-specific implementation. Right side: business impact.</p>
  </div>
  
  <div class="agro-stack-container">
    <!-- Card 1 -->
    <div class="agro-stack-card">
      <div class="agro-stack-header">
        <h3>Card 1 — Track & Trace</h3>
      </div>
      <div class="agro-stack-body">
        <div class="agro-stack-col">
          <h4>Agro-specific implementation</h4>
          <ul class="agro-stack-list">
            <li>Serialization at the point of formulation, tied to each product's EPA registration number</li>
            <li>Dispatch and receipt confirmed at every regional distribution center — not assumed from an invoice</li>
            <li>Real, scan-verified sell-through data from the dealer network, replacing shipment-based estimates</li>
          </ul>
        </div>
        <div class="agro-stack-col">
          <h4>Business impact</h4>
          <ul class="agro-stack-list">
            <li>Demand forecasts built on what actually sold, not what was shipped</li>
            <li>Audit-ready compliance records in minutes instead of a multi-day scramble</li>
          </ul>
        </div>
      </div>
    </div>
    
    <!-- Card 2 -->
    <div class="agro-stack-card">
      <div class="agro-stack-header">
        <h3>Card 2 — Anti-Counterfeiting Solution</h3>
      </div>
      <div class="agro-stack-body">
        <div class="agro-stack-col">
          <h4>Agro-specific implementation</h4>
          <ul class="agro-stack-list">
            <li>Tamper-evident holographic label on every bag or container, verified in seconds before purchase</li>
            <li>Geo-tagged clone detection flags a duplicate code the moment it's scanned somewhere it shouldn't be</li>
            <li>Dosage, tank-mix compatibility, and safety guidance delivered at the point of scan, in the applicator's language</li>
          </ul>
        </div>
        <div class="agro-stack-col">
          <h4>Business impact</h4>
          <ul class="agro-stack-list">
            <li>Fewer efficacy complaints traced back to spurious product</li>
            <li>Fewer misapplication-driven liability claims, backed by a timestamped record of what was communicated</li>
          </ul>
        </div>
      </div>
    </div>
    
    <!-- Card 3 -->
    <div class="agro-stack-card">
      <div class="agro-stack-header">
        <h3>Card 3 — AI Video Intelligence</h3>
      </div>
      <div class="agro-stack-body">
        <div class="agro-stack-col">
          <h4>Agro-specific implementation</h4>
          <ul class="agro-stack-list">
            <li>Loading and unloading verification at regional distribution centers, confirming dispatch matches the manifest</li>
            <li>Purpose-placed thermal monitoring for temperature-sensitive seed treatments in storage</li>
            <li>Targeted coverage on high-value patented formulations to catch shrinkage as it happens</li>
          </ul>
        </div>
        <div class="agro-stack-col">
          <h4>Business impact</h4>
          <ul class="agro-stack-list">
            <li>Freight disputes resolved with visual proof, not guesswork</li>
            <li>Temperature excursions caught before an entire batch of seed treatment is lost</li>
          </ul>
        </div>
      </div>
    </div>
    
    <!-- Card 4 -->
    <div class="agro-stack-card">
      <div class="agro-stack-header">
        <h3>Card 4 — Payment Linked Incentives</h3>
      </div>
      <div class="agro-stack-body">
        <div class="agro-stack-col">
          <h4>Agro-specific implementation</h4>
          <ul class="agro-stack-list">
            <li>Dealer incentive payouts calculated automatically from verified, scan-confirmed sell-through — not invoice volume</li>
            <li>Real-time dashboard shows every dealer exactly what they've earned, and why</li>
          </ul>
        </div>
        <div class="agro-stack-col">
          <h4>Business impact</h4>
          <ul class="agro-stack-list">
            <li>Faster, dispute-resistant payouts that reward dealers for real sell-through</li>
            <li>Protected shelf space and loyalty at the next reorder</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- 5. BUSINESS IMPACT -->
<section class="agro-section">
  <div class="agro-section-header">
    <p class="eyebrow">Enterprise Value</p>
    <h2>Business Impact</h2>
    <p>What this adds up to across an agrochemical manufacturing operation.</p>
  </div>
  
  <div class="agro-impact-grid">
    <div class="agro-impact-card">
      <h3>End-to-End Product Visibility</h3>
      <p>From formulation to field, know where every unit is at every stage — not just inside your own four walls.</p>
    </div>
    <div class="agro-impact-card">
      <h3>Protected Brand Trust</h3>
      <p>Fewer efficacy complaints and liability disputes traced back to spurious product reaching the shelf.</p>
    </div>
    <div class="agro-impact-card">
      <h3>Reduced Liability Exposure</h3>
      <p>A timestamped, defensible record of exactly what dosage and safety guidance was communicated, if a misapplication claim ever surfaces.</p>
    </div>
    <div class="agro-impact-card">
      <h3>Accurate Demand Planning</h3>
      <p>Production and inventory decisions built on real, verified sell-through — not shipment estimates that turn out wrong by harvest.</p>
    </div>
    <div class="agro-impact-card">
      <h3>Audit-Ready Compliance</h3>
      <p>Batch-level FIFRA, RUP, and WPS records available in minutes during a state or federal inspection, not reconstructed under deadline pressure.</p>
    </div>
    <div class="agro-impact-card">
      <h3>Stronger Dealer Relationships</h3>
      <p>Faster, dispute-resistant incentive payouts that reward what a dealer actually sold — protecting shelf space at the next reorder.</p>
    </div>
    <div class="agro-impact-card">
      <h3>Faster Dispute Resolution</h3>
      <p>Visual and data-backed proof resolves freight, distributor, and dealer disagreements in minutes instead of open-ended back-and-forth.</p>
    </div>
    <div class="agro-impact-card">
      <h3>Protected Cold-Chain Integrity</h3>
      <p>Real-time temperature monitoring catches an excursion before an entire batch of seed treatment is lost.</p>
    </div>
  </div>
</section>

<!-- 6. COMPLIANCE & REGULATORY -->
<section class="agro-section alt">
  <div class="agro-comp-inner">
    <div class="agro-comp-sidebar">
      <p class="eyebrow">Regulatory Alignment</p>
      <h2>Compliance & Regulatory Context</h2>
      <p style="font-size: 1.125rem; color: var(--agro-text); line-height: 1.6;">FIFRA, EPA registration, and state pesticide law — handled, not hoped for.</p>
    </div>
    <div class="agro-comp-list">
      <div class="agro-comp-item">
        <div class="agro-comp-icon"><svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg></div>
        <div class="agro-comp-text">
          <h3>FIFRA / EPA registration alignment</h3>
          <p>Serialization ties directly to each product's EPA registration number, the identifier regulators and state inspectors check first.</p>
        </div>
      </div>
      <div class="agro-comp-item">
        <div class="agro-comp-icon"><svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg></div>
        <div class="agro-comp-text">
          <h3>Restricted Use Pesticide (RUP) tracking</h3>
          <p>Purchase and application records tied to certified-applicator data, supporting the recordkeeping FIFRA requires.</p>
        </div>
      </div>
      <div class="agro-comp-item">
        <div class="agro-comp-icon"><svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg></div>
        <div class="agro-comp-text">
          <h3>Worker Protection Standard (WPS) support</h3>
          <p>Point-of-scan delivery of Restricted Entry Interval (REI), Pre-Harvest Interval (PHI), and safety guidance, in the applicator's preferred language.</p>
        </div>
      </div>
      <div class="agro-comp-item">
        <div class="agro-comp-icon"><svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg></div>
        <div class="agro-comp-text">
          <h3>State Lead Agency compliance</h3>
          <p>Every state enforces pesticide law through its own Department of Agriculture, coordinated nationally via AAPCO; batch and dealer-level data support audit-readiness during inspection.</p>
        </div>
      </div>
      <div class="agro-comp-item">
        <div class="agro-comp-icon"><svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg></div>
        <div class="agro-comp-text">
          <h3>Maximum Residue Limit (MRL) traceability</h3>
          <p>Batch-level data supports residue-testing queries and export-market compliance.</p>
        </div>
      </div>
    </div>
  </div>
</section>

"""

if voices_section:
    # Update testimonial
    t_quote = voices_section.find('p', class_='testimonial-quote')
    t_author = voices_section.find('div', class_='testimonial-author')
    t_role = voices_section.find('div', class_='testimonial-role')
    
    if t_quote: t_quote.string = '"Smart Epsilon anti-counterfeiting solution cut counterfeit-driven complaints sharply in our first two quarters. Our field team now spots clones before customers do."'
    if t_author: t_author.string = "Head of Brand Protection"
    if t_role: t_role.string = "Agrochemicals major"
    
    # We should add the stats if possible, or just append it to the role
    if t_role:
        t_role.string = "Agrochemicals major. World's largest agrochemical company — End-to-end visibility across 10+ countries with unit-level serialization at scale."
        
    new_html += str(voices_section)

# 8. BEFORE YOU ASK (FAQ) - Kept custom but restyled light
new_html += """
<section class="agro-section alt">
  <div class="agro-section-header">
    <p class="eyebrow">Before you ask</p>
    <h2>Frequently Asked Questions</h2>
  </div>
  <div class="agro-faq-inner">
    <div class="agro-faq-item">
      <div class="agro-faq-q">Does this support Restricted Use Pesticide (RUP) recordkeeping?</div>
      <div class="agro-faq-a">Yes — purchase and application records for RUPs are tied to certified-applicator data at the point of scan, supporting FIFRA's recordkeeping requirements.</div>
    </div>
    <div class="agro-faq-item">
      <div class="agro-faq-q">Can safety and application information reach our applicator network in multiple languages?</div>
      <div class="agro-faq-a">Yes — dosage, tank-mix, and safety guidance can be delivered in the applicator's preferred language at the point of scan, supporting WPS accessibility requirements.</div>
    </div>
    <div class="agro-faq-item">
      <div class="agro-faq-q">How does this integrate with our existing distributor and ERP systems?</div>
      <div class="agro-faq-a">Smart Epsilon connects to SAP, Oracle, and other major ERPs without rip-and-replace, via GS1 EPCIS 2.0. Most agrochemical clients are live in about six weeks.</div>
    </div>
    <div class="agro-faq-item">
      <div class="agro-faq-q">During a state inspection, can we produce batch-level records on demand?</div>
      <div class="agro-faq-a">Yes — batch and dealer-level data is queryable in real time, tied to each product's EPA registration number, for audit-readiness during State Lead Agency inspection.</div>
    </div>
  </div>
</section>

<script>
  document.querySelectorAll('.agro-faq-q').forEach(item => {
    item.addEventListener('click', () => {
      item.parentElement.classList.toggle('is-open');
    });
  });
</script>
"""

# CTA section
if cta_section:
    cta_intro = cta_section.find('h2', class_='cta-intro__title')
    cta_lede = cta_section.find('p', class_='cta-intro__lede')
    if cta_intro:
        cta_intro.string = "See how Smart Epsilon protects your formulation, your dealer network, and the growers who trust your label."
        # Keep html structure by parsing
        cta_intro.clear()
        cta_intro.append(BeautifulSoup("See how Smart Epsilon protects your formulation,<br/>your dealer network, and the growers who trust your label.", 'html.parser'))
    if cta_lede: cta_lede.string = ""
    new_html += str(cta_section)


final_html = header_html + new_html + footer_html

with open('/Users/cp/Ronak/CP/CP Website/servicepages/industry-template.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Redesign HTML correctly written.")
