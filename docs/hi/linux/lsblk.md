---
layout: page
title: linux/lsblk (हिन्दी)
description: "उपकरणों के बारे में जानकारी सूचीबद्ध करता है।"
content_hash: 54727a2d2f7b2816762ba2e0666b31f6e5e2711b
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/lsblk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/lsblk.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/linux/lsblk.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/lsblk.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/lsblk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lsblk

उपकरणों के बारे में जानकारी सूचीबद्ध करता है।
अधिक जानकारी: <https://manned.org/lsblk>।

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
