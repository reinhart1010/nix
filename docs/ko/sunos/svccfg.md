---
layout: page
title: sunos/svccfg (한국어)
description: "서비스 구성을 가져오고, 내보내고, 수정합니다."
content_hash: c3504864af79bdb7dfc7e4fb1e0247c939dc6a04
last_modified_at: 2024-06-23
related_topics:
  - title: English version
    url: /en/sunos/svccfg.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/sunos/svccfg.html
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

서비스 구성을 가져오고, 내보내고, 수정합니다.
더 많은 정보: <https://www.unix.com/man-page/linux/1m/svccfg>.

- 구성 파일 유효성 검사:

`svccfg validate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/smf_파일.xml</span>

- 서비스 구성을 파일로 내보내기:

`svccfg export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스명</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/smf_파일.xml</span>

- 파일에서 서비스 구성 가져오거나 업데이트:

`svccfg import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/smf_파일.xml</span>
