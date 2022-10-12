---
layout: page
title: linux/lsblk (हिन्दी)
description: "उपकरणों के बारे में जानकारी सूचीबद्ध करता है।"
content_hash: 2c57c58759baabeaec724189173abb7669d6844e
related_topics:
  - title: English version
    url: /en/linux/lsblk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/lsblk.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># lsblk

उपकरणों के बारे में जानकारी सूचीबद्ध करता है।
अधिक जानकारी: <https://manned.org/lsblk>.

- सभी भंडारण उपकरणों को ट्री-समान प्रारूप में सूचीबद्ध करें:

`lsblk`

- खाली उपकरणों को भी सूचीबद्ध करें:

`lsblk -a`

- मानव-पठनीय प्रारूप के बजाय SIZE कॉलम को बाइट्स में प्रिंट करें:

`lsblk -b`

- फाइल सिस्टम के बारे में आउटपुट जानकारी:

`lsblk -f`

- ट्री फॉर्मेटिंग के लिए ASCII वर्णों का प्रयोग करें:

`lsblk -i`

- ब्लॉक-डिवाइस टोपोलॉजी के बारे में आउटपुट जानकारी:

`lsblk -t`

- प्रमुख उपकरण संख्याओं की अल्पविराम से अलग की गई सूची द्वारा निर्दिष्ट उपकरणों को बाहर करें:

`lsblk -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,7</span>

- कॉलम की अल्पविराम से अलग की गई सूची का उपयोग करके एक अनुकूलित सारांश प्रदर्शित करें:

`lsblk --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">NAME</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SERIAL</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MODEL</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TRAN</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TYPE</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIZE</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FSTYPE</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MOUNTPOINT</span>
