---
layout: page
title: common/strings (हिन्दी)
description: "एक ऑब्जेक्ट फ़ाइल या बाइनरी में प्रिंट करने योग्य स्ट्रिंग्स खोजें।"
content_hash: 33b0170ff595499fe393785b46d4573b0fa239b4
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/strings.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/strings.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/strings.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/strings.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/strings.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># strings

एक ऑब्जेक्ट फ़ाइल या बाइनरी में प्रिंट करने योग्य स्ट्रिंग्स खोजें।
अधिक जानकारी: <https://manned.org/strings>।

- एक बाइनरी में सभी स्ट्रिंग्स प्रिंट करें:

`strings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल/का/पथ</span>

- परिणामों को कम से कम n अक्षरों लंबी स्ट्रिंग्स तक सीमित करें:

`strings -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल/का/पथ</span>

- प्रत्येक परिणाम को फ़ाइल के भीतर इसके ऑफ़सेट के साथ पूर्ववत करें:

`strings -t d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल/का/पथ</span>

- प्रत्येक परिणाम को फ़ाइल के भीतर इसके ऑफ़सेट के साथ हेक्साडेसिमल में पूर्ववत करें:

`strings -t x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल/का/पथ</span>
