---
layout: page
title: osx/chpass (한국어)
description: "사용자 데이터베이스 정보 추가 또는 변경, 로그인 쉘 및 비밀번호 포함."
content_hash: 37d3c30f4b096a58a3488699ea903500e7421215
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/chpass.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/chpass.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/chpass.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chpass

사용자 데이터베이스 정보 추가 또는 변경, 로그인 쉘 및 비밀번호 포함.
참고: Open Directory 시스템에서는 사용자의 비밀번호를 변경할 수 없으며, 대신 `passwd`를 사용하세요.
같이 보기: `passwd`.
더 많은 정보: <https://man.freebsd.org/cgi/man.cgi?chpass>.

- 현재 사용자에 대해 대화형으로 사용자 데이터베이스 정보 추가 또는 변경:

`su -c chpass`

- 현재 사용자에 대해 특정 로그인 [s]쉘 설정:

`chpass -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/쉘</span>

- 특정 사용자에 대해 로그인 [s]쉘 설정:

`chpass -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/쉘</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 지정된 [l]위치에 있는 디렉터리 노드에서 사용자 기록 편집:

`chpass -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">위치</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/쉘</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 사용자가 포함된 디렉터리 노드에 인증할 때 주어진 [u]사용자명 사용:

`chpass -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인증명</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/쉘</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>
