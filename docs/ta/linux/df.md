---
layout: page
title: linux/df (தமிழ்)
description: "கோப்பு முறைமை வட்டு இட உபயோகத்தின் மேலோட்டத்தை அளிக்கிறது."
content_hash: 6a17238e78b0ffc7abff58909ef3f8d21809d45a
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/df.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/linux/df.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/df.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/df.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/df.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># df

கோப்பு முறைமை வட்டு இட உபயோகத்தின் மேலோட்டத்தை அளிக்கிறது.
மேலும் விவரத்திற்கு: <https://www.gnu.org/software/coreutils/manual/html_node/df-invocation.html>.

- அனைத்து கோப்பு முறைமைகளையும் அவற்றின் வட்டு பயன்பாட்டையும் காண்பி:

`df`

- அனைத்து கோப்பு முறைமைகளையும் அவற்றின் வட்டு பயன்பாட்டையும் மனிதர்கள் படிக்கக்கூடிய வடிவத்தில் காண்பி:

`df -h`

- கொடுக்கப்பட்ட கோப்பு அல்லது கோப்பகத்தைக் கொண்ட கோப்பு முறைமை மற்றும் அதன் வட்டு பயன்பாட்டைக் காண்பி:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_அல்லது_அடைவு/பாதை</span>

- இலவச ஐனோட்களின் எண்ணிக்கையில் புள்ளிவிவரங்களைக் காண்பி:

`df -i`

- கோப்பு முறைமைகளைக் காண்பி ஆனால் குறிப்பிட்ட வகைகளை விலக்கவும்:

`df -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">squashfs</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmpfs</span>
