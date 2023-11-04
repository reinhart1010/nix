---
layout: page
title: common/ac (हिन्दी)
description: "उपयोगकर्ता कितने समय से जुड़े हुए हैं, इसके आँकड़े प्रिंट करें।"
content_hash: 9174dff993bc6046ff3018f8792053667294556f
last_modified_at: 2023-11-04
related_topics:
  - title: বাংলা version
    url: /bn/common/ac.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ac.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ac.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ac.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ac.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ac.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ac.html
    icon: bi bi-globe
---
# ac

उपयोगकर्ता कितने समय से जुड़े हुए हैं, इसके आँकड़े प्रिंट करें।
अधिक जानकारी: <https://man.openbsd.org/ac>.

- प्रिंट करें कि वर्तमान उपयोगकर्ता कितने समय तक कनेक्ट रहा है, घंटों में:

`ac`

- उपयोगकर्ता कितनी देर तक जुड़े रहे, इसे घंटों में प्रिंट करें:

`ac -p`

- प्रिंट करें कि कोई विशेष उपयोगकर्ता कितने समय से घंटों में जुड़ा हुआ है:

`ac -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता_नाम</span>

- प्रिंट करें कि कोई विशेष उपयोगकर्ता प्रति दिन घंटों में कितने समय से जुड़ा हुआ है (कुल सहित):

`ac -dp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता_नाम</span>
