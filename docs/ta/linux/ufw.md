---
layout: page
title: linux/ufw (தமிழ்)
description: "சிக்கலற்ற ஃபயர்வால்."
content_hash: ba84c1a4e1b9dbe43a5dd26c13362d987018dac5
last_modified_at: 2022-12-29
related_topics:
  - title: català version
    url: /ca/linux/ufw.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/ufw.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/ufw.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/ufw.html
    icon: bi bi-globe
---
# ufw

சிக்கலற்ற ஃபயர்வால்.
ஃபயர்வாலின் உள்ளமைவை எளிதாக்குவதை நோக்கமாகக் கொண்ட ஐப்டேபிள்களுக்கான முன்பக்கம்.
மேலும் விவரத்திற்கு: <https://wiki.ubuntu.com/UncomplicatedFirewall>.

- `ufw` ஐ இயக்கு:

`ufw enable`

- `ufw` ஐ முடக்கு:

`ufw disable`

- `ufw` விதிகளை அவற்றின் எண்களுடன் காட்டு:

`ufw status numbered`

- சேவையை அடையாளம் காட்டும் கருத்துடன் இந்த ஹோஸ்டில் உள்ள போர்ட் 5432 இல் உள்வரும் போக்குவரத்தை அனுமதிக்கவும்:

`ufw allow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5432</span>` comment "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">சேவை</span>`"`

- போர்ட் 22 இல், இந்த ஹோஸ்டில் உள்ள எந்த முகவரிக்கும் 192.168.0.4 இலிருந்து டிசிபி போக்குவரத்தை மட்டும் அனுமதிக்கவும்:

`ufw allow proto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">டிசிபி</span>` from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.4</span>` to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ஏதேனும்</span>` port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22</span>

- இந்த ஹோஸ்டில் போர்ட் 80 இல் போக்குவரத்தை நிராகரிக்கவும்:

`ufw deny `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>

- 8412:8500 வரம்பில் உள்ள துறைமுகங்களுக்கு அனைத்து யுடிபி போக்குவரத்தையும் நிராகரிக்கவும்:

`ufw deny proto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">யுடிபி</span>` from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ஏதேனும்</span>` to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ஏதாவது</span>` port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8412:8500</span>

- ஒரு குறிப்பிட்ட விதியை நீக்கவும். விதி எண்ணை `ufw status numbered` கட்டளையிலிருந்து மீட்டெடுக்கலாம்:

`ufw delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">விதி_எண்</span>
