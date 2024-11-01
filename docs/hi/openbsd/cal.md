---
layout: page
title: openbsd/cal (हिन्दी)
description: "वर्तमान दिन को हाइलाइट करते हुए कैलेंडर दिखाएं।"
content_hash: 1ce7d6f970c92a2b4812c927af786b45909f55cb
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/openbsd/cal.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/openbsd/cal.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/openbsd/cal.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/openbsd/cal.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cal

वर्तमान दिन को हाइलाइट करते हुए कैलेंडर दिखाएं।
अधिक जानकारी: <https://man.openbsd.org/cal>।

- वर्तमान महीने के लिए कैलेंडर दिखाएं:

`cal`

- किसी विशेष वर्ष के लिए कैलेंडर दिखाएं:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">वर्ष</span>

- किसी विशेष महीने और वर्ष के लिए कैलेंडर दिखाएं:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">महिना</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">वर्ष</span>

- वर्तमान [व]र्ष के लिए कैलेंडर दिखाएं:

`cal -y`

- [ज]ूलियन दिनों को दिखाएं (एक से शुरू होकर, 1 जनवरी से संख्या दी गई):

`cal -j`

- रविवार के बजाय [सो]मवार को सप्ताह की शुरुआत के रूप में उपयोग करें:

`cal -m`

- सप्ताह के नंबरों को संख्या दें (जो `-j` के साथ असंगत है):

`cal -w`
