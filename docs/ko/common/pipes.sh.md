---
layout: page
title: common/pipes.sh (한국어)
description: "터미널에 무작위 경로의 파이프를 그리는 Bash 스크립트."
content_hash: c9bf525fcd6d7422a2a88f3145bfc727a875de52
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pipes.sh.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pipes.sh.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pipes.sh

터미널에 무작위 경로의 파이프를 그리는 Bash 스크립트.
더 많은 정보: <https://github.com/pipeseroni/pipes.sh>.

- 파이프의 패턴 변경:

`pipes.sh -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0..9</span>

- 파이프의 색상 변경:

`pipes.sh -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0..7</span>

- 파이프의 프레임 속도 변경:

`pipes.sh -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20..100</span>

- 색상 비활성화:

`pipes.sh -C`

- 버전 표시:

`pipes.sh -v`
