---
layout: page
title: common/lp (한국어)
description: "파일을 인쇄합니다."
content_hash: 135aa8e723d0bbb58af5c73c0f363f3ab11af925
last_modified_at: 2024-11-08
related_topics:
  - title: Deutsch version
    url: /de/common/lp.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/lp.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/lp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lp

파일을 인쇄합니다.
더 많은 정보: <https://manned.org/lp>.

- 명령어의 출력을 기본 프린터로 인쇄 (참고: `lpstat` 명령어):

`echo "test" | lp`

- 파일을 기본 프린터로 인쇄:

`lp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일이름</span>

- 파일을 지정된 프린터로 인쇄 (참고: `lpstat` 명령어):

`lp -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프린터_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일이름</span>

- 파일을 기본 프린터로 N부 인쇄 (N을 원하는 복사본 수로 대체):

`lp -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일이름</span>

- 특정 페이지만 기본 프린터로 인쇄 (페이지 1, 3-5, 16번 인쇄):

`lp -P 1,3-5,16 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일이름</span>

- 인쇄 작업 재개:

`lp -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_ID</span>` -H resume`
