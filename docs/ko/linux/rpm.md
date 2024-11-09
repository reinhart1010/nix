---
layout: page
title: linux/rpm (한국어)
description: "RPM 패키지 관리 도구."
content_hash: a1a566ad6841d244abb81d19c5249b0bd6c0b0f8
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/rpm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/rpm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rpm

RPM 패키지 관리 도구.
다른 패키지 관리자의 동등한 명령을 보려면 <https://wiki.archlinux.org/title/Pacman/Rosetta>.
더 많은 정보: <https://rpm.org/>.

- httpd 패키지의 버전 표시:

`rpm --query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpd</span>

- 모든 일치하는 패키지의 버전 나열:

`rpm --query --all '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mariadb*</span>`'`

- 현재 설치된 버전에 상관없이 강제로 패키지 설치:

`rpm --upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/패키지.rpm</span>` --force`

- 파일의 소유자를 식별하고 패키지 버전 표시:

`rpm --query --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/postfix/main.cf</span>

- 패키지가 소유한 파일 나열:

`rpm --query --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kernel</span>

- RPM 파일의 스크립트릿 표시:

`rpm --query --package --scripts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지.rpm</span>

- 일치하는 패키지의 변경되었거나 누락되었거나 잘못 설치된 파일 표시:

`rpm --verify --all '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">php-*</span>`'`

- 특정 패키지의 변경 로그 표시:

`rpm --query --changelog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>
