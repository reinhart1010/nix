---
layout: page
title: linux/pacman-remove (தமிழ்)
description: "ஆர்ச் லினக்ஸ் தொகுப்பு மேலாளர் பயன்பாடு."
content_hash: 3d3d7cd825bd10f11e91018a31ac15c9088b7eaf
last_modified_at: 2023-11-13
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-remove.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-remove.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-remove.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman-remove.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-remove.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-remove.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --remove

ஆர்ச் லினக்ஸ் தொகுப்பு மேலாளர் பயன்பாடு.
இதையும் பார்க்கவும்: `pacman`.
மேலும் விவரத்திற்கு: <https://man.archlinux.org/man/pacman.8>.

- ஒரு தொகுப்பு மற்றும் அதன் சார்புகளை அகற்றவும்:

`sudo pacman --remove --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு</span>

- ஒரு தொகுப்பு மற்றும் அதன் சார்புகள் மற்றும் கட்டமைப்பு கோப்புகள் இரண்டையும் அகற்றவும்:

`sudo pacman --remove --recursive --nosave `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு</span>

- கேட்காமல் ஒரு தொகுப்பை அகற்றவும்:

`sudo pacman --remove --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு</span>

- அனாதை தொகுப்புகளை அகற்று (சார்புகளாக நிறுவப்பட்டது ஆனால் எந்த தொகுப்பிற்கும் தேவையில்லை):

`sudo pacman --remove --recursive --nosave $(pacman --query --unrequired --deps --quiet)`

- ஒரு தொகுப்பு மற்றும் அதைச் சார்ந்த அனைத்து தொகுப்புகளையும் அகற்றவும்:

`sudo pacman --remove --cascade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு</span>

- பாதிக்கப்படக்கூடிய தொகுப்புகளை பட்டியலிடுங்கள் (எந்த தொகுப்புகளையும் அகற்றாது):

`pacman --remove --print `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு</span>

- இந்த துணைக் கட்டளைக்கான உதவியைக் காட்டு:

`pacman --remove --help`
