---
layout: page
title: netbsd/chpass (한국어)
description: "사용자 데이터베이스 정보, 로그인 셸 및 비밀번호를 추가하거나 변경합니다."
content_hash: f99248f4194894bb64ddc1d5be803ea0d85243e0
last_modified_at: 2024-06-24
related_topics:
  - title: English version
    url: /en/netbsd/chpass.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/netbsd/chpass.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chpass

사용자 데이터베이스 정보, 로그인 셸 및 비밀번호를 추가하거나 변경합니다.
같이 보기: `passwd`.
더 많은 정보: <https://man.openbsd.org/chsh>.

- 현재 사용자에게 특정 로그인 셸을 대화식으로 설정:

`su -c chpass`

- 현재 사용자에게 특정 로그인 셸 설정:

`chpass -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/셸</span>

- 특정 사용자에게 로그인 셸 설정:

`chpass chsh -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/셸</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- `passwd` 파일 형식으로 사용자 데이터베이스 항목 지정:

`su -c 'chpass -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명:암호화된_비밀번호:uid:gid:...</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 로컬 비밀번호 파일만 업데이트:

`su -c 'chpass -l -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/셸</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 데이터베이스 [y]P 비밀번호 데이터베이스 항목을 강제로 변경:

`su -c 'chpass -y -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/셸</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>
