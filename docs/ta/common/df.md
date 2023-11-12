---
layout: page
title: common/df (தமிழ்)
description: "கோப்பு முறைமை வட்டு இட உபயோகத்தின் மேலோட்டத்தை அளிக்கிறது."
content_hash: cbe35d64cdc9cd3ae7d3784168c264a78f223c2e
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/df.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/df.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/df.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/df.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/df.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/df.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/df.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/df.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/df.html
    icon: bi bi-globe
tldri18n_status: 2
---
# df

கோப்பு முறைமை வட்டு இட உபயோகத்தின் மேலோட்டத்தை அளிக்கிறது.
மேலும் விவரத்திற்கு: <https://www.gnu.org/software/coreutils/df>.

- அனைத்து கோப்பு முறைமைகளையும் அவற்றின் வட்டு பயன்பாட்டையும் காண்பி:

`df`

- அனைத்து கோப்பு முறைமைகளையும் அவற்றின் வட்டு பயன்பாட்டையும் மனிதர்கள் படிக்கக்கூடிய வடிவத்தில் காண்பி:

`df -h`

- கொடுக்கப்பட்ட கோப்பு அல்லது கோப்பகத்தைக் கொண்ட கோப்பு முறைமை மற்றும் அதன் வட்டு பயன்பாட்டைக் காண்பி:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு_அல்லது_அடைவு</span>

- இலவச ஐனோட்களின் எண்ணிக்கையில் புள்ளிவிவரங்களைக் காண்பி:

`df -i`

- கோப்பு முறைமைகளைக் காண்பி ஆனால் குறிப்பிட்ட வகைகளை விலக்கவும்:

`df -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">squashfs</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmpfs</span>
