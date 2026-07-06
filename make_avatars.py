import os
base = r'c:\Users\Administrator\Desktop\ADIESTRADOR'

avatars = {
"avatar-maria.svg": '''<svg xmlns="http://www.w3.org/2000/svg" width="400" height="300" viewBox="0 0 400 300">
<defs><linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#2D6A4F"/><stop offset="100%" style="stop-color:#52B788"/></linearGradient></defs>
<rect width="400" height="300" fill="url(#g)"/>
<circle cx="200" cy="110" r="55" fill="#D4A574"/><circle cx="200" cy="115" r="42" fill="#F5D5B8"/>
<circle cx="180" cy="105" r="5" fill="#1A1A2E"/><circle cx="220" cy="105" r="5" fill="#1A1A2E"/>
<path d="M188 120 Q200 132 212 120" stroke="#C47A5A" stroke-width="2.5" fill="none" stroke-linecap="round"/>
<text x="200" y="220" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-weight="900" font-size="40">Maria G.</text>
<text x="200" y="255" text-anchor="middle" fill="white" opacity="0.75" font-family="Inter,sans-serif" font-weight="600" font-size="18">Golden Retriever - Nala</text>
</svg>''',
"avatar-carlos.svg": '''<svg xmlns="http://www.w3.org/2000/svg" width="400" height="300" viewBox="0 0 400 300">
<defs><linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#E76F51"/><stop offset="100%" style="stop-color:#D95737"/></linearGradient></defs>
<rect width="400" height="300" fill="url(#g)"/>
<circle cx="200" cy="110" r="55" fill="#D4A574"/><circle cx="200" cy="115" r="42" fill="#F5D5B8"/>
<circle cx="180" cy="105" r="5" fill="#1A1A2E"/><circle cx="220" cy="105" r="5" fill="#1A1A2E"/>
<path d="M188 120 Q200 132 212 120" stroke="#C47A5A" stroke-width="2.5" fill="none" stroke-linecap="round"/>
<text x="200" y="220" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-weight="900" font-size="40">Carlos R.</text>
<text x="200" y="255" text-anchor="middle" fill="white" opacity="0.75" font-family="Inter,sans-serif" font-weight="600" font-size="18">Beagle - Taco</text>
</svg>''',
"avatar-luciana.svg": '''<svg xmlns="http://www.w3.org/2000/svg" width="400" height="300" viewBox="0 0 400 300">
<defs><linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#D4A574"/><stop offset="100%" style="stop-color:#E8C987"/></linearGradient></defs>
<rect width="400" height="300" fill="url(#g)"/>
<circle cx="200" cy="110" r="55" fill="#8B6F47"/><circle cx="200" cy="115" r="42" fill="#D4B896"/>
<circle cx="180" cy="105" r="5" fill="#1A1A2E"/><circle cx="220" cy="105" r="5" fill="#1A1A2E"/>
<path d="M188 120 Q200 132 212 120" stroke="#6B5030" stroke-width="2.5" fill="none" stroke-linecap="round"/>
<text x="200" y="220" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-weight="900" font-size="40">Luciana P.</text>
<text x="200" y="255" text-anchor="middle" fill="white" opacity="0.75" font-family="Inter,sans-serif" font-weight="600" font-size="18">Mestiza - Mora</text>
</svg>''',
"avatar-sofia.svg": '''<svg xmlns="http://www.w3.org/2000/svg" width="400" height="300" viewBox="0 0 400 300">
<defs><linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#2D6A4F"/><stop offset="100%" style="stop-color:#40916C"/></linearGradient></defs>
<rect width="400" height="300" fill="url(#g)"/>
<circle cx="200" cy="110" r="55" fill="#D4A574"/><circle cx="200" cy="115" r="42" fill="#F5D5B8"/>
<circle cx="180" cy="105" r="5" fill="#1A1A2E"/><circle cx="220" cy="105" r="5" fill="#1A1A2E"/>
<path d="M188 120 Q200 132 212 120" stroke="#C47A5A" stroke-width="2.5" fill="none" stroke-linecap="round"/>
<text x="200" y="220" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-weight="900" font-size="40">Sofia V.</text>
<text x="200" y="255" text-anchor="middle" fill="white" opacity="0.75" font-family="Inter,sans-serif" font-weight="600" font-size="18">Caniche - Simon</text>
</svg>'''
}

for name, content in avatars.items():
    path = os.path.join(base, name)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Created {path}')
print('Done!')