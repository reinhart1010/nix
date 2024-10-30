---
layout: page
title: sunos/svccfg (हिन्दी)
description: "सेवा कॉन्फ़िगरेशन को आयात, निर्यात और संशोधित करें।"
content_hash: 55955ab29dee4017f4f34274d1cd8cf6b4af63a4
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/sunos/svccfg.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/sunos/svccfg.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/sunos/svccfg.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/svccfg.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/sunos/svccfg.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/svccfg.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/svccfg.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/sunos/svccfg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># svccfg

सेवा कॉन्फ़िगरेशन को आयात, निर्यात और संशोधित करें।
अधिक जानकारी: <https://www.unix.com/man-page/linux/1m/svccfg>।

- कॉन्फ़िगरेशन फ़ाइल मान्य करें:

`svccfg validate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पथ/से/फाइल.xml</span>

- सेवा कॉन्फ़िगरेशन को फ़ाइल में निर्यात करें:

`svccfg export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">सेवामान</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पथ/से/फाइल.xml</span>

- फ़ाइल से सेवा कॉन्फ़िगरेशन को आयात/अपडेट करें:

`svccfg import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पथ/से/फाइल.xml</span>
