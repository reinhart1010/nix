---
layout: page
title: common/ant (हिन्दी)
description: "Apache Ant: जावा-आधारित प्रोजेक्ट बनाएं और प्रबंधित करें।"
content_hash: 40154c23033cd1259efaf1001400d8260e091aa1
last_modified_at: 2024-10-24
related_topics:
  - title: Deutsch version
    url: /de/common/ant.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ant.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ant.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ant.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ant.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ant.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ant.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ant

Apache Ant: जावा-आधारित प्रोजेक्ट बनाएं और प्रबंधित करें।
अधिक जानकारी: <https://ant.apache.org>।

- डिफ़ॉल्ट बिल्ड फ़ाइल के साथ एक प्रोजेक्ट बनाएं `build.xml`:

`ant`

- बिल्ड फ़ाइल के अलावा अन्य का उपयोग करके एक प्रोजेक्ट बनाएं `build.xml`:

`ant -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">buildfile.xml</span>

- इस परियोजना के लिए संभावित लक्ष्यों पर जानकारी प्रिंट करें:

`ant -p`

- डिबगिंग जानकारी प्रिंट करें:

`ant -d`

- उन सभी लक्ष्यों को निष्पादित करें जो विफल लक्ष्य पर निर्भर नहीं हैं:

`ant -k`
