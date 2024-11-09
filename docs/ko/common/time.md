---
layout: page
title: common/time (한국어)
description: "명령어 실행 시간을 측정."
content_hash: e495d118abeff9b2ab1d8a58244ee8f86fbf4738
last_modified_at: 2024-11-09
related_topics:
  - title: bosanski version
    url: /bs/common/time.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/time.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/time.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/time.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/time.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/common/time.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/common/time.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/time.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># time

명령어 실행 시간을 측정.
참고: `time`은 셸 내장 명령어이거나 독립 실행형 프로그램이거나 둘 다일 수 있습니다.
더 많은 정보: <https://manned.org/time>.

- `command`를 실행하고 시간 측정 결과를 `stdout`에 출력:

`time `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 매우 간단한 스톱워치 생성 (Bash에서만 작동):

`time read`
