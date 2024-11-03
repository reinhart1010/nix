---
layout: page
title: openbsd/sed (हिन्दी)
description: "स्क्रिप्ट करने योग्य तरीके से पाठ संपादित करें।"
content_hash: d4ea9e9248467b0df0de31bc493b8a5862911bb4
last_modified_at: 2024-11-03
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
tldri18n_status: 2
---
# sed

स्क्रिप्ट करने योग्य तरीके से पाठ संपादित करें।
देखें: `awk`, `ed`।
अधिक जानकारी: <https://man.openbsd.org/sed.1>।

- सभी इनपुट पंक्तियों में सभी `apple` (बुनियादी regex) घटनाओं को `mango` (बुनियादी regex) के साथ बदलें और परिणाम को `stdout` पर प्रिंट करें:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आदेश</span>` | sed 's/apple/mango/g'`

- एक विशेष स्क्रिप्ट [f]फाइल को निष्पादित करें और परिणाम को `stdout` पर प्रिंट करें:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आदेश</span>` | sed -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्क्रिप्ट.sed/का/पथ</span>

- प्रत्येक फ़ाइल को खोलने में देरी करें जब तक कि एक आदेश जिसमें संबंधित `w` कार्य या फ्लैग लागू नहीं होता है:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आदेश</span>` | sed -fa `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्क्रिप्ट.sed/का/पथ</span>

- सभी इनपुट पंक्तियों में सभी `apple` (विस्तारित regex) घटनाओं को `APPLE` (विस्तारित regex) के साथ बदलें और परिणाम को `stdout` पर प्रिंट करें:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आदेश</span>` | sed -E 's/(apple)/\U\1/g'`

- केवल पहली पंक्ति को `stdout` पर प्रिंट करें:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आदेश</span>` | sed -n '1p'`

- एक विशेष फ़ाइल में सभी `apple` (बुनियादी regex) घटनाओं को `mango` (बुनियादी regex) के साथ बदलें और मूल फ़ाइल को उसी स्थान पर अधिलेखित करें:

`sed -i 's/apple/mango/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल/का/पथ</span>
