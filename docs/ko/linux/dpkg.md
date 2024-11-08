---
layout: page
title: linux/dpkg (한국어)
description: "Debian 패키지 관리자."
content_hash: 3d75c2b31ea2b412570e3de12839ee48c19c89e7
last_modified_at: 2024-11-08
related_topics:
  - title: Deutsch version
    url: /de/linux/dpkg.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dpkg.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/dpkg.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/dpkg.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/dpkg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dpkg.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dpkg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dpkg

Debian 패키지 관리자.
`deb`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
다른 패키지 관리자의 동등한 명령을 보려면 <https://wiki.archlinux.org/title/Pacman/Rosetta>.
더 많은 정보: <https://manned.org/dpkg>.

- 패키지 설치:

`dpkg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.deb</span>

- 패키지 제거:

`dpkg -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 설치된 패키지 나열:

`dpkg -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>

- 패키지의 내용 나열:

`dpkg -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 로컬 패키지 파일의 내용 나열:

`dpkg -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.deb</span>

- 특정 파일이 어떤 패키지에 속해 있는지 확인:

`dpkg -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 설치되었거나 이미 제거된 패키지 및 구성 파일 삭제:

`dpkg -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>
