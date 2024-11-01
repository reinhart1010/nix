---
layout: page
title: openbsd/chpass (हिन्दी)
description: "उपयोगकर्ता डेटाबेस जानकारी जोड़ें या बदलें, जिसमें लॉगिन शेल और पासवर्ड शामिल हैं।"
content_hash: c387c0733fcb59391fdf4ace971c0bde6cf96bd2
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/openbsd/chpass.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/openbsd/chpass.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/openbsd/chpass.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/openbsd/chpass.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chpass

उपयोगकर्ता डेटाबेस जानकारी जोड़ें या बदलें, जिसमें लॉगिन शेल और पासवर्ड शामिल हैं।
देखें: `passwd`।
अधिक जानकारी: <https://man.openbsd.org/chsh>।

- वर्तमान उपयोगकर्ता के लिए इंटरैक्टिव रूप से एक विशिष्ट लॉगिन शेल सेट करें:

`doas chsh`

- वर्तमान उपयोगकर्ता के लिए एक विशिष्ट लॉगिन [s]hell सेट करें:

`doas chsh -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पथ/से/शेल</span>

- एक विशिष्ट उपयोगकर्ता के लिए लॉगिन [s]hell सेट करें:

`doas chsh -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पथ/से/शेल</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता नाम</span>

- `passwd` फ़ाइल प्रारूप में एक उपयोगकर्ता डेटाबेस प्रविष्टि निर्दिष्ट करें:

`doas chsh -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता नाम:एनक्रिप्टेड_पासवर्ड:uid:gid:...</span>
