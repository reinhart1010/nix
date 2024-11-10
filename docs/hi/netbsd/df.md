---
layout: page
title: netbsd/df (हिन्दी)
description: "फ़ाइल सिस्टम डिस्क स्पेस उपयोग का अवलोकन दिखाएँ।"
content_hash: e6018b5145ccaaf775c76a2af712f6e5fa0108e3
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/netbsd/df.html
    icon: bi bi-globe
  - title: español version
    url: /es/netbsd/df.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/netbsd/df.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/netbsd/df.html
    icon: bi bi-globe
tldri18n_status: 2
---
# df

फ़ाइल सिस्टम डिस्क स्पेस उपयोग का अवलोकन दिखाएँ।
अधिक जानकारी: <https://man.netbsd.org/df.1>।

- 512-बाइट इकाइयों का उपयोग करके सभी फ़ाइल सिस्टम और उनके डिस्क उपयोग को दिखाएँ:

`df`

- [h]मानव-पठनीय इकाइयों का उपयोग करें (1024 की शक्तियों के आधार पर):

`df -h`

- `statvfs` द्वारा लौटाए गए संरचना(ओं) के सभी फ़ील्ड दिखाएँ:

`df -G`

- दिए गए फ़ाइल या निर्देशिका को शामिल करते हुए फ़ाइल सिस्टम और उसके डिस्क उपयोग को दिखाएँ:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल_या_निर्देशिका का पथ</span>

- मुक्त और उपयोग किए गए [I]इनोड की संख्या पर सांख्यिकी शामिल करें:

`df -i`

- स्पेस आंकड़े लिखते समय 1024-बाइट इकाइयों का उपयोग करें:

`df -k`

- जानकारी को [P]पोर्टेबल तरीके से दिखाएँ:

`df -P`
