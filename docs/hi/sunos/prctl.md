---
layout: page
title: sunos/prctl (हिन्दी)
description: "चल रहे प्रक्रियाओं, कार्यों और परियोजनाओं के संसाधन नियंत्रण प्राप्त करें या सेट करें।"
content_hash: 290e97bd1378389c5b89474982021450f95b4d2e
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/sunos/prctl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/prctl.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/sunos/prctl.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/sunos/prctl.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/prctl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/sunos/prctl.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/prctl.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/prctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# prctl

चल रहे प्रक्रियाओं, कार्यों और परियोजनाओं के संसाधन नियंत्रण प्राप्त करें या सेट करें।
अधिक जानकारी: <https://www.unix.com/man-page/sunos/1/prctl>।

- प्रक्रिया सीमाओं और अनुमतियों की जांच करें:

`prctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- मशीन पार्सेबल प्रारूप में प्रक्रिया सीमाओं और अनुमतियों की जांच करें:

`prctl -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- चल रही प्रक्रिया के लिए विशिष्ट सीमा प्राप्त करें:

`prctl -n process.max-file-descriptor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>
