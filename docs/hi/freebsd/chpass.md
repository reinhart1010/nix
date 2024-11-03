---
layout: page
title: freebsd/chpass (हिन्दी)
description: "लॉगिन shell और पासवर्ड सहित उपयोगकर्ता डेटाबेस जानकारी जोड़ें या बदलें।"
content_hash: baa4b71b55b83f1cbc18dfefb5041d1f381dc81d
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/freebsd/chpass.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/freebsd/chpass.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/freebsd/chpass.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/freebsd/chpass.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chpass

लॉगिन shell और पासवर्ड सहित उपयोगकर्ता डेटाबेस जानकारी जोड़ें या बदलें।
यह भी देखें: `passwd`।
अधिक जानकारी: <https://man.freebsd.org/cgi/man.cgi?chpass>।

- वर्तमान उपयोगकर्ता के लिए उपयोगकर्ता डेटाबेस जानकारी को अंतःक्रियात्मक रूप से जोड़ें या बदलें:

`su -c chpass`

- वर्तमान उपयोगकर्ता के लिए एक विशिष्ट लॉगिन [s]hell सेट करें:

`chpass -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell/का/पथ</span>

- किसी विशिष्ट उपयोगकर्ता के लिए लॉगिन [s]hell सेट करें:

`chpass -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell/का/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोक्तानाम</span>

- खाता [e]समाप्ति समय बदलें (युग से सेकंड में, UTC):

`su -c 'chpass -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">समय</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोक्तानाम</span>`'`

- उपयोगकर्ता का पासवर्ड बदलें:

`su -c 'chpass -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">एन्क्रिप्टेड_पासवर्ड</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोक्तानाम</span>`'`

- क्वेरी करने के लिए NIS सर्वर का [h]होस्ट का नाम या पता निर्दिष्ट करें:

`su -c 'chpass -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">होस्ट का नाम</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोक्तानाम</span>`'`

- एक विशेष NIS डोमेन निर्दिष्ट करें (डिफ़ॉल्ट रूप से सिस्टम डोमेन नाम):

`su -c 'chpass -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">डोमेन</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोक्तानाम</span>`'`
