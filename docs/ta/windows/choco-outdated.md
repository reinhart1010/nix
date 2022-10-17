---
layout: page
title: windows/choco-outdated (தமிழ்)
description: "சாக்லேட்டியுடன் காலாவதியான தொகுப்புகளைச் சரிபார்க்கவும்."
content_hash: 9cc64fc56d433120d85ee865926dbcd6f04223ed
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-outdated.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-outdated.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-outdated.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># choco outdated

சாக்லேட்டியுடன் காலாவதியான தொகுப்புகளைச் சரிபார்க்கவும்.
மேலும் விவரத்திற்கு:  <https://chocolatey.org/docs/commands-outdated>.

- காலாவதியான தொகுப்புகளின் பட்டியலை அட்டவணை வடிவத்தில் காண்பி:

`choco outdated`

- வெளியீட்டில் பின் செய்யப்பட்ட தொகுப்புகளை புறக்கணிக்கவும்:

`choco outdated --ignore-pinned`

- தொகுப்புகளை சரிபார்க்க தனிப்பயன் மூலத்தைக் குறிப்பிடவும்:

`choco outdated --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_url|alias</span>

- அங்கீகாரத்திற்கான பயனர்பெயர் மற்றும் கடவுச்சொல்லை வழங்கவும்:

`choco outdated --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பயனர்பெயர்</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கடவுச்சொல்</span>
