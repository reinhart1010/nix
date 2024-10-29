---
layout: page
title: sunos/prstat (हिन्दी)
description: "सक्रिय प्रक्रिया सांख्यिकी की रिपोर्ट करें।"
content_hash: 83b24a84beacbdcaa2be93ecff4c3ffc8adbd536
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/sunos/prstat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/prstat.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/sunos/prstat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/sunos/prstat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/prstat.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/sunos/prstat.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/prstat.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/prstat.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/sunos/prstat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># prstat

सक्रिय प्रक्रिया सांख्यिकी की रिपोर्ट करें।
अधिक जानकारी: <https://www.unix.com/man-page/sunos/1m/prstat>।

- सभी प्रक्रियाओं की जांच करें और सीपीयू उपयोग के अनुसार सांख्यिकी की रिपोर्ट करें:

`prstat`

- सभी प्रक्रियाओं की जांच करें और मेमोरी उपयोग के अनुसार सांख्यिकी की रिपोर्ट करें:

`prstat -s rss`

- प्रत्येक उपयोगकर्ता के लिए कुल उपयोग सारांश की रिपोर्ट करें:

`prstat -t`

- माइक्रोस्टेट प्रक्रिया लेखांकन जानकारी की रिपोर्ट करें:

`prstat -m`

- हर सेकंड शीर्ष 5 सीपीयू उपयोग करने वाली प्रक्रियाओं की सूची प्रिंट करें:

`prstat -c -n 5 -s cpu 1`
