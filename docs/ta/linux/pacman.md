---
layout: page
title: linux/pacman (தமிழ்)
description: "ஆர்ச் லினக்ஸ் தொகுப்பு மேலாளர் பயன்பாடு."
content_hash: 528f5c4a6bd20f02b36c8c283279ffcb97ac1dbf
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/pacman.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacman.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/pacman.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/pacman.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pacman

ஆர்ச் லினக்ஸ் தொகுப்பு மேலாளர் பயன்பாடு.
`pacman sync` போன்ற சில துணைக் கட்டளைகள் அவற்றின் சொந்த பயன்பாட்டு ஆவணங்களைக் கொண்டுள்ளன.
மேலும் விவரத்திற்கு: <https://man.archlinux.org/man/pacman.8>.

- அனைத்து தொகுப்புகளையும் ஒத்திசைத்து புதுப்பிக்கவும்:

`sudo pacman -Syu`

- ஒரு புதிய தொகுப்பை நிறுவவும்:

`sudo pacman -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு_பெயர்</span>

- ஒரு தொகுப்பு மற்றும் அதன் சார்புகளை அகற்றவும்:

`சுடோ பேக்மேன் -ரூ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு_பெயர்</span>

- வழக்கமான வெளிப்பாடு அல்லது முக்கிய சொல்லுக்கு தொகுப்பு தரவுத்தளத்தில் தேடவும்:

`pacman -Ss "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தேடல்_முறை</span>`"`

- நிறுவப்பட்ட தொகுப்புகள் மற்றும் பதிப்புகளை பட்டியலிடுங்கள்:

`pacman -Q`

- வெளிப்படையாக நிறுவப்பட்ட தொகுப்புகள் மற்றும் பதிப்புகளை மட்டும் பட்டியலிடுங்கள்:

`pacman -Qe`

- அனாதை தொகுப்புகளை பட்டியலிடு (சார்புகளாக நிறுவப்பட்டது ஆனால் உண்மையில் எந்த தொகுப்பிற்கும் தேவையில்லை):

`pacman -Qtdq`

- முழு பேக்மேன் தற்காலிக சேமிப்பையும் காலி செய்யவும்:

`sudo pacman -Scc`