with open('/Users/cp/.gemini/antigravity/brain/675b45b3-1249-4cd2-a478-97874d96a273/scratch/build_anti_counterfeiting_page.py', 'r') as f:
    content = f.read()

# 1. Quote Fix (Removing literal quote marks from HTML in Sec 2)
content = content.replace('"A customer was hurt by a counterfeit sold under your name. Whose liability is that?"', 'A customer was hurt by a counterfeit sold under your name. Whose liability is that?')
# Remove any remaining stray quotes in the quote items just in case
content = content.replace('<p class="quote-item__q">"', '<p class="quote-item__q">')
content = content.replace('?"</p>', '?</p>')
content = content.replace('."</p>', '.</p>')
content = content.replace('"</p>', '</p>')

# 2. ERP Image
import glob, os
erp_images = glob.glob('/Users/cp/Ronak/CP/CP Website/servicepages/assets/sec6_erp_v2*.jpg')
if erp_images:
    new_erp_img = os.path.basename(erp_images[0])
    content = content.replace('src="assets/sec6_erp_1784700440246.jpg"', f'src="assets/{new_erp_img}"')
    content = content.replace('src="assets/sec6_erp.jpg"', f'src="assets/{new_erp_img}"')


# 3. Section 8 (Rollout) Timeline Icon Dark Color
content = content.replace('color: rgba(0,0,0,0.4);', 'color: #111111;')

# 4. Section 5 & 6 Hover Effects
sec5_hover_css = """  transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
}
.bento-card:hover {
  transform: translateY(-4px);
  border-color: rgba(104, 98, 167, 0.4);
  box-shadow: 0 12px 40px rgba(15, 15, 37, 0.1);
}"""
if '.bento-card:hover' not in content:
    content = content.replace('  box-shadow: 0 4px 24px rgba(0,0,0,0.02);\n}', '  box-shadow: 0 4px 24px rgba(0,0,0,0.02);\n' + sec5_hover_css)


sec6_css_update = """  transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
}
.integration-card:hover {
  transform: translateY(-4px);
  border-color: rgba(104, 98, 167, 0.4);
  box-shadow: 0 12px 40px rgba(15, 15, 37, 0.1);
}
.integration-card:hover .integration-img {
  transform: scale(1.05);
}"""

content = content.replace("""  transition: all 0.3s ease;
}
.integration-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 32px rgba(0,0,0,0.06);
}""", sec6_css_update)

content = content.replace(""".integration-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}""", """.integration-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.7s cubic-bezier(0.16, 1, 0.3, 1);
}""")

with open('/Users/cp/.gemini/antigravity/brain/675b45b3-1249-4cd2-a478-97874d96a273/scratch/build_anti_counterfeiting_page.py', 'w') as f:
    f.write(content)
