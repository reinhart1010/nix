---
layout: page
title: common/shc (한국어)
description: "범용 쉘 스크립트 컴파일러."
content_hash: f93ba1d4f4acf6e7bec64a19a18d88ef1a17e202
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/shc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/shc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># shc

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
