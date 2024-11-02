---
layout: page
title: openbsd/pkg_info (हिन्दी)
description: "OpenBSD में पैकेजों के बारे में जानकारी देखें।"
content_hash: 881241c26dbfe5734ca06e2369d7fafd50a1c5fd
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/openbsd/pkg_info.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/openbsd/pkg_info.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/openbsd/pkg_info.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/openbsd/pkg_info.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/openbsd/pkg_info.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/openbsd/pkg_info.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pkg_info

OpenBSD में पैकेजों के बारे में जानकारी देखें।
देखें: `pkg_add`, `pkg_delete`।
अधिक जानकारी: <https://man.openbsd.org/pkg_info>।

- पैकेज नाम का उपयोग करके पैकेज के लिए खोजें:

`pkg_info -Q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>

- `pkg_add -l` के साथ उपयोग के लिए स्थापित पैकेजों की सूची आउटपुट करें:

`pkg_info -mz`
