---
layout: page
title: netbsd/sed (हिन्दी)
description: "स्क्रिप्ट करने योग्य तरीके से टेक्स्ट संपादित करें।"
content_hash: 82ec29c226c149777a6594df4af19404f802aa09
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/netbsd/sed.html
    icon: bi bi-globe
  - title: español version
    url: /es/netbsd/sed.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/netbsd/sed.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/netbsd/sed.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sed

स्क्रिप्ट करने योग्य तरीके से टेक्स्ट संपादित करें।
देखें: `awk`, `ed`।
अधिक जानकारी: <https://man.netbsd.org/sed.1>।

- सभी इनपुट लाइनों में `apple` (बेसिक regex) के सभी उदाहरणों को `mango` (बेसिक regex) से बदलें और परिणाम को `stdout` पर प्रिंट करें:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आदेश</span>` | sed 's/apple/mango/g'`

- एक विशेष स्क्रिप्ट [f]फाइल निष्पादित करें और परिणाम को `stdout` पर प्रिंट करें:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आदेश</span>` | sed -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्क्रिप्ट.sed/का/पथ</span>

- प्रत्येक फ़ाइल को खोलने में देरी करें जब तक कि एक कमांड जिसमें संबंधित `w` फ़ंक्शन या फ्लैग इनपुट की एक पंक्ति पर लागू नहीं किया जाता है:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आदेश</span>` | sed -fa `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्क्रिप्ट.sed/का/पथ</span>

- GNU [g]regex एक्सटेंशन चालू करें:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आदेश</span>` | sed -fg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्क्रिप्ट.sed/का/पथ</span>

- सभी इनपुट लाइनों में `apple` (एक्सटेंडेड regex) के सभी उदाहरणों को `APPLE` (एक्सटेंडेड regex) से बदलें और परिणाम को `stdout` पर प्रिंट करें:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आदेश</span>` | sed -E 's/(apple)/\U\1/g'`

- केवल पहली पंक्ति को `stdout` पर प्रिंट करें:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आदेश</span>` | sed -n '1p'`

- एक विशेष फ़ाइल में `apple` (बेसिक regex) के सभी उदाहरणों को `mango` (बेसिक regex) से बदलें और मूल फ़ाइल को उसी स्थान पर ओवरराइट करें:

`sed -i 's/apple/mango/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल/का/पथ</span>
