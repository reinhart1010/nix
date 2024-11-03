---
layout: page
title: freebsd/df (हिन्दी)
description: "फाइल सिस्टम डिस्क स्पेस उपयोग का अवलोकन प्रदर्शित करें।"
content_hash: 36acf9eb3f656fdc0bc771f47f0c0e433ab6b87f
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/freebsd/df.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/freebsd/df.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/freebsd/df.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/freebsd/df.html
    icon: bi bi-globe
tldri18n_status: 2
---
# df

फाइल सिस्टम डिस्क स्पेस उपयोग का अवलोकन प्रदर्शित करें।
अधिक जानकारी: <https://man.freebsd.org/cgi/man.cgi?df>।

- सभी फाइल सिस्टम और उनके डिस्क उपयोग को 512-बाइट यूनिट्स में प्रदर्शित करें:

`df`

- [h]मानव-पठनीय यूनिट्स का उपयोग करें (1024 की शक्तियों पर आधारित) और कुल योग प्रदर्शित करें:

`df -h -c`

- [H]मानव-पठनीय यूनिट्स का उपयोग करें (1000 की शक्तियों पर आधारित):

`df -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-si|H</span>

- दिए गए फ़ाइल या डायरेक्टरी को शामिल करते हुए फाइल सिस्टम और उसके डिस्क उपयोग को प्रदर्शित करें:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल_या_निर्देशिका/का/पथ</span>

- फाइल सिस्टम [T]प्रकार सहित फ्री और उपयोग किए गए [i]नोड्स की संख्या पर सांख्यिकी शामिल करें:

`df -iT`

- स्पेस आंकड़े लिखते समय 1024-बाइट यूनिट्स का उपयोग करें:

`df -k`

- जानकारी को [P]पोर्टेबल तरीके से प्रदर्शित करें:

`df -P`
