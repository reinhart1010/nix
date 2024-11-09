---
layout: page
title: linux/pkginfo (한국어)
description: "CRUX 시스템에서 패키지 데이터베이스를 조회."
content_hash: d4ed39243c6e28481538499b25bfcc06d1076f02
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/pkginfo.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pkginfo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pkginfo

CRUX 시스템에서 패키지 데이터베이스를 조회.
더 많은 정보: <https://crux.nu/Main/Handbook3-6#ntoc19>.

- 설치된 패키지 및 버전 나열:

`pkginfo -i`

- 패키지가 소유한 파일 나열:

`pkginfo -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패턴과 일치하는 파일의 소유자(들) 나열:

`pkginfo -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>

- 파일의 풋프린트 출력:

`pkginfo -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
