---
layout: page
title: linux/dpkg-query (한국어)
description: "설치된 패키지에 대한 정보 표시."
content_hash: a9993aa01f1ce7f85eb800a1ad008f84b5c20082
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/dpkg-query.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/dpkg-query.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dpkg-query.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dpkg-query.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dpkg-query

설치된 패키지에 대한 정보 표시.
더 많은 정보: <https://manned.org/dpkg-query.1>.

- 설치된 모든 패키지 나열:

`dpkg-query --list`

- 패턴과 일치하는 설치된 패키지 나열:

`dpkg-query --list '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">libc6*</span>`'`

- 패키지에 의해 설치된 모든 파일 나열:

`dpkg-query --listfiles `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">libc6</span>

- 패키지에 대한 정보 표시:

`dpkg-query --status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">libc6</span>

- 패턴과 일치하는 파일을 소유한 패키지 검색:

`dpkg-query --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/ld.so.conf.d</span>
