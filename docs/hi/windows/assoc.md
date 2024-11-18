---
layout: page
title: windows/assoc (हिन्दी)
description: "फ़ाइल एक्सटेंशन और फ़ाइल प्रकारों के बीच संबंधों को प्रदर्शित या बदलें।"
content_hash: b06b76f2f47e8b22aec8ec183949fb3740f1fbfe
last_modified_at: 2024-11-18
related_topics:
  - title: English version
    url: /en/windows/assoc.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/assoc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/assoc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/assoc.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/assoc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/assoc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/assoc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># assoc

फ़ाइल एक्सटेंशन और फ़ाइल प्रकारों के बीच संबंधों को प्रदर्शित या बदलें।
अधिक जानकारी: <https://learn.microsoft.com/windows-server/administration/windows-commands/assoc>।

- फ़ाइल एक्सटेंशनों और फ़ाइल प्रकारों के बीच सभी संबंधों की सूची बनाएं:

`assoc`

- एक विशिष्ट एक्सटेंशन के लिए संबंधित फ़ाइल प्रकार प्रदर्शित करें:

`assoc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.txt</span>

- एक विशिष्ट एक्सटेंशन के लिए संबंधित फ़ाइल प्रकार सेट करें:

`assoc .`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">txt</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">txt फ़ाइल</span>

- `assoc` का आउटपुट एक स्क्रीन में एक बार में देखें:

`assoc | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">more</span>
