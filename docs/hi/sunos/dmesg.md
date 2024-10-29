---
layout: page
title: sunos/dmesg (हिन्दी)
description: "कर्नेल संदेशों को `stdout` पर लिखें।"
content_hash: 198eae9a3298c06aecf9e563b7ac07af9f0619a6
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/sunos/dmesg.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/dmesg.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/sunos/dmesg.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/sunos/dmesg.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/dmesg.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/sunos/dmesg.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/dmesg.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/dmesg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/sunos/dmesg.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/sunos/dmesg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dmesg

कर्नेल संदेशों को `stdout` पर लिखें।
अधिक जानकारी: <https://www.unix.com/man-page/sunos/1m/dmesg>।

- कर्नेल संदेश दिखाएं:

`dmesg`

- इस सिस्टम पर कितनी भौतिक मेमोरी उपलब्ध है दिखाएं:

`dmesg | grep -i memory`

- कर्नेल संदेश 1 पृष्ठ में एक बार दिखाएं:

`dmesg | less`
