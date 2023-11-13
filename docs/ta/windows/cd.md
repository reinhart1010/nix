---
layout: page
title: windows/cd (தமிழ்)
description: "தற்போதைய வேலை கோப்பகத்தைக் காட்டவும் அல்லது வேறு கோப்பகத்திற்கு நகர்த்தவும்."
content_hash: 5e2fa91bb38c321689d82187de5f210010258939
last_modified_at: 2023-11-13
related_topics:
  - title: বাংলা version
    url: /bn/windows/cd.html
    icon: bi bi-globe
  - title: čeština version
    url: /cs/windows/cd.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/windows/cd.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/cd.html
    icon: bi bi-globe
  - title: español version
    url: /es/windows/cd.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/cd.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/cd.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/cd.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/cd.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/cd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/cd.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/cd.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/windows/cd.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cd

தற்போதைய வேலை கோப்பகத்தைக் காட்டவும் அல்லது வேறு கோப்பகத்திற்கு நகர்த்தவும்.
PowerShell இல், இந்தக் கட்டளையானது `Set-Location` என்பதன் மாற்றுப் பெயராகும். இந்த ஆவணம் `cd` இன் கட்டளை வரியில் (`cmd`) பதிப்பை அடிப்படையாகக் கொண்டது.
மேலும் விவரத்திற்கு: <https://learn.microsoft.com/windows-server/administration/windows-commands/cd>.

- சமமான PowerShell கட்டளையின் ஆவணங்களைக் காண்க:

`tldr set-location`

- தற்போதைய கோப்பகத்தின் பாதையைக் காட்டு:

`cd`

- அதே வட்டில் ஒரு குறிப்பிட்ட கோப்பகத்திற்குச் செல்லவும்:

`cd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">அடைவிற்குப்\பாதை</span>

- வேறு [d] இயக்ககத்தில் உள்ள குறிப்பிட்ட கோப்பகத்திற்குச் செல்லவும்:

`cd /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">அடைவிற்குப்\பாதை</span>

- தற்போதைய கோப்பகத்தின் பெற்றோருக்குச் செல்லவும்:

`cd ..`

- தற்போதைய பயனரின் முகப்பு கோப்பகத்திற்குச் செல்லவும்:

`cd %userprofile%`

- தற்போதைய வட்டில் வேருக்கு செல்லவும்:

`cd \`
