---
layout: page
title: windows/rmdir (தமிழ்)
description: "ஒரு கோப்பகம் மற்றும் அதன் உள்ளடக்கங்களை அகற்றவும்."
content_hash: 0313f0bf3750b06537cf091a613e47fddd023a6e
last_modified_at: 2023-11-13
related_topics:
  - title: English version
    url: /en/windows/rmdir.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/rmdir.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/rmdir.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/rmdir.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rmdir

ஒரு கோப்பகம் மற்றும் அதன் உள்ளடக்கங்களை அகற்றவும்.
PowerShell இல், இந்த கட்டளை `Remove-Item` என்பதன் மாற்றுப் பெயராகும். இந்த ஆவணம் `rmdir` இன் கட்டளை வரியில் (`cmd`) பதிப்பை அடிப்படையாகக் கொண்டது.
மேலும் விவரத்திற்கு: <https://learn.microsoft.com/windows-server/administration/windows-commands/rmdir>.

- சமமான PowerShell கட்டளையின் ஆவணங்களைக் காண்க:

`tldr remove-item`

- வெற்று கோப்பகத்தை அகற்றவும்:

`rmdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">அடைவிற்குப்/பாதை</span>

- ஒரு கோப்பகத்தையும் அதன் உள்ளடக்கங்களையும் மீண்டும் மீண்டும் அகற்றவும்:

`rmdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">அடைவிற்குப்/பாதை</span>` /s`

- மீண்டும் மீண்டும் கேட்காமல் ஒரு கோப்பகத்தையும் அதன் உள்ளடக்கங்களையும் அகற்றவும்:

`rmdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">அடைவிற்குப்/பாதை</span>` /s /q`
