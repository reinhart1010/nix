---
layout: page
title: linux/fdisk (தமிழ்)
description: "பகிர்வு அட்டவணைகள் மற்றும் பகிர்வுகளை ஹார்ட் டிஸ்கில் நிர்வகிப்பதற்கான ஒரு நிரல்."
content_hash: b01136d0066098ebc403eb08dda1b56e94df4e19
last_modified_at: 2023-06-02
related_topics:
  - title: English version
    url: /en/linux/fdisk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/fdisk.html
    icon: bi bi-globe
---
# fdisk

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

- ஒரு வட்டை பகிர்ந்தவுடன், உதவி பட்டியலைத் திறக்கவும்:

`m`
