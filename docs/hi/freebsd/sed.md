---
layout: page
title: freebsd/sed (हिन्दी)
description: "स्क्रिप्ट करने योग्य तरीके से टेक्स्ट संपादित करें।"
content_hash: 261fedf46900714991c6f97e56460269ecd17f2d
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/freebsd/sed.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/freebsd/sed.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/freebsd/sed.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/freebsd/sed.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sed

स्क्रिप्ट करने योग्य तरीके से टेक्स्ट संपादित करें।
देखें: `awk`, `ed`।
अधिक जानकारी: <https://www.freebsd.org/cgi/man.cgi?sed>।

- सभी इनपुट लाइनों में `apple` (बेसिक regex) की सभी उपस्थिति को `mango` (बेसिक regex) से बदलें और परिणाम को `stdout` पर प्रिंट करें:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आदेश</span>` | sed 's/apple/mango/g'`

- एक विशेष स्क्रिप्ट [f]फाइल का निष्पादन करें और परिणाम को `stdout` पर प्रिंट करें:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आदेश</span>` | sed -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्क्रिप्ट.sed/का/पथ</span>

- प्रत्येक फ़ाइल को खोलने में देरी करें जब तक कि एक कमांड जिसमें संबंधित `w` फ़ंक्शन या ध्वज लागू नहीं किया जाता है:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आदेश</span>` | sed -fa `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्क्रिप्ट.sed/का/पथ</span>

- सभी इनपुट लाइनों में `apple` (एक्सटेंडेड regex) की सभी उपस्थिति को `APPLE` (एक्सटेंडेड regex) से बदलें और परिणाम को `stdout` पर प्रिंट करें:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आदेश</span>` | sed -E 's/(apple)/\U\1/g'`

- केवल पहली पंक्ति को `stdout` पर प्रिंट करें:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आदेश</span>` | sed -n '1p'`

- एक विशेष फ़ाइल में सभी `apple` (बेसिक regex) की उपस्थिति को `mango` (बेसिक regex) से बदलें और मूल फ़ाइल को उसी स्थान पर ओवरराइट करें:

`sed -i 's/apple/mango/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल/का/पथ</span>
