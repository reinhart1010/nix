---
layout: page
title: linux/lsusb (हिन्दी)
description: "यूएसबी बसों और उनसे जुड़े उपकरणों के बारे में जानकारी प्रदर्शित करें।"
content_hash: 1055e456ba2f4142df814b647d50434cea26de6d
related_topics:
  - title: català version
    url: /ca/linux/lsusb.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/lsusb.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/lsusb.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/lsusb.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># lsusb

यूएसबी बसों और उनसे जुड़े उपकरणों के बारे में जानकारी प्रदर्शित करें।
अधिक जानकारी: <https://manned.org/lsusb>.

- उपलब्ध सभी USB उपकरणों की सूची बनाएं:

`lsusb`

- USB पदानुक्रम को एक ट्री के रूप में सूचीबद्ध करें:

`lsusb -t`

- USB उपकरणों के बारे में विस्तारित जानकारी की सूची बनाएं:

`lsusb --verbose`

- USB डिवाइस के बारे में विस्तृत जानकारी की सूची बनाएं:

`lsusb -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपकरण</span>

- केवल निर्दिष्ट विक्रेता और उत्पाद आईडी वाले उपकरणों की सूची बनाएं:

`lsusb -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">वेंडर</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उत्पाद</span>
