import re
from bs4 import BeautifulSoup

def build_page():
    with open('/Users/cp/Ronak/CP/CP Website/servicepages/industry-template.html', 'r') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # 1. Hero Section
    eyebrow = soup.find(class_='eyebrow')
    if eyebrow: eyebrow.string = 'AGROCHEMICALS'

    page_title = soup.find('h1', class_='page-title')
    if page_title: page_title.string = 'Every bag verified. Every dealer accountable. Every acre protected.'

    # Find the subhead which is the p tag after h1
    if page_title:
        subhead = page_title.find_next_sibling('p')
        if subhead: subhead.string = "Smart Epsilon gives agrochemical manufacturers plant-to-field visibility, verified authenticity, and dealer accountability — so spurious product, misapplication liability, and channel disputes get caught before they cost you a season's trust."

    # Trust chips
    trust_items = soup.find_all('span', class_='features-pill-tag')
    if len(trust_items) >= 2:
        trust_items[0].string = 'EPA / FIFRA-ready compliance'
        trust_items[1].string = 'Works with your ERP'
        # Add third one by duplicating second
        import copy
        new_tag = copy.copy(trust_items[1])
        new_tag.string = 'Live in ~6 weeks'
        trust_items[1].insert_after(new_tag)

    # CTA
    hero_btn = soup.find('a', class_='btn-primary')
    if hero_btn:
        hero_btn.string = 'Schedule an Agrochemicals Demo'

    # Right Card in Hero
    level_titles = soup.find_all('div', class_='level-title')
    level_descs = soup.find_all('p', class_='level-desc')
    if len(level_titles) >= 3 and len(level_descs) >= 3:
        level_titles[0].string = 'Plant-to-field visibility'
        level_descs[0].string = 'Track every bag from the moment it leaves the formulation plant to the moment a grower opens it.'
        level_titles[1].string = 'Dealer Accountability'
        level_descs[1].string = 'Automated payouts built on verified sell-through data, not self-reported shipment numbers.'
        level_titles[2].string = 'Brand Protection'
        level_descs[2].string = 'Stop spurious look-alikes from destroying your brand reputation in the field.'

    card_header = soup.find('h3', class_='card-header-title')
    if card_header: card_header.string = 'Real-world impact'

    # 2. Real Supply Chain Problems (Quote Wall)
    quote_eyebrow = soup.find('span', class_='quote-wall-eyebrow')
    if quote_eyebrow: quote_eyebrow.string = 'Agrochemical supply chains break in more ways than any one page can cover'
    
    quote_title = soup.find('h2', class_='quote-wall-title')
    if quote_title: quote_title.string = 'Here are the five that cost the most, most often.'
    
    quote_subtitle = soup.find('p', class_='quote-wall-subtitle')
    if quote_subtitle: quote_subtitle.string = '' # removing it since it's combined into title

    quotes = soup.find_all('div', class_='quote-item')
    quote_data = [
        ("Spurious Product in the Channel", "Your biggest ag retailer is quietly stocking a look-alike at 20% below your list price. Can you prove to a grower which bag is real? Unregistered formulators and repackagers sell copies that look right on the shelf — a grower finds out only when the spray fails."),
        ("Sell-In Doesn't Equal Sell-Out", "Distributor orders looked strong all season. Why is next year's demand forecast already wrong? What shipped and what actually moved through the dealer network to a grower are different numbers — and production plans get built on the wrong one."),
        ("Regulatory Audit, No Notice", "A State Lead Agency inspector wants batch-level RUP records and WPS documentation — this week. Reconstructing that from spreadsheets turns a routine inspection into a multi-day scramble."),
        ("Misapplication Liability", "A grower used the wrong dosage, and now there's a crop-failure claim with your name on it. The liability conversation starts with your brand, whether or not the product was ever the actual problem."),
        ("Dealer Trust and Channel Loyalty", "Your dealer's incentive payout has been stuck in review for six weeks. Why would they push your product this season? Slow, disputed rebate programs cost the shelf space the payout was supposed to buy.")
    ]
    
    # We need 5 quotes, template has 4. Let's duplicate the last one.
    if len(quotes) < 5:
        import copy
        for _ in range(5 - len(quotes)):
            new_quote = copy.copy(quotes[0])
            quotes[-1].insert_after(new_quote)
        quotes = soup.find_all('div', class_='quote-item')
        
    for i, (title, desc) in enumerate(quote_data):
        q = quotes[i].find('div', class_='quote-item__q')
        a = quotes[i].find('div', class_='quote-item__answer')
        num = quotes[i].find('div', class_='quote-item__num')
        if num: num.string = f"0{i+1}"
        if q: q.string = title
        if a: a.string = desc

    # 3. Solutions (Bento Slider)
    bento_header = soup.find('div', class_='bento-header')
    if bento_header:
        b_eyebrow = bento_header.find('p', class_='eyebrow')
        b_h2 = bento_header.find('h2')
        b_p = bento_header.find('p')
        if b_eyebrow: b_eyebrow.string = 'Solutions'
        if b_h2: b_h2.string = 'Ten specific problems Smart Epsilon solves for agrochemical manufacturers.'
        if b_p: b_p.string = ''

    bento_cards = soup.find_all('div', class_='bento-card')
    bento_data = [
        ("Verify authenticity", "Verify a crop protection product's authenticity before purchase — no device required for the first check."),
        ("Real demand data", "Replace shipment-based demand estimates with real, scan-confirmed sell-through data."),
        ("Audit-ready records", "Produce audit-ready batch records for a state or federal inspection in minutes, not days."),
        ("Safety guidance", "Deliver dosage, tank-mix compatibility, and safety guidance at the point of scan, in the applicator's language."),
        ("Automated payouts", "Calculate dealer incentive payouts automatically from verified sales — not self-reported invoice volume."),
        ("Detect diversion", "Detect counterfeit or diverted product entering regional distribution before it reaches a shelf."),
        ("Loading accuracy", "Confirm loading and unloading accuracy at regional distribution centers in real time."),
        ("Cold-chain compliance", "Monitor temperature compliance for cold-sensitive seed treatments in storage and transit."),
        ("Flag shrinkage/theft", "Flag shrinkage or theft of high-value patented formulations as it happens, not at the next count."),
        ("Dealer visibility", "Give every dealer real-time visibility into exactly what they've earned, and why.")
    ]
    
    # Template has 6 bento cards, we need 10
    if len(bento_cards) < 10:
        import copy
        parent = bento_cards[0].parent
        for _ in range(10 - len(bento_cards)):
            new_card = copy.copy(bento_cards[0])
            parent.append(new_card)
        bento_cards = soup.find_all('div', class_='bento-card')
        
    for i, (title, desc) in enumerate(bento_data):
        t_el = bento_cards[i].find('h3', class_='bento-title')
        d_el = bento_cards[i].find('p', class_='bento-desc')
        if t_el: t_el.string = title
        if d_el: d_el.string = desc

    # 4. How Each Solution Applies to Agrochemicals (Integration Grid)
    int_header = soup.find('section', class_='integration-section').find('div', style=lambda v: v and 'max-width: 600px' in v)
    if int_header:
        i_eyebrow = int_header.find('p', class_='eyebrow')
        i_h2 = int_header.find('h2')
        i_p = int_header.find('p')
        if i_eyebrow: i_eyebrow.string = 'How Each Solution Applies'
        if i_h2: i_h2.string = 'Agrochemical Implementations'
        if i_p: i_p.string = 'Horizontal stacked cards showing agro-specific implementation and business impact.'

    int_cards = soup.find_all('div', class_='int-card')
    int_data = [
        ("1. Track & Trace", "Implementation:\n- Serialization at formulation, tied to EPA registration number\n- Dispatch and receipt confirmed at every regional distribution center\n- Real, scan-verified sell-through data from the dealer network\n\nImpact:\n- Demand forecasts built on actual sales\n- Audit-ready compliance records in minutes"),
        ("2. Anti-Counterfeiting Solution", "Implementation:\n- Tamper-evident holographic label verified in seconds\n- Geo-tagged clone detection flags duplicates\n- Dosage, tank-mix compatibility delivered at point of scan\n\nImpact:\n- Fewer efficacy complaints traced to spurious product\n- Fewer misapplication liability claims"),
        ("3. AI Video Intelligence", "Implementation:\n- Loading/unloading verification at regional centers\n- Thermal monitoring for temperature-sensitive seed treatments\n- Targeted coverage on high-value formulations\n\nImpact:\n- Freight disputes resolved with visual proof\n- Temperature excursions caught before batch is lost"),
        ("4. Payment Linked Incentives", "Implementation:\n- Dealer payouts calculated automatically from verified sell-through\n- Real-time dashboard shows dealers exactly what they earned\n\nImpact:\n- Faster, dispute-resistant payouts\n- Protected shelf space and loyalty at the next reorder")
    ]
    
    # Template has 3 cards, we need 4.
    if len(int_cards) < len(int_data):
        import copy
        for _ in range(len(int_data) - len(int_cards)):
            new_card = copy.copy(int_cards[0])
            int_cards[-1].insert_after(new_card)
        int_cards = soup.find_all('div', class_='int-card')
        
    for i, (title, desc) in enumerate(int_data):
        # We will remove the image since we don't have specific ones for these, or keep placeholders?
        # User said "remove all the extra content dont put any content beoynd what i have provided u"
        # Let's remove the .int-card-img entirely to clean up the layout
        img = int_cards[i].find('img', class_='int-card-img')
        if img: img.decompose()
        
        t_el = int_cards[i].find('h3', class_='int-card-title')
        d_el = int_cards[i].find('p', class_='int-card-desc')
        if t_el: t_el.string = title
        if d_el:
            # We need to render the newlines as <br> or multiple paragraphs.
            # Using BeautifulSoup we can replace the text with <br>s
            d_el.clear()
            lines = desc.split('\n')
            for idx, line in enumerate(lines):
                d_el.append(line)
                if idx < len(lines) - 1:
                    d_el.append(soup.new_tag('br'))

    # 5. Business Impact (Sticky List)
    vstep_section = soup.find('section', class_='vstep-section')
    if vstep_section:
        v_eyebrow = vstep_section.find('p', class_='eyebrow')
        v_h2 = vstep_section.find('h2')
        v_p = vstep_section.find('p')
        if v_eyebrow: v_eyebrow.string = 'Business Impact'
        if v_h2: v_h2.string = 'What this adds up to across an agrochemical manufacturing operation.'
        if v_p: v_p.string = ''

    vsteps = soup.find_all('div', class_='vstep-item')
    vstep_data = [
        ("End-to-End Product Visibility", "From formulation to field, know where every unit is at every stage — not just inside your own four walls."),
        ("Protected Brand Trust", "Fewer efficacy complaints and liability disputes traced back to spurious product reaching the shelf."),
        ("Reduced Liability Exposure", "A timestamped, defensible record of exactly what dosage and safety guidance was communicated, if a misapplication claim ever surfaces."),
        ("Accurate Demand Planning", "Production and inventory decisions built on real, verified sell-through — not shipment estimates that turn out wrong by harvest."),
        ("Audit-Ready Compliance", "Batch-level FIFRA, RUP, and WPS records available in minutes during a state or federal inspection, not reconstructed under deadline pressure."),
        ("Stronger Dealer Relationships", "Faster, dispute-resistant incentive payouts that reward what a dealer actually sold — protecting shelf space at the next reorder."),
        ("Faster Dispute Resolution", "Visual and data-backed proof resolves freight, distributor, and dealer disagreements in minutes instead of open-ended back-and-forth."),
        ("Protected Cold-Chain Integrity", "Real-time temperature monitoring catches an excursion before an entire batch of seed treatment is lost.")
    ]
    
    if len(vsteps) > 0:
        import copy
        parent = vsteps[0].parent
        for v in vsteps[1:]:
            v.decompose()
        for _ in range(7):
            new_vstep = copy.copy(vsteps[0])
            parent.append(new_vstep)
        vsteps = soup.find_all('div', class_='vstep-item')
    
    for i, (title, desc) in enumerate(vstep_data):
        t_el = vsteps[i].find('h3', class_='vstep-title')
        d_el = vsteps[i].find('p', class_='vstep-desc')
        num_el = vsteps[i].find('div', class_='vstep-outline-num')
        if t_el: t_el.string = title
        if d_el: d_el.string = desc
        if num_el: num_el.string = f"0{i+1}"

    # 6. Compliance & Regulatory Context (Features Capsule)
    features_section = soup.find('section', id='features')
    if features_section:
        f_eyebrow = features_section.find('p', class_='eyebrow')
        f_h2 = features_section.find('h2')
        f_p = features_section.find('p', style=lambda v: v and 'font-size: 1.125rem' in v)
        if f_eyebrow: f_eyebrow.string = 'Compliance & Regulatory Context'
        if f_h2: f_h2.string = 'FIFRA, EPA registration, and state pesticide law — handled, not hoped for.'
        if f_p: f_p.string = ''

    tabs = soup.find_all('button', class_='features-capsule-tab')
    tab_data = [
        ("FIFRA / EPA Registration Alignment", "Serialization ties directly to each product's EPA registration number, the identifier regulators and state inspectors check first."),
        ("RUP Tracking", "Purchase and application records tied to certified-applicator data, supporting the recordkeeping FIFRA requires."),
        ("WPS Support", "Point-of-scan delivery of Restricted Entry Interval (REI), Pre-Harvest Interval (PHI), and safety guidance, in the applicator's preferred language."),
        ("State Lead Agency compliance", "Every state enforces pesticide law through its own Department of Agriculture, coordinated nationally via AAPCO; batch and dealer-level data support audit-readiness during inspection.")
    ]
    
    contents = soup.find_all('div', class_='features-slide-content')
    
    for i, (title, desc) in enumerate(tab_data):
        if i < len(tabs):
            span = tabs[i].find('span')
            if span: span.string = title.split(' ')[0] # just use the first word or two for the tab button
        if i < len(contents):
            h3 = contents[i].find('h3')
            p = contents[i].find('p')
            if h3: h3.string = title
            if p: p.string = desc

    # 7. Proof
    testimonials = soup.find_all('div', class_='testimonial-card')
    if testimonials:
        t_quote = testimonials[0].find('p', class_='testimonial-quote')
        t_author = testimonials[0].find('div', class_='testimonial-author')
        t_role = testimonials[0].find('div', class_='testimonial-role')
        if t_quote: t_quote.string = "\"Smart Epsilon's anti-counterfeiting solution cut counterfeit-driven complaints sharply in our first two quarters. Our field team now spots clones before customers do.\""
        if t_author: t_author.string = "Head of Brand Protection"
        if t_role: t_role.string = "Agrochemicals major"

    # Add the "World's largest agrochemical company" text somewhere nearby if possible, or skip since user said "dont put any content beoynd what i have provided u"

    # 8. Before You Ask
    faq_section = soup.find('section', class_='faq-section')
    if faq_section:
        faq_eyebrow = faq_section.find('p', class_='eyebrow')
        faq_h2 = faq_section.find('h2')
        faq_p = faq_section.find('p', style=lambda v: v and 'font-size: 1.125rem' in v)
        if faq_eyebrow: faq_eyebrow.string = 'Before you ask'
        if faq_h2: faq_h2.string = 'Frequently Asked Questions'
        if faq_p: faq_p.string = ''
        
    faq_items = soup.find_all('div', class_='faq-item')
    faq_data = [
        ("Does this support Restricted Use Pesticide (RUP) recordkeeping?", "Yes — purchase and application records for RUPs are tied to certified-applicator data at the point of scan, supporting FIFRA's recordkeeping requirements."),
        ("Can safety and application information reach our applicator network in multiple languages?", "Yes — dosage, tank-mix, and safety guidance can be delivered in the applicator's preferred language at the point of scan, supporting WPS accessibility requirements."),
        ("How does this integrate with our existing distributor and ERP systems?", "Smart Epsilon connects to SAP, Oracle, and other major ERPs without rip-and-replace, via GS1 EPCIS 2.0. Most agrochemical clients are live in about six weeks."),
        ("During a state inspection, can we produce batch-level records on demand?", "Yes — batch and dealer-level data is queryable in real time, tied to each product's EPA registration number, for audit-readiness during State Lead Agency inspection.")
    ]
    
    if len(faq_items) > 0:
        import copy
        parent = faq_items[0].parent
        for f in faq_items[1:]:
            f.decompose()
        for _ in range(3):
            new_f = copy.copy(faq_items[0])
            parent.append(new_f)
        faq_items = soup.find_all('div', class_='faq-item')
        
    for i, (title, desc) in enumerate(faq_data):
        q = faq_items[i].find('div', class_='faq-trigger-q')
        a = faq_items[i].find('div', class_='faq-answer-inner')
        if q: q.string = title
        if a: a.string = desc

    # 9. CTA
    cta_section = soup.find('section', class_='cta-section')
    if cta_section:
        cta_h2 = cta_section.find('h2')
        cta_p = cta_section.find('p')
        cta_btn = cta_section.find('a', class_='btn-primary')
        if cta_h2: cta_h2.string = 'See how Smart Epsilon protects your formulation, your dealer network, and the growers who trust your label.'
        if cta_p: cta_p.string = ''
        if cta_btn: cta_btn.string = 'Schedule an Agrochemicals Demo'

    with open('/Users/cp/Ronak/CP/CP Website/servicepages/industry-template.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

    print("Content accurately mapped using BeautifulSoup!")

build_page()
