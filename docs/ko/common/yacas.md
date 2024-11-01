---
layout: page
title: common/yacas (한국어)
description: "또 다른 컴퓨터 대수 시스템."
content_hash: 09a42471c01b115101baf5047946f15b845055b8
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/yacas.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/yacas.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># yacas

또 다른 컴퓨터 대수 시스템.
더 많은 정보: <https://www.yacas.org>.

- 대화형 `yacas` 세션 시작:

`yacas`

- `yacas` 세션에서 문 실행:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Integrate(x)Cos(x)</span>`;`

- `yacas` 세션에서 예시 표시:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Example()</span>`;`

- `yacas` 세션 종료:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quit</span>

- 하나 이상의 `yacas` 스크립트를 실행하고(터미널이나 프롬프트 없이) 종료:

`yacas -p -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트2</span>

- 하나의 문을 실행하고 결과를 출력한 후 종료:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Echo( Deriv(x)Cos(1/x) );</span>`" | yacas -p -c /dev/stdin`
