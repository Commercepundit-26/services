with open('/Users/cp/.gemini/antigravity/brain/675b45b3-1249-4cd2-a478-97874d96a273/scratch/build_anti_counterfeiting_page.py', 'r') as f:
    content = f.read()

# Fix the font issue for outline numbers (preventing overlapping paths in variable fonts)
content = content.replace(
    '.vstep-outline-num {\n  font-size: 4rem;',
    '.vstep-outline-num {\n  font-family: system-ui, -apple-system, sans-serif;\n  font-size: 4rem;'
)

# Remove quotes from the remaining items in "The Cost of Not Knowing"
content = content.replace(
    '"Customs just seized a shipment. Is it yours, or a copy good enough to fool your own team?"',
    'Customs just seized a shipment. Is it yours, or a copy good enough to fool your own team?'
)

content = content.replace(
    '"A viral post shows your product failing — except it\\'s not your product."',
    'A viral post shows your product failing — except it\\'s not your product.'
)

content = content.replace(
    '"Your biggest distributor is quietly buying from someone else, because fakes come in 20% cheaper."',
    'Your biggest distributor is quietly buying from someone else, because fakes come in 20% cheaper.'
)

with open('/Users/cp/.gemini/antigravity/brain/675b45b3-1249-4cd2-a478-97874d96a273/scratch/build_anti_counterfeiting_page.py', 'w') as f:
    f.write(content)
