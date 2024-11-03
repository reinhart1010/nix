---
layout: page
title: freebsd/look (हिन्दी)
description: "एक सॉर्ट की गई फ़ाइल में एक उपसर्ग से शुरू होने वाली पंक्तियों को प्रदर्शित करें।"
content_hash: ad08d8c70e91a0bac35b14d6bdf7cd9041940e30
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/freebsd/look.html
    icon: bi bi-globe
  - title: español version
    url: /es/freebsd/look.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/freebsd/look.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/freebsd/look.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/freebsd/look.html
    icon: bi bi-globe
tldri18n_status: 2
---
# look

एक सॉर्ट की गई फ़ाइल में एक उपसर्ग से शुरू होने वाली पंक्तियों को प्रदर्शित करें।
देखें: `grep`, `sort`।
अधिक जानकारी: <https://man.freebsd.org/cgi/man.cgi?look>।

- एक विशेष फ़ाइल में एक विशेष उपसर्ग से शुरू होने वाली पंक्तियों के लिए खोजें:

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पूर्वसूचक</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पथ/से/फाइल</span>

- केवल अल्फ़ान्यूमेरिक वर्णों पर केस-इंसेंसिटिव खोजें:

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--ignore-case</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--alphanum</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पूर्वसूचक</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पथ/से/फाइल</span>

- एक स्ट्रिंग टर्मिनेशन कैरेक्टर निर्दिष्ट करें (डिफ़ॉल्ट रूप से स्पेस):

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--terminate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>

- `/usr/share/dict/words` में खोजें (`--ignore-case` और `--alphanum` को मान लिया गया है):

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पूर्वसूचक</span>
