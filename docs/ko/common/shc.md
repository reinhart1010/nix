---
layout: page
title: common/shc (한국어)
description: "범용 쉘 스크립트 컴파일러."
content_hash: f93ba1d4f4acf6e7bec64a19a18d88ef1a17e202
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/shc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shc

범용 쉘 스크립트 컴파일러.
더 많은 정보: <https://manned.org/shc>.

- 쉘 스크립트 컴파일:

`shc -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스크립트</span>

- 쉘 스크립트를 컴파일하고 출력 바이너리 파일 지정:

`shc -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스크립트</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">바이너리</span>

- 쉘 스크립트를 컴파일하고 실행 파일의 만료 날짜 설정:

`shc -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스크립트</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">일/월/연도</span>

- 쉘 스크립트를 컴파일하고 만료 시 표시할 메시지 설정:

`shc -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스크립트</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">일/월/연도</span>` -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제공자에게 문의하세요</span>`"`
