---
layout: page
title: common/npm-view (한국어)
description: "패키지에 대한 레지스트리 정보를 조회."
content_hash: c65a09c4031dcda4ac7e755467d402ed4209d84b
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/npm-view.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/npm-view.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># npm view

패키지에 대한 레지스트리 정보를 조회.
더 많은 정보: <https://docs.npmjs.com/cli/commands/npm-view>.

- 패키지의 최신 버전에 대한 정보 조회:

`npm view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 특정 버전의 패키지 정보 조회:

`npm view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 패키지의 모든 사용 가능한 버전 조회:

`npm view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` versions`

- 패키지 설명 조회:

`npm view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` description`

- 패키지의 최신 버전의 의존성 조회:

`npm view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` dependencies`

- 패키지의 저장소 URL 조회:

`npm view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` repository`

- 패키지의 관리자 조회:

`npm view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` maintainers`
