---
layout: page
title: common/hledger-balance (한국어)
description: "유연하고 일반적인 \"합계\" 보고서로, 숫자 데이터가 포함된 계정을 보여줍니다."
content_hash: eb9c9c4e6729ea28e33c07a7e0538ef21f0799bd
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/hledger-balance.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/hledger-balance.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/hledger-balance.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># hledger balance

유연하고 일반적인 "합계" 보고서로, 숫자 데이터가 포함된 계정을 보여줍니다.
이는 기간별 잔액 변화, 종료 잔액, 예산 성과, 미실현 자본 이득 등을 포함할 수 있습니다.
더 많은 정보: <https://hledger.org/hledger.html#balance>.

- 모든 시간 동안 모든 계좌의 모든 기입에서 잔액 변화를 표시:

`hledger balance`

- `*expenses*`로 명명된 계정에서, 상위 두 수준만 요약하여 트리 형태로 잔액 변화를 표시:

`hledger balance `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expenses</span>` --tree --depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- 매월 비용, 총계 및 평균을 표시하고, 총계로 정렬하며 월간 예산 목표 포함:

`hledger balance `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expenses</span>` --monthly --row-total --average --sort-amount --budget`

- 위와 유사하지만, `Expense` 유형으로 계정을 일치시키고, 지루한 계정을 생략하지 않고 두 개의 수준 트리로 표시:

`hledger bal type:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">X</span>` -MTAS --budget -t -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` --no-elide`

- 종료 잔액을 2024년 분기별로, `*assets*` 또는 `*liabilities*`로 명명된 계정에서 표시 (시작일 이전의 기입 포함):

`hledger balance --historical --period '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quarterly in 2024</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">assets</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">liabilities</span>

- 위와 유사하지만, 0 잔액도 표시하고, 총계로 정렬하여 세 개의 수준으로 요약:

`hledger bal -HQ date:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2024</span>` type:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AL</span>` -ES -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- 각 분기 말에 기본 통화로 투자 자산의 시장 가치를 표시:

`hledger bal -HVQ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">assets:investments</span>

- 암호화폐가 아닌 투자 자산에 대한 각 분기의 시장 가격 변동으로 인한 미실현 자본 이득/손실 표시:

`hledger bal --gain -Q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">assets:investments</span>` not:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cryptocurrency</span>
