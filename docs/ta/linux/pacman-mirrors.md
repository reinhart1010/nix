---
layout: page
title: linux/pacman-mirrors (தமிழ்)
description: "மஞ்சாரோ லினக்ஸுக்கு பேக்மேன் கண்ணாடி பட்டியலை உருவாக்கவும்."
content_hash: 788e4d528015a18d7c8b8bfa98d83ec7fbb6975b
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/pacman-mirrors.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-mirrors.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-mirrors.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacman-mirrors.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-mirrors.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman-mirrors

மஞ்சாரோ லினக்ஸுக்கு பேக்மேன் கண்ணாடி பட்டியலை உருவாக்கவும்.
பேக்மேன்-கண்ணாடிகள் ஒவ்வொரு ஓட்டத்திற்கும் உங்கள் தரவுத்தளத்தை ஒத்திசைக்க மற்றும் `sudo pacman -Syyu` ஐப் பயன்படுத்தி உங்கள் கணினியைப் புதுப்பிக்க வேண்டும்.
இதையும் பார்க்கவும்: `pacman`.
மேலும் விவரத்திற்கு: <https://wiki.manjaro.org/index.php?title=Pacman-mirrors>.

- இயல்புநிலை அமைப்புகளைப் பயன்படுத்தி ஒரு கண்ணாடி பட்டியலை உருவாக்கவும்:

`sudo pacman-mirrors --fasttrack`

- தற்போதைய கண்ணாடிகளின் நிலையைப் பெறுங்கள்:

`pacman-mirrors --status`

- தற்போதைய கிளையைக் காட்டு:

`pacman-mirrors --get-branch`

- வேறு கிளைக்கு மாறவும்:

`sudo pacman-mirrors --api --set-branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stable|unstable|testing</span>

- உங்கள் நாட்டில் உள்ள கண்ணாடிகளை மட்டும் பயன்படுத்தி, கண்ணாடி பட்டியலை உருவாக்கவும்:

`sudo pacman-mirrors --geoip`
