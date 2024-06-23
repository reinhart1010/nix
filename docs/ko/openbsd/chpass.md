---
layout: page
title: openbsd/chpass (한국어)
description: "로그인 셸과 비밀번호를 포함한 사용자 데이터베이스 정보를 추가하거나 변경합니다."
content_hash: 64005f54f349978721b54c9910f8e8671991dee9
last_modified_at: 2024-06-23
related_topics:
  - title: English version
    url: /en/openbsd/chpass.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/openbsd/chpass.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/openbsd/chpass.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/openbsd/chpass.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># chpass

로그인 셸과 비밀번호를 포함한 사용자 데이터베이스 정보를 추가하거나 변경합니다.
같이 보기: `passwd`.
더 많은 정보: <https://man.openbsd.org/chsh>.

- 현재 사용자에게 특정 로그인 셸을 대화식으로 설정:

`doas chsh`

- 현재 사용자에게 특정 로그인 셸을 설정:

`doas chsh -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/셸</span>

- 특정 사용자에게 로그인 셸을 설정:

`doas chsh -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/셸</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- `passwd` 파일 형식의 사용자 데이터베이스 항목을 지정:

`doas chsh -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명:암호화된_비밀번호:uid:gid:...</span>
