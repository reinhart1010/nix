---
layout: page
title: common/pueue-log (한국어)
description: "하나 이상의 작업에 대한 로그 출력을 표시합니다."
content_hash: 41c8955101f30a2eb92592dd6c15d57baad46a7e
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/pueue-log.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pueue-log.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pueue log

하나 이상의 작업에 대한 로그 출력을 표시합니다.
같이 보기: `pueue status`.
더 많은 정보: <https://github.com/Nukesor/pueue>.

- 모든 작업의 마지막 몇 줄의 출력 표시:

`pueue log`

- 특정 작업의 전체 출력 표시:

`pueue log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>

- 여러 작업의 마지막 몇 줄의 출력 표시:

`pueue log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>

- 출력의 끝에서 특정 줄 수 만큼의 줄을 출력:

`pueue log --lines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_lines</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>
