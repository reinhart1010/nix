---
layout: page
title: linux/pacman-sync (தமிழ்)
description: "ஆர்ச் லினக்ஸ் தொகுப்பு மேலாளர் பயன்பாடு."
content_hash: 3d617b406e9e4881d1c3366c435ea8d7a50fd9f8
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-sync.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-sync.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-sync.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman-sync.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-sync.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-sync.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --sync

ஆர்ச் லினக்ஸ் தொகுப்பு மேலாளர் பயன்பாடு.
இதையும் பார்க்கவும்: `pacman`.
மேலும் விவரத்திற்கு: <https://man.archlinux.org/man/pacman.8>.

- ஒரு புதிய தொகுப்பை நிறுவவும்:

`sudo pacman --sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு_பெயர்</span>

- அனைத்து தொகுப்புகளையும் ஒத்திசைத்து புதுப்பிக்கவும் (தொகுப்புகளைப் பதிவிறக்குவதற்கு `--downloadonly` சேர்க்கவும், அவற்றைப் புதுப்பிக்க வேண்டாம்):

`sudo pacman --sync --refresh --sysupgrade`

- அனைத்து தொகுப்புகளையும் புதுப்பித்து, கேட்காமல் புதிய ஒன்றை நிறுவவும்:

`sudo pacman --sync --refresh --sysupgrade --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு_பெயர்</span>

- வழக்கமான வெளிப்பாடு அல்லது முக்கிய சொல்லுக்கு தொகுப்பு தரவுத்தளத்தில் தேடவும்:

`pacman --sync --தேடல் "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தேடல்_முறை</span>`"`

- தொகுப்பு பற்றிய தகவலைக் காட்டு:

`pacman --sync --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு_பெயர்</span>

- தொகுப்பு புதுப்பிப்பின் போது முரண்பட்ட கோப்புகளை மேலெழுதவும்:

`sudo pacman --sync --refresh --sysupgrade --ஓவர்ரைட் `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு</span>

- அனைத்து தொகுப்புகளையும் ஒத்திசைத்து புதுப்பிக்கவும், ஆனால் ஒரு குறிப்பிட்ட தொகுப்பை புறக்கணிக்கவும் (ஒருமுறைக்கு மேல் பயன்படுத்தலாம்):

`sudo pacman --sync --refresh --sysupgrade --ignor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொகுப்பு_பெயர்</span>

- நிறுவப்படாத தொகுப்புகள் மற்றும் பயன்படுத்தப்படாத களஞ்சியங்களை தற்காலிக சேமிப்பிலிருந்து அகற்றவும் (அனைத்து தொகுப்புகளையும் சுத்தம் செய்ய இரண்டு `--clean` கொடிகளைப் பயன்படுத்தவும்):

`sudo pacman --sync --clean`
