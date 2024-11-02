---
layout: page
title: openbsd/sed (हिन्दी)
description: "स्क्रिप्ट करने योग्य तरीके से पाठ संपादित करें।"
content_hash: 10af411e651d223592d0b9bf4a638b858fc59da6
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/openbsd/sed.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/openbsd/sed.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/openbsd/sed.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/openbsd/sed.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/openbsd/sed.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sed

स्क्रिप्ट करने योग्य तरीके से पाठ संपादित करें।
देखें: `awk`, `ed`।
अधिक जानकारी: <https://man.openbsd.org/sed.1>।

- सभी इनपुट पंक्तियों में सभी `apple` (बुनियादी regex) घटनाओं को `mango` (बुनियादी regex) के साथ बदलें और परिणाम को `stdout` पर प्रिंट करें:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आदेश</span>` | sed 's/apple/mango/g'`

- एक विशेष स्क्रिप्ट [f]फाइल को निष्पादित करें और परिणाम को `stdout` पर प्रिंट करें:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आदेश</span>` | sed -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पथ/से/स्क्रिप्ट.sed</span>

- प्रत्येक फ़ाइल को खोलने में देरी करें जब तक कि एक आदेश जिसमें संबंधित `w` कार्य या फ्लैग लागू नहीं होता है:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आदेश</span>` | sed -fa `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पथ/से/स्क्रिप्ट.sed</span>

- सभी इनपुट पंक्तियों में सभी `apple` (विस्तारित regex) घटनाओं को `APPLE` (विस्तारित regex) के साथ बदलें और परिणाम को `stdout` पर प्रिंट करें:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आदेश</span>` | sed -E 's/(apple)/\U\1/g'`

- केवल पहली पंक्ति को `stdout` पर प्रिंट करें:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आदेश</span>` | sed -n '1p'`

- एक विशेष फ़ाइल में सभी `apple` (बुनियादी regex) घटनाओं को `mango` (बुनियादी regex) के साथ बदलें और मूल फ़ाइल को उसी स्थान पर अधिलेखित करें:

`sed -i 's/apple/mango/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पथ/से/फाइल</span>
