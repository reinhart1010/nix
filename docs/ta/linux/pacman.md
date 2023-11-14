---
layout: page
title: linux/pacman (தமிழ்)
description: "ஆர்ச் லினக்ஸ் தொகுப்பு மேலாளர் பயன்பாடு."
content_hash: 61cd86da4b82cb5178ee97a599d668af1493cb10
last_modified_at: 2023-11-14
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
  - title: Indonesia version
    url: /id/linux/pacman.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/pacman.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman.html
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
  - title: українська version
    url: /uk/linux/pacman.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/pacman.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman

ஆர்ச் லினக்ஸ் தொகுப்பு மேலாளர் பயன்பாடு.
இதையும் பார்க்கவும்: `pacman-database`, `pacman-deptest`, `pacman-files`, `pacman-key`, `pacman-mirrors`, `pacman-query`, `pacman-remove`, `pacman-sync`, `pacman-upgrade`.
மேலும் விவரத்திற்கு: <https://man.archlinux.org/man/pacman.8>.

- அனைத்து தொகுப்புகளையும் ஒத்திசைத்து புதுப்பிக்கவும்:

`sudo pacman -Syu`

- ஒரு புதிய தொகுப்பை நிறுவவும்:

`sudo pacman -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு</span>

- ஒரு தொகுப்பு மற்றும் அதன் சார்புகளை அகற்றவும்:

`sudo pacman -Rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு</span>

- ஒரு குறிப்பிட்ட கோப்பைக் கொண்ட தொகுப்புகளுக்கான தரவுத்தளத்தில் தேடவும்:

`pacman -F "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_பெயர்</span>`"`

- நிறுவப்பட்ட தொகுப்புகள் மற்றும் பதிப்புகளை பட்டியலிடுங்கள்:

`pacman -Q`

- வெளிப்படையாக நிறுவப்பட்ட தொகுப்புகள் மற்றும் பதிப்புகளை மட்டும் பட்டியலிடுங்கள்:

`pacman -Qe`

- அனாதை தொகுப்புகளை பட்டியலிடு (சார்புகளாக நிறுவப்பட்டது ஆனால் உண்மையில் எந்த தொகுப்பிற்கும் தேவையில்லை):

`pacman -Qtdq`

- முழு பேக்மேன் தற்காலிக சேமிப்பையும் காலி செய்யவும்:

`sudo pacman -Scc`
