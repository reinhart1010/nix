---
layout: page
title: common/mv (हिन्दी)
description: "फ़ाइलों और निर्देशिकाओं को स्थानांतरित या नाम बदलें।"
content_hash: b0cd9e6d4cfe6c8cfde3c16ac4123cd0a87f2a97
last_modified_at: 2025-03-02
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
  - title: 한국어 version
    url: /ko/common/mv.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/mv.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/mv.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/mv.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/mv.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/mv.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mv

फ़ाइलों और निर्देशिकाओं को स्थानांतरित या नाम बदलें।
अधिक जानकारी: <https://www.gnu.org/software/coreutils/manual/html_node/mv-invocation.html>।

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
