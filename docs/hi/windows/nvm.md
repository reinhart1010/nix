---
layout: page
title: windows/nvm (हिन्दी)
description: "Node.js के संस्करणों को स्थापित, अनइंस्टॉल या स्विच करें।"
content_hash: f936700ed271dd30a2ede6907fcefac8a7acc3f8
last_modified_at: 2024-11-26
related_topics:
  - title: English version
    url: /en/windows/nvm.html
    icon: bi bi-globe
  - title: español version
    url: /es/windows/nvm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/nvm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/nvm.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/nvm.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/nvm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/nvm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nvm

Node.js के संस्करणों को स्थापित, अनइंस्टॉल या स्विच करें।
"12.8" या "v16.13.1" जैसे संस्करण नंबर और "stable", "system" आदि जैसे लेबल का समर्थन करता है।
अधिक जानकारी: <https://github.com/coreybutler/nvm-windows>।

- Node.js का एक विशिष्ट संस्करण स्थापित करें:

`nvm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">नोड_संस्करण</span>

- Node.js का डिफ़ॉल्ट संस्करण सेट करें (यह Administrator के रूप में चलाना आवश्यक है):

`nvm use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">नोड_संस्करण</span>

- सभी उपलब्ध Node.js संस्करणों की सूची बनाएं और डिफ़ॉल्ट संस्करण को हाइलाइट करें:

`nvm list`

- सभी दूरस्थ Node.js संस्करणों की सूची बनाएं:

`nvm ls-remote`

- दिए गए Node.js संस्करण को अनइंस्टॉल करें:

`nvm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">नोड_संस्करण</span>
