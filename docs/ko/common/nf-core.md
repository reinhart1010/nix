---
layout: page
title: common/nf-core (한국어)
description: "Nextflow의 모범 사례 지침을 생성, 검사 및 개발하기 위한 nf-core 프레임워크 도구."
content_hash: 909d3aa69dffee798e6891868a07906d09c77369
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/nf-core.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nf-core.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nf-core

Nextflow의 모범 사례 지침을 생성, 검사 및 개발하기 위한 nf-core 프레임워크 도구.
더 많은 정보: <https://nf-co.re/docs/nf-core-tools>.

- nf-core에서 기존 파이프라인 나열:

`nf-core list`

- 새 파이프라인 스켈레톤 생성:

`nf-core create`

- 파이프라인 코드 린트:

`nf-core lint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 파이프라인 레시피의 소프트웨어 버전 업그레이드:

`nf-core bump-version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_버전</span>

- nf-core 파이프라인 실행:

`nf-core launch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파이프라인_이름</span>

- 오프라인 사용을 위한 nf-core 파이프라인 다운로드:

`nf-core download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파이프라인_이름</span>
