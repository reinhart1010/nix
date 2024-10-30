---
layout: page
title: common/gnomon (한국어)
description: "타임스탬프로 콘솔 로깅 문에 주석을 달고, 느린 프로세스를 찾는 유틸리티."
content_hash: cf498c2d721c8aae8c35410b3ba4ee180118c3f5
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/gnomon.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gnomon.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gnomon

타임스탬프로 콘솔 로깅 문에 주석을 달고, 느린 프로세스를 찾는 유틸리티.
더 많은 정보: <https://github.com/paypal/gnomon>.

- UNIX (또는 DOS) 파이프를 사용하여 gnomon을 통해 명령의 `stdout`을 파이프:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">npm test</span>` | gnomon`

- 프로세스 시작 이후 경과한 시간(초)를 표시:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">npm test</span>` | gnomon --type=elapsed-total`

- UTC로 절대 타임스탬프를 표시:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">npm test</span>` | gnomon --type=absolute`

- 0.5초의 높은 임계값을 사용, 이 값을 초과하면 타임스탬프가 밝은 빨간색으로 표시됨:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">npm test</span>` | gnomon --high 0.5`

- 0.2초의 중간 임계값을 사용, 이를 초과하면 타임스탬프가 밝은 노란색으로 표시됨:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">npm test</span>` | gnomon --medium `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.2</span>
