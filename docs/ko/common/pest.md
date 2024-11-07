---
layout: page
title: common/pest (한국어)
description: "단순성에 중점을 둔 PHP 테스트 프레임워크."
content_hash: f9ce3428ad7b51df7d3c1a31a5f5848d907db52c
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pest.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pest.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pest

단순성에 중점을 둔 PHP 테스트 프레임워크.
더 많은 정보: <https://pestphp.com>.

- 현재 디렉토리에 표준 Pest 구성 초기화:

`pest --init`

- 현재 디렉토리의 테스트 실행:

`pest`

- 주어진 그룹으로 주석이 달린 테스트 실행:

`pest --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 테스트를 실행하고 커버리지 보고서를 `stdout`에 출력:

`pest --coverage`

- 커버리지를 포함한 테스트를 실행하고, 커버리지가 최소 퍼센트보다 적으면 실패:

`pest --coverage --min=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>

- 테스트를 병렬로 실행:

`pest --parallel`

- 변이를 포함한 테스트 실행:

`pest --mutate`
