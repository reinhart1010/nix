---
layout: page
title: linux/free (हिन्दी)
description: "सिस्टम में 'Free' और यूज्ड मेमोरी की मात्रा दिखाता है।"
content_hash: 51807d2f629eda5f8644123ebd323eb12b2d7d72
related_topics:
  - title: català version
    url: /ca/linux/free.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/free.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/free.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/free.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># free

सिस्टम में 'Free' और यूज्ड मेमोरी की मात्रा दिखाता है।
अधिक जानकारी: <https://manned.org/free>.

- सिस्टम मेमोरी दिखाएं:

`free`

- सिस्टम मेमोरी को बाइट्स/केबी/एमबी/जीबी में दिखाएं:

`free -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">b|k|m|g</span>

- मानव-पठनीय इकाइयों में सिस्टम मेमोरी प्रदर्शित करें:

`free -h`

- हर 2 सेकंड में आउटपुट अपडेट करें:

`free -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>
