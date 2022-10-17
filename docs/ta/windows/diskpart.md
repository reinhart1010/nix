---
layout: page
title: windows/diskpart (தமிழ்)
description: "வட்டு, தொகுதி மற்றும் பகிர்வு மேலாளர்."
content_hash: 0499f552ae57d99c634b8bd5a1ae296524d27e74
related_topics:
  - title: English version
    url: /en/windows/diskpart.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># diskpart

வட்டு, தொகுதி மற்றும் பகிர்வு மேலாளர்.
மேலும் விவரத்திற்கு: <https://learn.microsoft.com/windows-server/administration/windows-commands/diskpart>.

- `diskpart` ஐ அதன் கட்டளை வரியை உள்ளிட நிர்வாக கட்டளை வரியில் தானாகவே இயக்கவும்:

`diskpart`

- அனைத்து வட்டுகளையும் பட்டியலிடுங்கள்:

`list disk`

- ஒரு தொகுதியைத் தேர்ந்தெடுக்கவும்:

`select volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொகுதி</span>

- தேர்ந்தெடுக்கப்பட்ட தொகுதிக்கு ஒரு இயக்கி கடிதத்தை ஒதுக்கவும்:

`assign letter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கடிதம்</span>

- ஒரு புதிய பகிர்வை உருவாக்கவும்:

`create partition primary`

- தேர்ந்தெடுக்கப்பட்ட தொகுதியை செயல்படுத்தவும்:

`active`

- வட்டு பகுதியிலிருந்து வெளியேறு:

`exit`
