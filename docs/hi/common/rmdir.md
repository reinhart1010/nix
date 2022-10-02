---
layout: page
title: common/rmdir (हिन्दी)
description: "निर्देशिका को हटाता है।"
content_hash: 205b48dc558a3105a6580e6c998b9d41239f711f
related_topics:
  - title: English version
    url: /en/common/rmdir.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/rmdir.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/rmdir.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/rmdir.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rmdir

निर्देशिका को हटाता है।
अधिक जानकारी: <https://www.gnu.org/software/coreutils/rmdir>।

- निर्देशिका निकालें, बशर्ते वह खाली हो। गैर-रिक्त निर्देशिकाओं को हटाने के लिए `rm -r` का उपयोग करें:

`rmdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">निर्देशिका / का / पथ</span>

- लक्ष्य और उसकी मूल निर्देशिका निकालें (नेस्टेड निर्देशिकाओं के लिए उपयोगी):

`rmdir -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">निर्देशिका / का / पथ</span>
