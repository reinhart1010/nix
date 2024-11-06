---
layout: page
title: common/hledger-incomestatement (한국어)
description: "보고 기간 동안 수익 유입과 비용 유출 표시."
content_hash: a083917055d63cd1cf58b36df151d13070228a28
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/hledger-incomestatement.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/hledger-incomestatement.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># hledger incomestatement

보고 기간 동안 수익 유입과 비용 유출 표시.
금액은 일반적인 재무제표처럼 정상적인 양수 기호로 표시됩니다.
더 많은 정보: <https://hledger.org/hledger.html#incomestatement>.

- 수익과 비용(수익 및 비용 계정의 변화) 표시:

`hledger incomestatement`

- 매월 수익과 비용 표시:

`hledger incomestatement --monthly`

- 매월 수익/비용/총액을 가장 큰 것부터 두 단계로 요약하여 표시:

`hledger incomestatement --monthly --row-total --average --sort --depth 2`

- 위 명령의 단축형으로, `is.html`에 HTML 출력 생성:

`hledger is -MTAS -2 -o is.html`
