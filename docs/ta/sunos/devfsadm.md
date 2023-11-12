---
layout: page
title: sunos/devfsadm (தமிழ்)
description: "`/dev` க்கான நிர்வாக கட்டளை. `/dev` பெயர்வெளியை பராமரிக்கிறது."
content_hash: 7693369d71186853359a20e5e66a41790505d558
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/sunos/devfsadm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/devfsadm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/devfsadm.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/sunos/devfsadm.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/devfsadm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# devfsadm

`/dev` க்கான நிர்வாக கட்டளை. `/dev` பெயர்வெளியை பராமரிக்கிறது.
மேலும் விவரத்திற்கு: <https://www.unix.com/man-page/sunos/1m/devfsadm>.

- புதிய டிஸ்க்குகளை ஸ்கேன் செய்யவும்:

`devfsadm -c disk`

- தொங்கும் /தேவ் இணைப்புகளை சுத்தம் செய்து புதிய சாதனத்தை ஸ்கேன் செய்யவும்:

`devfsadm -C -v`

- ட்ரை-ரன் - என்ன மாற்றப்படும் என்பதை வெளியீடு ஆனால் எந்த மாற்றமும் செய்யாது:

`devfsadm -C -v -n`
