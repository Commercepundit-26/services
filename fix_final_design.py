with open('/Users/cp/.gemini/antigravity/brain/675b45b3-1249-4cd2-a478-97874d96a273/scratch/build_anti_counterfeiting_page.py', 'r') as f:
    content = f.read()

# 1. Quotes in Section 4
content = content.replace('"Can we measure the ROI of this system?"', 'Can we measure the ROI of this system?')
content = content.replace('"Will this hold up in a court of law during a dispute?"', 'Will this hold up in a court of law during a dispute?')
content = content.replace('"Will this slow down our production line?"', 'Will this slow down our production line?')
content = content.replace('"Does this affect our packaging design?"', 'Does this affect our packaging design?')

# 2. Bento slider shadow cutoff
content = content.replace(
    'padding-bottom: 32px;',
    'padding-bottom: 50px;\n  padding-top: 12px;\n  padding-left: 12px;\n  padding-right: 12px;\n  margin-inline: -12px;\n  margin-top: -12px;'
)

# 3. int-card CSS hover
content = content.replace(
    '.int-card {',
    '.int-card {\n  transition: transform 0.4s ease, box-shadow 0.4s ease, border-color 0.4s ease;'
)
content = content.replace(
    '.int-card-img {',
    '.int-card:hover {\n  transform: translateY(-4px);\n  border-color: rgba(104, 98, 167, 0.4);\n  box-shadow: 0 12px 40px rgba(15, 15, 37, 0.1);\n}\n.int-card-img {'
)

# 4. int-card HTML tilt
content = content.replace(
    '<div class="int-card">',
    '<div class="int-card" data-tilt data-tilt-max="3" data-tilt-speed="400" data-tilt-glare data-tilt-max-glare="0.05">'
)

# 5. Section 7 Table Hover
content = content.replace(
    '.comparison-table tbody tr:last-child td:first-child',
    '.comparison-table tbody tr {\n  transition: background-color 0.2s ease;\n}\n.comparison-table tbody tr:hover {\n  background-color: rgba(104, 98, 167, 0.05);\n}\n.comparison-table tbody tr:last-child td:first-child'
)

# 6. Section 8 Progress Line bounds
content = content.replace(
    'bottom: 32px;\n  width: 2px;\n  background: rgba(0,0,0,0.06);',
    'bottom: 56px;\n  width: 2px;\n  background: rgba(0,0,0,0.06);'
)
content = content.replace(
    'transition: height 0.1s ease-out;\n}',
    'transition: height 0.1s ease-out;\n  max-height: calc(100% - 88px);\n}'
)

with open('/Users/cp/.gemini/antigravity/brain/675b45b3-1249-4cd2-a478-97874d96a273/scratch/build_anti_counterfeiting_page.py', 'w') as f:
    f.write(content)
