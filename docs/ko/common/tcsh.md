---
layout: page
title: common/tcsh (한국어)
description: "파일 이름 자동 완성과 명령 줄 편집 기능을 제공하는 C 셸."
content_hash: 6514137c5c698db5d1a361bd9c1a44c2d5f6a616
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/tcsh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tcsh

파일 이름 자동 완성과 명령 줄 편집 기능을 제공하는 C 셸.
같이 보기: `csh`.
더 많은 정보: <https://manned.org/tcsh>.

- 상호작용 셸 세션 시작:

`tcsh`

- 시작 구성 파일을 로드하지 않고 상호작용 셸 세션 시작:

`tcsh -f`

- 특정 [c]명령 실행:

`tcsh -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'tcsh is executed'</span>`"`

- 특정 스크립트 실행:

`tcsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.tcsh</span>

- 특정 스크립트의 구문 오류 검사:

`tcsh -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.tcsh</span>

- `stdin`에서 특정 명령 실행:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "echo 'tcsh is executed'"</span>` | tcsh`
