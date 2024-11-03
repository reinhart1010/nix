---
layout: page
title: common/ksh (한국어)
description: "Korn Shell, Bash와 호환되는 명령줄 인터프리터."
content_hash: a9bf41c8f5b174894b3135a868ce9996e9959f9b
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/ksh.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ksh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ksh

Korn Shell, Bash와 호환되는 명령줄 인터프리터.
같이 보기: `histexpand`.
더 많은 정보: <http://kornshell.com>.

- 대화형 셸 세션 시작:

`ksh`

- 특정 [c]명령어 실행:

`ksh -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'ksh is executed'</span>`"`

- 특정 스크립트 실행:

`ksh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.ksh</span>

- 특정 스크립트를 실행하지 않고 구문 오류 검사:

`ksh -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.ksh</span>

- 특정 스크립트를 실행하면서 각 명령을 실행 전 출력:

`ksh -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.ksh</span>
