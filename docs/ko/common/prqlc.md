---
layout: page
title: common/prqlc (한국어)
description: "PRQL 컴파일러."
content_hash: 9835a26f59b0f29730a7078d61a887d1101f18cc
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/prqlc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/prqlc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># prqlc

PRQL 컴파일러.
PRQL은 데이터를 변환하기 위한 현대적인 언어로, 간단하고 강력한 파이프라인 SQL 대체 언어입니다.
더 많은 정보: <https://prql-lang.org>.

- 대화형으로 컴파일러 실행:

`prqlc compile`

- 특정 `.prql` 파일을 `stdout`으로 컴파일:

`prqlc compile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.prql</span>

- `.prql` 파일을 `.sql` 파일로 컴파일:

`prqlc compile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.prql</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/타겟.sql</span>

- 쿼리 컴파일:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">from employees | filter has_dog | select salary</span>`" | prqlc compile`

- 디렉터리를 감시하고 파일 수정 시 컴파일:

`prqlc watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
