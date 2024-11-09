---
layout: page
title: common/sg (한국어)
description: "Ast-grep은 코드 구조 검색, 린트 및 재작성 도구입니다."
content_hash: 84822e038817eb3f7d95c522b82c84676d515f86
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/sg.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sg

Ast-grep은 코드 구조 검색, 린트 및 재작성 도구입니다.
더 많은 정보: <https://ast-grep.github.io/guide/introduction.html>.

- 대화형 모드를 사용하여 가능한 쿼리 스캔:

`sg scan --interactive`

- 패턴을 사용하여 현재 디렉토리의 코드 재작성:

`sg run --pattern '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>`' --rewrite '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>`' --lang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">python</span>

- 변경 사항을 적용하지 않고 시각화:

`sg run --pattern '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">useState<number>($A)</span>`' --rewrite '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">useState($A)</span>`' --lang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">typescript</span>

- 결과를 JSON으로 출력하고, `jq`를 사용하여 정보 추출 후 `jless`를 통해 대화형으로 보기:

`sg run --pattern '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Some($A)</span>`' --rewrite '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">None</span>`' --json | jq '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.[].replacement</span>`' | jless`
