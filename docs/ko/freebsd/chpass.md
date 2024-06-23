---
layout: page
title: freebsd/chpass (한국어)
description: "사용자 데이터베이스 정보, 로그인 쉘 및 비밀번호를 추가하거나 변경합니다."
content_hash: 1d7842ce9fa9505d766eb66a70844c06dd634428
last_modified_at: 2024-06-23
related_topics:
  - title: English version
    url: /en/freebsd/chpass.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/freebsd/chpass.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/freebsd/chpass.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># chpass

사용자 데이터베이스 정보, 로그인 쉘 및 비밀번호를 추가하거나 변경합니다.
같이 보기: `passwd`.
더 많은 정보: <https://man.freebsd.org/cgi/man.cgi?chpass>.

- 현재 사용자의 사용자 데이터베이스 정보를 대화식으로 추가하거나 변경:

`su -c chpass`

- 현재 사용자의 로그인 쉘 설정:

`chpass -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/쉘</span>

- 특정 사용자의 로그인 쉘 설정:

`chpass -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/쉘</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 계정 만료 시간 변경 (에포크로부터 초 단위, UTC):

`su -c 'chpass -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시간</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>`'`

- 사용자 비밀번호 변경:

`su -c 'chpass -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">암호화된_비밀번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>`'`

- 조회할 NIS 서버의 호스트명 또는 주소 지정:

`su -c 'chpass -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>`'`

- 특정 NIS 도메인 지정 (기본값은 시스템 도메인 이름):

`su -c 'chpass -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>`'`
