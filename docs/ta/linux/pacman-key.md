---
layout: page
title: linux/pacman-key (தமிழ்)
description: "பேக்மேனின் கீரிங்கை நிர்வகிக்க GnuPGக்கான ரேப்பர் ஸ்கிரிப்ட் பயன்படுத்தப்படுகிறது."
content_hash: 2bee6ee6007df9c88922713043f43fc818f92d30
last_modified_at: 2023-11-13
related_topics:
  - title: English version
    url: /en/linux/pacman-key.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-key.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-key.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman-key

பேக்மேனின் கீரிங்கை நிர்வகிக்க GnuPGக்கான ரேப்பர் ஸ்கிரிப்ட் பயன்படுத்தப்படுகிறது.
இதையும் பார்க்கவும்: `pacman`.
மேலும் விவரத்திற்கு: <https://man.archlinux.org/man/pacman-key>.

- பேக்மேன் கீரிங்கை துவக்கவும்:

`sudo pacman-key --init`

- இயல்பு ஆர்ச் லினக்ஸ் விசைகளைச் சேர்க்கவும்:

`sudo pacman-key --populate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archlinux</span>

- பொது விசையிலிருந்து விசைகளை பட்டியலிடவும்:

`pacman-key --list-keys`

- குறிப்பிட்ட விசைகளைச் சேர்க்கவும்:

`sudo pacman-key --சேர் `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">விசைக்கோப்பு.gpg/பாதை</span>

- ஒரு முக்கிய சேவையகத்திலிருந்து ஒரு விசையைப் பெறுங்கள்:

`sudo pacman-key --recv-keys "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid|பெயர்|மின்னஞ்சல்</span>`"`

- ஒரு குறிப்பிட்ட விசையின் கைரேகையை அச்சிடுங்கள்:

`pacman-key --finger "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid|பெயர்|மின்னஞ்சல்</span>`"`

- இறக்குமதி செய்யப்பட்ட விசையை உள்நாட்டில் கையொப்பமிடவும்:

`sudo pacman-key --lsign-key "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid|பெயர்|மின்னஞ்சல்</span>`"`

- ஒரு குறிப்பிட்ட விசையை அகற்று:

`sudo pacman-key --delete "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid|பெயர்|மின்னஞ்சல்</span>`"`
