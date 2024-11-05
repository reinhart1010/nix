---
layout: page
title: common/nrm (한국어)
description: "npm 레지스트리 관리자."
content_hash: d100bc053461e7922f07af5c9f76035a552848b4
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/nrm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nrm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nrm

npm 레지스트리 관리자.
다양한 npm 레지스트리 간에 쉽게 전환할 수 있도록 도와줍니다.
더 많은 정보: <https://github.com/Pana/nrm>.

- 모든 레지스트리 나열:

`nrm ls`

- 특정 레지스트리로 변경:

`nrm use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레지스트리</span>

- 모든 레지스트리의 응답 시간 표시:

`nrm test`

- 사용자 정의 레지스트리 추가:

`nrm add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레지스트리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">URL</span>

- 레지스트리 삭제:

`nrm del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레지스트리</span>
