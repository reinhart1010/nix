---
layout: page
title: common/dlv (한국어)
description: "Go 프로그래밍 언어용 디버거."
content_hash: e7f70d1ee93791e456220897a915bd4d211de108
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/dlv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dlv

Go 프로그래밍 언어용 디버거.
더 많은 정보: <https://github.com/go-delve/delve/blob/master/Documentation/usage/dlv.md>.

- 현재 디렉터리에서 기본 패키지를 컴파일하고, 디버깅을 시작 (기본으로 인수가 없음):

`dlv debug`

- 특정 패키지를 컴파일하고 디버깅을 시작:

`dlv debug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수</span>

- 테스트 바이너리를 컴파일하고 컴파일된 프로그램 디버깅을 시작:

`dlv test`

- 헤드리스 디버그 서버에 연결:

`dlv connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_주소</span>

- 실행 중인 프로세스에 연결하고 디버깅을 시작:

`div attach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- 프로그램 컴파일 및 추적 시작:

`dlv trace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` --regexp '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>`'`
