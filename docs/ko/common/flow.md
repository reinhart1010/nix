---
layout: page
title: common/flow (한국어)
description: "JavaScript용 정적 유형 검사기."
content_hash: c767adc7284baa578b8f1f75d376d3703a7624b9
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/flow.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/flow.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># flow

JavaScript용 정적 유형 검사기.
더 많은 정보: <https://flow.org>.

- 흐름 검사를 실행:

`flow`

- 흐름별로 검사 중인 파일을 확인:

`flow ls`

- 디렉토리의 모든 파일에 대해 유형 검사를 실행:

`flow batch-coverage --show-all --strip-root `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 라인별 유형 적용 범위 통계 표시:

`flow coverage --color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.jsx</span>
