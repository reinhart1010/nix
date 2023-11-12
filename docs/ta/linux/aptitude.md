---
layout: page
title: linux/aptitude (தமிழ்)
description: "டெபியன் மற்றும் உபுண்டு தொகுப்பு மேலாண்மை பயன்பாடு."
content_hash: 20792ecd236167c52d9ecc2de3a40c89ef21a202
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/aptitude.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/aptitude.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/aptitude.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/aptitude.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/aptitude.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/aptitude.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/aptitude.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/aptitude.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/aptitude.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aptitude

டெபியன் மற்றும் உபுண்டு தொகுப்பு மேலாண்மை பயன்பாடு.
மேலும் விவரத்திற்கு: <https://manpages.debian.org/latest/aptitude/aptitude.8.html>.

- கிடைக்கும் தொகுப்புகள் மற்றும் பதிப்புகளின் பட்டியலை ஒத்திசைக்கவும். அடுத்தடுத்த `aptitude` கட்டளைகளை இயக்கும் முன், இதை முதலில் இயக்க வேண்டும்:

`aptitude update`

- புதிய தொகுப்பு மற்றும் அதன் சார்புகளை நிறுவவும்:

`aptitude install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு</span>

- தொகுப்பைத் தேடுங்கள்:

`aptitude search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு</span>

- நிறுவப்பட்ட தொகுப்பைத் தேடவும் (`?installed` தகுதி தேடல் சொல்:

`aptitude search '?installed(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு</span>`)'`

- ஒரு நிரல்தொகுப்பு மற்றும் அதை சார்ந்த அனைத்து தொகுப்புகளையும் அகற்றவும்:

`aptitude remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு</span>

- நிறுவப்பட்ட தொகுப்புகளை புதிய கிடைக்கக்கூடிய பதிப்புகளுக்கு மேம்படுத்தவும்:

`aptitude upgrade`

- நிறுவப்பட்ட தொகுப்புகளை மேம்படுத்தவும் (போன்ற `aptitude upgrade`) வழக்கற்றுப் போன தொகுப்புகளை அகற்றுதல் மற்றும் புதிய நிரல்தொகுப்பு சார்புகளை சந்திக்க கூடுதல் தொகுப்புகளை நிறுவுதல் உட்பட:

`aptitude full-upgrade`

- தானாக மேம்படுத்தப்படுவதைத் தடுக்க, நிறுவப்பட்ட தொகுப்பை நிறுத்தி வைக்கவும்:

`aptitude hold '?installed(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு</span>`)'`
