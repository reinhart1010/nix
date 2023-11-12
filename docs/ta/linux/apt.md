---
layout: page
title: linux/apt (தமிழ்)
description: "டெபியன் அடிப்படையிலான விநியோகங்களுக்கான தொகுப்பு மேலாண்மை பயன்பாடு."
content_hash: 8c9d7c0e851c8656b615ecf74ea3afc2bb2f8ade
last_modified_at: 2023-11-12
related_topics:
  - title: العربية version
    url: /ar/linux/apt.html
    icon: bi bi-globe
  - title: বাংলা version
    url: /bn/linux/apt.html
    icon: bi bi-globe
  - title: català version
    url: /ca/linux/apt.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/apt.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/apt.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/linux/apt.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/apt.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/apt.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/apt.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt

டெபியன் அடிப்படையிலான விநியோகங்களுக்கான தொகுப்பு மேலாண்மை பயன்பாடு.
உபுண்டு பதிப்பு 16.04 மற்றும் அதற்குப் பிந்தைய பதிப்புகளில் ஊடாடும் வகையில் பயன்படுத்தப்படும் போது `apt-get` க்கு மாற்றாக பரிந்துரைக்கப்படுகிறது.
மேலும் விவரத்திற்கு: <https://manpages.debian.org/latest/apt/apt.8.html>.

- கிடைக்கக்கூடிய தொகுப்புகள் மற்றும் பதிப்புகளின் பட்டியலைப் புதுப்பிக்கவும் (மற்ற `apt` கட்டளைகளுக்கு முன் இதை இயக்க பரிந்துரைக்கப்படுகிறது):

`sudo apt update`

- கொடுக்கப்பட்ட தொகுப்பைத் தேடுங்கள்:

`apt search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு</span>

- தொகுப்பிற்கான தகவலைக் காட்டு:

`apt show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு</span>

- தொகுப்பை நிறுவவும் அல்லது கிடைக்கும் சமீபத்திய பதிப்பிற்கு புதுப்பிக்கவும்:

`sudo apt install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு</span>

- ஒரு தொகுப்பை அகற்று ('purge' ஐப் பயன்படுத்தி அதன் உள்ளமைவு கோப்புகளையும் நீக்குகிறது):

`sudo apt remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு</span>

- நிறுவப்பட்ட அனைத்து தொகுப்புகளையும் அவற்றின் புதிய கிடைக்கக்கூடிய பதிப்புகளுக்கு மேம்படுத்தவும்:

`sudo apt upgrade`

- அனைத்து தொகுப்புகளையும் பட்டியலிடுங்கள்:

`apt list`

- நிறுவப்பட்ட தொகுப்புகளை பட்டியலிடுங்கள்:

`apt list --installed`
