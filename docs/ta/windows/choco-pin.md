---
layout: page
title: windows/choco-pin (தமிழ்)
description: "சாக்லேட்டியுடன் ஒரு குறிப்பிட்ட பதிப்பில் ஒரு தொகுப்பைப் பின் செய்யவும்."
content_hash: 786ff8f6681b4901a64963ea952e3cbb58affcc4
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-pin.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-pin.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-pin.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-pin.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco pin

சாக்லேட்டியுடன் ஒரு குறிப்பிட்ட பதிப்பில் ஒரு தொகுப்பைப் பின் செய்யவும்.
மேம்படுத்தும் போது பின் செய்யப்பட்ட தொகுப்புகள் தானாகவே தவிர்க்கப்படும்.
மேலும் விவரத்திற்கு: <https://chocolatey.org/docs/commands-pin>.

- பின் செய்யப்பட்ட தொகுப்புகள் மற்றும் அவற்றின் பதிப்புகளின் பட்டியலைக் காண்பி:

`choco pin list`

- ஒரு தொகுப்பை அதன் தற்போதைய பதிப்பில் பின் செய்யவும்:

`choco pin add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு</span>

- ஒரு குறிப்பிட்ட பதிப்பில் ஒரு தொகுப்பைப் பின் செய்யவும்:

`choco pin add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பதிப்பு</span>

- ஒரு குறிப்பிட்ட தொகுப்பிற்கான பின்னை அகற்றவும்:

`choco pin remove --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு</span>
