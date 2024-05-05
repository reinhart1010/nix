---
layout: page
title: common/ack (தமிழ்)
description: "டெவலப்பர்களுக்காக உகந்ததாக `grep` போன்ற ஒரு தேடல் கருவி."
content_hash: 9440ac54baed220f00ea409b46e72340166cd801
last_modified_at: 2024-05-05
related_topics:
  - title: বাংলা version
    url: /bn/common/ack.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ack.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ack.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ack.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ack.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ack.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ack.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ack.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/common/ack.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/ack.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ack.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ack.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ack.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ack

டெவலப்பர்களுக்காக உகந்ததாக `grep` போன்ற ஒரு தேடல் கருவி.
மேலும் பார்க்கவும்: `rg`, இது மிகவும் வேகமானது.
மேலும் விவரத்திற்கு: <https://beyondgrep.com/documentation>.

- தற்போதைய கோப்பகத்தில் ஒரு சரம் அல்லது வழக்கமான வெளிப்பாடு உள்ள கோப்புகளை மீண்டும் மீண்டும் தேடவும்:

`ack "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தேடல்_முறை</span>`"`

- கேஸ்-சென்சிட்டிவ் பேட்டர்னைத் தேடுங்கள்:

`ack --ignore-case "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தேடல்_முறை</span>`"`

- ஒரு வடிவத்துடன் பொருந்தக்கூடிய வரிகளைத் தேடவும், [o]பொருந்திய உரையை மட்டும் அச்சிடவும் மற்றும் வரியின் மீதமுள்ளவை அல்ல:

`ack -o "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தேடல்_முறை</span>`"`

- ஒரு குறிப்பிட்ட வகை கோப்புகளுக்கான தேடலை வரம்பிடவும்:

`ack --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தேடல்_முறை</span>`"`

- ஒரு குறிப்பிட்ட வகை கோப்புகளில் தேட வேண்டாம்:

`ack --type no`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தேடல்_முறை</span>`"`

- காணப்பட்ட மொத்த பொருத்தங்களின் எண்ணிக்கையை எண்ணுங்கள்:

`ack --count --no-filename "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தேடல்_முறை</span>`"`

- ஒவ்வொரு கோப்பிற்கும் கோப்பு பெயர்கள் மற்றும் பொருத்தங்களின் எண்ணிக்கையை மட்டும் அச்சிடவும்:

`ack --count --files-with-matches "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தேடல்_முறை</span>`"`

- `--type` உடன் பயன்படுத்தக்கூடிய அனைத்து மதிப்புகளையும் பட்டியலிடுங்கள்:

`ack --help-types`
