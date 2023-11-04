---
layout: page
title: common/aireplay-ng (हिन्दी)
description: "वायरलेस नेटवर्क में पैकेट इंजेक्ट करें।"
content_hash: 2463313b516b041eb73a1e28f076e9f8f1d13b2f
last_modified_at: 2023-11-04
related_topics:
  - title: বাংলা version
    url: /bn/common/aireplay-ng.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/aireplay-ng.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aireplay-ng.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aireplay-ng.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/aireplay-ng.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/aireplay-ng.html
    icon: bi bi-globe
---
# aireplay-ng

वायरलेस नेटवर्क में पैकेट इंजेक्ट करें।
`aireplay-ng` का हिस्सा।
अधिक जानकारी: <https://www.aircrack-ng.org/doku.php?id=aireplay-ng>.

- एक्सेस प्वाइंट के MAC पते, क्लाइंट के MAC पते और एक इंटरफ़ेस को देखते हुए एक विशिष्ट संख्या में असंबद्ध पैकेट भेजें:

` sudo aireplay-ng --deauth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>` --bssid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ap_mac</span>` --dmac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">client_mac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>` `
