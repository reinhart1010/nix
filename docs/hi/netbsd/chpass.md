---
layout: page
title: netbsd/chpass (हिन्दी)
description: "उपयोगकर्ता डेटाबेस जानकारी जोड़ें या बदलें, जिसमें लॉगिन शेल और पासवर्ड शामिल हैं।"
content_hash: aeb72f2aadfe1127aeae45bab671371d1e6531b0
last_modified_at: 2024-11-18
related_topics:
  - title: English version
    url: /en/netbsd/chpass.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/netbsd/chpass.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/netbsd/chpass.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chpass

उपयोगकर्ता डेटाबेस जानकारी जोड़ें या बदलें, जिसमें लॉगिन शेल और पासवर्ड शामिल हैं।
और देखें: `passwd`।
अधिक जानकारी: <https://man.netbsd.org/chsh>।

- वर्तमान उपयोगकर्ता के लिए इंटरैक्टिव रूप से एक विशिष्ट लॉगिन शेल सेट करें:

`su -c chpass`

- वर्तमान उपयोगकर्ता के लिए एक विशिष्ट लॉगिन [s]शेल सेट करें:

`chpass -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">शेल/का/पथ</span>

- एक विशिष्ट उपयोगकर्ता के लिए एक लॉगिन [s]शेल सेट करें:

`chpass chsh -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">शेल/का/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता_नाम</span>

- `passwd` फ़ाइल प्रारूप में एक उपयोगकर्ता डेटाबेस प्रविष्टि निर्दिष्ट करें:

`su -c 'chpass -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता_नाम:encrypted_password:uid:gid:...</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता_नाम</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता_नाम</span>

- केवल [l]स्थानीय पासवर्ड फ़ाइल को अपडेट करें:

`su -c 'chpass -l -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">शेल/का/पथ</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता_नाम</span>

- मजबूरन डेटाबेस [y]P पासवर्ड डेटाबेस प्रविष्टि बदलें:

`su -c 'chpass -y -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">शेल/का/पथ</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता_नाम</span>
