---
layout: page
title: common/printenv (한국어)
description: "모든 환경 변수 또는 지정된 환경 변수의 값을 출력."
content_hash: c73daca03a4eddcdf768825fbe15484399841633
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/printenv.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/printenv.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/printenv.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># printenv

모든 환경 변수 또는 지정된 환경 변수의 값을 출력.
더 많은 정보: <https://www.gnu.org/software/coreutils/printenv>.

- 모든 환경 변수의 키-값 쌍 출력:

`printenv`

- 특정 변수의 값 출력:

`printenv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HOME</span>

- 변수를 출력하고 줄바꿈 대신 NUL로 끝내기:

`printenv --null `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HOME</span>
