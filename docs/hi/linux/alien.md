---
layout: page
title: linux/alien (हिन्दी)
description: "विभिन्न इंस्टॉलेशन पैकेज को अन्य प्रारूपों में कनवर्ट करें।"
content_hash: d75d4c0e46f5294728e9420d4ec08f2d1f0257e4
last_modified_at: 2024-02-16
related_topics:
  - title: Deutsch version
    url: /de/linux/alien.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/alien.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/alien.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/alien.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/alien.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/alien.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/alien.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># alien

विभिन्न इंस्टॉलेशन पैकेज को अन्य प्रारूपों में कनवर्ट करें।
यह भी देखें: Arch Linux पर `.deb` रूपांतरण के लिए `debtap`।
अधिक जानकारी: <https://manned.org/alien>.

- किसी खास इंस्टॉलेशन फ़ाइल को Debian फ़ॉर्मैट (`.deb` एक्सटेंशन) में बदलें:

`sudo alien --to-deb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल/का/पथ</span>

- विशिष्ट अधिष्ठापन फाइल को Red Hat फॉर्मेट (`.rpm` एक्सटेंशन) में बदलें:

`sudo alien --to-rpm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल/का/पथ</span>

- एक विशिष्ट इंस्टॉलेशन फ़ाइल को Slackware इंस्टॉलेशन फ़ाइल (`.tgz` एक्सटेंशन) में कनवर्ट करें:

`sudo alien --to-tgz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल/का/पथ</span>

- एक विशिष्ट इंस्टॉलेशन फ़ाइल को Debian प्रारूप में बदलें और सिस्टम पर इंस्टॉल करें:

`sudo alien --to-deb --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल/का/पथ</span>
