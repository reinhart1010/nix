---
layout: page
title: windows/choco-new (தமிழ்)
description: "சாக்லேட்டியுடன் புதிய தொகுப்பு விவரக்குறிப்பு கோப்புகளை உருவாக்கவும்."
content_hash: 9aed57922cac28ec984616254d84a980a0637c41
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-new.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-new.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-new.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># choco new

சாக்லேட்டியுடன் புதிய தொகுப்பு விவரக்குறிப்பு கோப்புகளை உருவாக்கவும்.
மேலும் விவரத்திற்கு: <https://chocolatey.org/docs/commands-new>.

- ஒரு புதிய தொகுப்பு எலும்புக்கூட்டை உருவாக்கவும்:

`choco new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு_பெயர்</span>

- ஒரு குறிப்பிட்ட பதிப்பில் புதிய தொகுப்பை உருவாக்கவும்:

`choco new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு_பெயர்</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பதிப்பு</span>

- குறிப்பிட்ட பராமரிப்பாளர் பெயருடன் புதிய தொகுப்பை உருவாக்கவும்:

`choco new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு_பெயர்</span>` --maintainer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பராமரிப்பாளர்_பெயர்</span>

- தனிப்பயன் வெளியீட்டு கோப்பகத்தில் புதிய தொகுப்பை உருவாக்கவும்:

`choco new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு_பெயர்</span>` --output-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">அடைவிற்குப்/பாதை</span>

- குறிப்பிட்ட 32-பிட் மற்றும் 64-பிட் நிறுவி URLகளுடன் புதிய தொகுப்பை உருவாக்கவும்:

`choco புதிய `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு_பெயர்</span>` url="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`" url64="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`"`
