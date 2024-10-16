---
layout: page
title: common/eva (한국어)
description: "구문 강조 및 지속적인 기록을 갖춘 `bc`와 유사한 간단한 계산기 REPL."
content_hash: 614e07cedc53f4bb4fdc34240c8cd888f8849443
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/eva.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/eva.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># eva

구문 강조 및 지속적인 기록을 갖춘 `bc`와 유사한 간단한 계산기 REPL.
더 많은 정보: <https://github.com/NerdyPepper/eva>.

- 대화형 모드에서 계산기 실행:

`eva`

- 표현식의 결과를 계산:

`eva "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(1 + 2) * 2 ^ 2</span>`"`

- 소수 자릿수를 5로 강제하는 표현식을 계산:

`eva --fix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5 / 3</span>`"`

- 사인과 코사인을 사용하여 표현식을 계산:

`eva "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sin(1) + cos(1)</span>`"`
