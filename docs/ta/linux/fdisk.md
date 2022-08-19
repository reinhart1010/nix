---
layout: page
title: linux/fdisk (தமிழ்)
description: "பகிர்வு அட்டவணைகள் மற்றும் பகிர்வுகளை ஹார்ட் டிஸ்கில் நிர்வகிப்பதற்கான ஒரு நிரல்."
content_hash: 60176e8692d5505f77a6b06be199281c2b9faddb
related_topics:
  - title: English version
    url: /en/linux/fdisk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/fdisk.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># fdisk

பகிர்வு அட்டவணைகள் மற்றும் பகிர்வுகளை ஹார்ட் டிஸ்கில் நிர்வகிப்பதற்கான ஒரு நிரல்.
மேலும் பார்க்கவும்: `partprobe`.
மேலும் விவரத்திற்கு: <https://manned.org/fdisk>.

- பகிர்வுகளின் பட்டியல்:

`sudo fdisk -l`

- பகிர்வு கையாளுதலைத் தொடங்கவும்:

`sudo fdisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- ஒரு வட்டை பகிர்ந்தவுடன், ஒரு பகிர்வை உருவாக்கவும்:

`n`

- ஒரு வட்டை பகிர்ந்தவுடன், நீக்க ஒரு பகிர்வை தேர்ந்தெடுக்கவும்:

`d`

- ஒரு வட்டை பகிர்ந்தவுடன், பகிர்வு அட்டவணையைப் பார்க்கவும்:

`p`

- ஒரு வட்டை பகிர்ந்தவுடன், செய்யப்பட்ட மாற்றங்களை எழுதவும்:

`w`

- ஒரு வட்டை பகிர்ந்தவுடன், செய்யப்பட்ட மாற்றங்களை நிராகரிக்கவும்:

`q`

- ஒரு வட்டை பகிர்ந்தவுடன், உதவி மெனுவைத் திறக்கவும்:

`m`
