---
layout: page
title: sunos/svcadm (हिन्दी)
description: "सेवा उदाहरणों को प्रबंधित करें।"
content_hash: 601b61c9fd2f4751625dbc4259d6ba5be2e2bcc2
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/sunos/svcadm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/svcadm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/sunos/svcadm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/sunos/svcadm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/svcadm.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/sunos/svcadm.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/svcadm.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/svcadm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/sunos/svcadm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># svcadm

सेवा उदाहरणों को प्रबंधित करें।
अधिक जानकारी: <https://www.unix.com/man-page/linux/1m/svcadm>।

- सेवा डेटाबेस में एक सेवा को सक्षम करें:

`svcadm enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">सेवा नाम</span>

- सेवा को निष्क्रिय करें:

`svcadm disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">सेवा नाम</span>

- चल रही सेवा को पुनः प्रारंभ करें:

`svcadm restart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">सेवा नाम</span>

- सेवा को कॉन्फ़िगरेशन फ़ाइलों को फिर से पढ़ने के लिए आदेश दें:

`svcadm refresh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">सेवा नाम</span>

- एक सेवा को रखरखाव स्थिति से हटा दें और इसे प्रारंभ करने का आदेश दें:

`svcadm clear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">सेवा नाम</span>
