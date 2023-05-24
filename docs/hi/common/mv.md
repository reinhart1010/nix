---
layout: page
title: common/mv (हिन्दी)
description: "फ़ाइलों और निर्देशिकाओं को स्थानांतरित या नाम बदलें।"
content_hash: ebdc4af051b63f0b55d18760f827c25db14c9222
last_modified_at: 2023-05-24
related_topics:
  - title: Deutsch version
    url: /de/common/mv.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/mv.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/mv.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/mv.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/mv.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/mv.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/mv.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mv.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mv

फ़ाइलों और निर्देशिकाओं को स्थानांतरित या नाम बदलें।
अधिक जानकारी: <https://www.gnu.org/software/coreutils/mv>।

- किसी फ़ाइल को मनमाना स्थान पर ले जाएँ:

`mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्रोत/का/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लक्ष्य/का/पथ</span>

- फ़ाइल नाम रखते हुए फ़ाइलों को दूसरी निर्देशिका में ले जाएँ:

`mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्रोत1/का/पथ स्रोत2/का/पथ ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लक्ष्य_निर्देशिका/का/पथ</span>

- मौजूदा फाइलों को अधिलेखित करने से पहले पुष्टि के लिए संकेत न दें:

`mv -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्रोत/का/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लक्ष्य/का/पथ</span>

- फ़ाइल अनुमतियों की परवाह किए बिना, मौजूदा फ़ाइलों को अधिलेखित करने से पहले पुष्टि के लिए संकेत दें:

`mv -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्रोत/का/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लक्ष्य/का/पथ</span>

- लक्ष्य पर मौजूदा फाइलों को अधिलेखित न करें:

`mv -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्रोत/का/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लक्ष्य/का/पथ</span>

- फ़ाइलों को वर्बोज़ मोड में ले जाएँ, फ़ाइलों को स्थानांतरित करने के बाद दिखाएँ:

`mv -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्रोत/का/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लक्ष्य/का/पथ</span>
