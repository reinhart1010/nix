---
layout: page
title: common/objdump (한국어)
description: "오브젝트 파일에 대한 정보를 표시."
content_hash: a02cd77f2291978415838b598fd66d07cfa11e88
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/objdump.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/objdump.html
    icon: bi bi-globe
tldri18n_status: 2
---
# objdump

오브젝트 파일에 대한 정보를 표시.
더 많은 정보: <https://manned.org/objdump>.

- 파일 헤더 정보를 표시:

`objdump -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">바이너리</span>

- 모든 헤더 정보를 표시:

`objdump -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">바이너리</span>

- 실행 가능한 섹션의 디스어셈블리 출력 표시:

`objdump -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">바이너리</span>

- 인텔 구문으로 실행 가능한 섹션의 디스어셈블리 출력 표시:

`objdump -M intel -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">바이너리</span>

- 모든 섹션의 전체 바이너리 헥스 덤프 표시:

`objdump -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">바이너리</span>
