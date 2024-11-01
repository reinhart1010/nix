---
layout: page
title: openbsd/df (हिन्दी)
description: "फ़ाइल सिस्टम डिस्क स्पेस उपयोग का एक अवलोकन प्रदर्शित करें।"
content_hash: 4787a8c4399d7c6f37c6886f447b9f88b90e523f
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/openbsd/df.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/openbsd/df.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/openbsd/df.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/openbsd/df.html
    icon: bi bi-globe
tldri18n_status: 2
---
# df

फ़ाइल सिस्टम डिस्क स्पेस उपयोग का एक अवलोकन प्रदर्शित करें।
अधिक जानकारी: <https://man.openbsd.org/df.1>।

- सभी फ़ाइल सिस्टम और उनके डिस्क उपयोग को 512-बाइट इकाइयों का उपयोग करके प्रदर्शित करें:

`df`

- सभी फ़ाइल सिस्टम और उनके डिस्क उपयोग को [h]मानव-पठनीय रूप में प्रदर्शित करें (1024 के गुणांक के आधार पर):

`df -h`

- दिए गए फ़ाइल या निर्देशिका को शामिल करते हुए फ़ाइल सिस्टम और इसके डिस्क उपयोग को प्रदर्शित करें:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल या निर्देशिका का पथ</span>

- मुक्त और उपयोग किए गए [i]नोड्स की संख्या पर सांख्यिकी शामिल करें:

`df -i`

- स्थान आंकड़ों को लिखते समय 1024-बाइट इकाइयों का उपयोग करें:

`df -k`

- जानकारी को [P]पोर्टेबल तरीके से प्रदर्शित करें:

`df -P`
