---
layout: page
title: common/neofetch (हिन्दी)
description: "आपके ऑपरेटिंग सिस्टम, सॉफ्टवेयर और हार्डवेयर के बारे में जानकारी प्रदर्शित करने के लिए CLI टूल।"
content_hash: 2e53c50af57e18a9c281862d9c4219acd458d3e9
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/neofetch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/neofetch.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/neofetch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# neofetch

आपके ऑपरेटिंग सिस्टम, सॉफ्टवेयर और हार्डवेयर के बारे में जानकारी प्रदर्शित करने के लिए CLI टूल।
अधिक जानकारी: <https://github.com/dylanaraps/neofetch>।

- डिफ़ॉल्ट कॉन्फ़िगरेशन लौटाएं, और इसे बनाएं यदि यह पहली बार प्रोग्राम चलता है:

`neofetch`

- आउटपुट में दिखाई देने से एक जानकारी लाइन को ट्रिगर करें, जहां 'infoname' कॉन्फ़िगरेशन फ़ाइल में फ़ंक्शन नाम है, उदा। स्मृति:

`neofetch --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enable|disable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">infoname</span>

- OS आर्किटेक्चर छुपाएं/दिखाएं:

`neofetch --os_arch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- आउटपुट में CPU ब्रांड को सक्षम/अक्षम करें:

`neofetch --cpu_brand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>
