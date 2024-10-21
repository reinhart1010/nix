---
layout: page
title: common/gdc (한국어)
description: "GCC를 백엔드로 사용하는 D 컴파일러."
content_hash: ad100498581c7dce18bdb29bf1a6050f93d8b3ed
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/gdc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gdc

GCC를 백엔드로 사용하는 D 컴파일러.
더 많은 정보: <https://wiki.dlang.org/Using_GDC>.

- 실행 파일을 생성:

`gdc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.d</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_실행파일</span>

- 모듈 종속성에 대한 정보를 출력:

`gdc -fdeps`

- Ddoc 문서를 생성:

`gdc -fdoc`

- D 인터페이스 파일 생성:

`gdc -fintfc`

- 컴파일 시 표준 GCC 라이브러리를 링크하지 않음:

`gdc -nostdlib`
