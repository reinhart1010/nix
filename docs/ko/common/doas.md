---
layout: page
title: common/doas (한국어)
description: "다른 사용자로 명령을 실행."
content_hash: b2d4f2e8748c1d7311f17c488441e0fb00e00e00
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/doas.html
    icon: bi bi-globe
tldri18n_status: 2
---
# doas

다른 사용자로 명령을 실행.
더 많은 정보: <https://man.openbsd.org/doas>.

- 루트 권한으로 명령을 실행:

`doas `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 다른 사용자 권한으로 명령을 실행:

`doas -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 루트 권한으로 기본 쉘을 시작:

`doas -s`

- 구성 파일을 구문 분석하고, 다른 사용자로 명령 실행이 허용되는지 확인:

`doas -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- `doas`가 이전에 제공된 후에도 비밀번호를 요청하도록 함:

`doas -L`
