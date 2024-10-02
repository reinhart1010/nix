---
layout: page
title: linux/lspci (हिन्दी)
description: "सभी PCI उपकरणों की सूची दिखाएं।"
content_hash: 46c5cd6cd9486904dbb723ac12cf7cffb6954b21
last_modified_at: 2024-10-02
related_topics:
  - title: English version
    url: /en/linux/lspci.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/linux/lspci.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/lspci.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/lspci.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># lspci

सभी PCI उपकरणों की सूची दिखाएं।
अधिक जानकारी: <https://manned.org/lspci>।

- उपकरणों की संक्षिप्त सूची दिखाएं:

`lspci`

- अतिरिक्त जानकारी प्रदर्शित करें:

`lspci -v`

- प्रत्येक उपकरण को संभालने वाले ड्राइवर और मॉड्यूल प्रदर्शित करें:

`lspci -k`

- एक विशिष्ट उपकरण दिखाएं:

`lspci -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">00:18.3</span>

- जानकारी को पठनीय रूप में डंप करें:

`lspci -vm`
