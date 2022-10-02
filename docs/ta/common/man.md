---
layout: page
title: common/man (தமிழ்)
description: "கையேடு பக்கங்களை வடிவமைத்து காட்டவும்."
content_hash: e2b23e209455ec71764056ec561d4b1a62602efb
related_topics:
  - title: English version
    url: /en/common/man.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/man.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/man.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/man.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># man

கையேடு பக்கங்களை வடிவமைத்து காட்டவும்.
மேலும் விவரத்திற்கு: <https://www.man7.org/linux/man-pages/man1/man.1.html>.

- ஒரு கட்டளைக்கான மேன் பக்கத்தைக் காண்பி:

`man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கட்டளை</span>

- பிரிவு 7 இலிருந்து ஒரு கட்டளைக்கான மேன் பக்கத்தைக் காண்பி:

`man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கட்டளை</span>

- கட்டளைக்கு கிடைக்கக்கூடிய அனைத்து பிரிவுகளையும் பட்டியலிடுங்கள்:

`man -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கட்டளை</span>

- மேன்பக்கங்களுக்காகத் தேடப்பட்ட பாதையைக் காண்பி:

`man --path`

- மேன்பேஜைக் காட்டிலும் மேன்பேஜின் இருப்பிடத்தைக் காண்பி:

`man -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கட்டளை</span>

- ஒரு குறிப்பிட்ட மொழியைப் பயன்படுத்தி மேன் பக்கத்தைக் காண்பி:

`man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கட்டளை</span>` --locale=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மொழி</span>

- தேடல் சரம் கொண்ட மேன் பக்கங்களைத் தேடவும்:

`man -k "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தேடல்_சரம்</span>`"`
