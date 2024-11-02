---
layout: page
title: common/qalc (한국어)
description: "강력하고 사용하기 쉬운 명령줄 계산기."
content_hash: c0c464b4fc1a7b6fc5b9aeb84ac96c201c64d2ca
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/qalc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/qalc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/qalc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qalc

강력하고 사용하기 쉬운 명령줄 계산기.
같이 보기: `bc`.
더 많은 정보: <https://qalculate.github.io/manual/qalc.html>.

- [i]nteractive 모드로 시작:

`qalc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--interactive</span>

- [t]erse 모드로 시작 (결과만 출력):

`qalc --terse`

- 통화 환율 [e] 갱신:

`qalc --exrates`

- 비대화식으로 계산 수행:

`qalc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">66+99|2^4|6 feet to cm|1 bitcoin to USD|20 kmph to mph|...</span>

- 지원되는 모든 함수/접두사/단위/변수 나열:

`qalc --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">list-functions|list-prefixes|list-units|list-variables</span>

- [f]ile에서 명령 실행:

`qalc --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
