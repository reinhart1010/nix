---
layout: page
title: sunos/snoop (हिन्दी)
description: "नेटवर्क पैकेट स्निफर।"
content_hash: 84d8d296130808c839eff87d676c773d333522ab
last_modified_at: 2024-10-29
related_topics:
  - title: বাংলা version
    url: /bn/sunos/snoop.html
    icon: bi bi-globe
  - title: English version
    url: /en/sunos/snoop.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/snoop.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/sunos/snoop.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/sunos/snoop.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/snoop.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/sunos/snoop.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/snoop.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/snoop.html
    icon: bi bi-globe
tldri18n_status: 2
---
# snoop

नेटवर्क पैकेट स्निफर।
सनओएस का tcpdump समकक्ष।
अधिक जानकारी: <https://www.unix.com/man-page/sunos/1m/snoop>।

- एक विशेष नेटवर्क इंटरफेस पर पैकेट कैप्चर करें:

`snoop -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">e1000g0</span>

- कैप्चर किए गए पैकेट को प्रदर्शित करने के बजाय एक फ़ाइल में सहेजें:

`snoop -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल/का/पथ</span>

- एक फ़ाइल से पैकेट का विस्तृत प्रोटोकॉल स्तर सारांश प्रदर्शित करें:

`snoop -V -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल/का/पथ</span>

- एक होस्टनाम से आने वाले और एक दिए गए पोर्ट पर जाने वाले नेटवर्क पैकेट कैप्चर करें:

`snoop to port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पोर्ट</span>` from host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">होस्टनाम</span>

- दो आईपी पते के बीच विनिमय किए गए नेटवर्क पैकेट का हेक्स-डंप कैप्चर और दिखाएँ:

`snoop -x0 -p4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip2</span>
