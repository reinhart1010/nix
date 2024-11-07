---
layout: page
title: common/lex (한국어)
description: "어휘 분석기 생성기."
content_hash: 610891d834b995d6d47f06426e06fc6c9c755dc1
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/lex.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/lex.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/lex.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># lex

어휘 분석기 생성기.
어휘 분석기의 명세가 주어지면 이를 구현하는 C 코드를 생성합니다.
참고: 대부분의 주요 운영 체제에서 이 명령은 `flex`의 별칭입니다.
더 많은 정보: <https://manned.org/lex.1>.

- Lex 파일로부터 분석기를 생성하고, `lex.yy.c` 파일에 저장:

`lex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">분석기.l</span>

- 출력 파일 지정:

`lex -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">분석기.l</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">분석기.c</span>

- Lex가 생성한 C 파일 컴파일:

`c99 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/lex.yy.c</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">실행_파일</span>
