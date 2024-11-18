---
layout: page
title: windows/choco-pin (हिन्दी)
description: "चॉकलेट के साथ एक संस्करण पर एक पैकेज पिन करें।"
content_hash: 36ed42e49482373608cf05c41723871f757950b7
last_modified_at: 2024-11-18
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-pin.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-pin.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/choco-pin.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-pin.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-pin.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-pin.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/choco-pin.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># choco pin

चॉकलेट के साथ एक संस्करण पर एक पैकेज पिन करें।
पिन किए गए पैकेज को अपग्रेड करते समय स्वचालित रूप से छोड़ दिया जाता है।
अधिक जानकारी: <https://chocolatey.org/docs/commands-pin>।

- पिन किए गए पैकेज और उनके संस्करणों की एक सूची प्रदर्शित करें:

`choco pin list`

- एक पैकेज को उसके वर्तमान संस्करण पर पिन करें:

`choco pin add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>

- एक पैकेज को एक विशिष्ट संस्करण पर पिन करें:

`choco pin add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">संस्करण</span>

- एक विशिष्ट पैकेज के लिए एक पिन हटा दें:

`choco pin remove --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>
