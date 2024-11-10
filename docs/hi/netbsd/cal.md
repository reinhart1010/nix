---
layout: page
title: netbsd/cal (हिन्दी)
description: "एक कैलेंडर प्रदर्शित करें।"
content_hash: 3f4a381d0e5f5f2531e58b9d4fc173b0ba3cdb4e
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/netbsd/cal.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/netbsd/cal.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/netbsd/cal.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cal

एक कैलेंडर प्रदर्शित करें।
अधिक जानकारी: <https://man.netbsd.org/cal.1>।

- वर्तमान महीने के लिए एक कैलेंडर प्रदर्शित करें:

`cal`

- एक विशेष वर्ष के लिए एक कैलेंडर प्रदर्शित करें:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">वर्ष</span>

- एक विशेष महीने और वर्ष के लिए एक कैलेंडर प्रदर्शित करें:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">महीना</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">वर्ष</span>

- वर्तमान वर्ष के लिए संपूर्ण कैलेंडर प्रदर्शित करें [j]जूलियन दिन का उपयोग करते हुए (एक-आधारित, 1 जनवरी से क्रमांकित):

`cal -y -j`

- [h]आज को हाइलाइट करें और [3] महीनों को प्रदर्शित करें जो तारीख को कवर करते हैं:

`cal -h -3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">महीना</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">वर्ष</span>

- वर्तमान वर्ष के एक विशेष [m]महीने से [B]2 महीने पहले और [A]3 महीने बाद प्रदर्शित करें:

`cal -A 3 -B 2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">महीना</span>

- निर्दिष्ट महीने से पहले और बाद में एक विशिष्ट संख्या के महीनों को प्रदर्शित करें ([C]संदर्भ):

`cal -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">महीने</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">महीना</span>

- सप्ताह के प्रारंभिक [d]दिन को निर्धारित करें (0: रविवार, 1: सोमवार, ..., 6: शनिवार):

`cal -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0..6</span>
