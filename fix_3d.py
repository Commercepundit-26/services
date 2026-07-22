with open('/Users/cp/.gemini/antigravity/brain/675b45b3-1249-4cd2-a478-97874d96a273/scratch/build_anti_counterfeiting_page.py', 'r') as f:
    content = f.read()

# Decrease hero grid transparency by 50%
content = content.replace('background: rgba(15, 15, 37, 0.4);', 'background: rgba(15, 15, 37, 0.2);')
content = content.replace('background: rgba(104, 98, 167, 0.25);', 'background: rgba(104, 98, 167, 0.12);')

# Add 3D Tilt JS library
tilt_script = """<script src="https://cdnjs.cloudflare.com/ajax/libs/vanilla-tilt/1.8.1/vanilla-tilt.min.js"></script>
</body>"""
content = content.replace('</body>', tilt_script)

# Add data-tilt attributes to the cards
content = content.replace('class="bento-card"', 'class="bento-card" data-tilt data-tilt-max="3" data-tilt-speed="400" data-tilt-glare data-tilt-max-glare="0.05"')
content = content.replace('class="integration-card"', 'class="integration-card" data-tilt data-tilt-max="3" data-tilt-speed="400" data-tilt-glare data-tilt-max-glare="0.05"')

# Also add a slight perspective property to their containers to enhance the 3D feel
# The bento grid container is .bento-grid
content = content.replace('.bento-grid {', '.bento-grid {\n  perspective: 1000px;')
# The integration grid container is .integration-grid
content = content.replace('.integration-grid {', '.integration-grid {\n  perspective: 1000px;')

with open('/Users/cp/.gemini/antigravity/brain/675b45b3-1249-4cd2-a478-97874d96a273/scratch/build_anti_counterfeiting_page.py', 'w') as f:
    f.write(content)
