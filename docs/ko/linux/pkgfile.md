---
layout: page
title: linux/pkgfile (한국어)
description: "Arch 기반 시스템의 공식 저장소에서 패키지의 파일을 검색합니다."
content_hash: 90eb9098864f4e1ff606e948811fd49d287da8d5
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/pkgfile.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pkgfile.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pkgfile

Arch 기반 시스템의 공식 저장소에서 패키지의 파일을 검색합니다.
같이 보기: `pacman files`, `pacman --files`의 사용법 설명.
더 많은 정보: <https://manned.org/pkgfile>.

- pkgfile 데이터베이스 동기화:

`sudo pkgfile --update`

- 특정 파일을 소유한 패키지 검색:

`pkgfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>

- 패키지가 제공하는 모든 파일 나열:

`pkgfile --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지가 제공하는 실행 파일 나열:

`pkgfile --list --binaries `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 대소문자를 구분하지 않고 특정 파일을 소유한 패키지 검색:

`pkgfile --ignorecase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>

- `bin` 또는 `sbin` 디렉토리에서 특정 파일을 소유한 패키지 검색:

`pkgfile --binaries `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>

- 특정 파일을 소유한 패키지를 패키지 버전과 함께 검색:

`pkgfile --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>

- 특정 저장소에서 특정 파일을 소유한 패키지 검색:

`pkgfile --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>
