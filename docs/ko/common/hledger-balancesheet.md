---
layout: page
title: common/hledger-balancesheet (한국어)
description: "자산 및 부채 계정의 최종 잔액을 표시."
content_hash: a0c01eb3bfdbdeec14238a0e8ba3aa99db59a2f3
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/hledger-balancesheet.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/hledger-balancesheet.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># hledger balancesheet

자산 및 부채 계정의 최종 잔액을 표시.
금액은 일반 재무제표와 같이 정상적인 양의 부호로 표시됩니다.
더 많은 정보: <https://hledger.org/hledger.html#balancesheet>.

- 0을 제외한 `자산` 및 `부채` 계정의 현재 잔액 표시:

`hledger balancesheet`

- 유동 자산(`현금` 계정 유형)만 표시:

`hledger balancesheet type:C`

- 0 잔액의 계정을 포함하고 계정 계층 구조 표시:

`hledger balancesheet --empty --tree`

- 매월 말 잔액 표시:

`hledger balancesheet --monthly`

- 매월 말 잔액의 시장 가치를 홈 통화로 표시:

`hledger balancesheet --monthly -V`

- 분기별 잔액을 계정 계층 구조의 상위 두 레벨만 표시:

`hledger balancesheet --quarterly --tree --depth 2`

- 위의 명령의 간단한 형태로 `bs.html`에서 HTML 출력 생성:

`hledger bs -Qt -2 -o bs.html`
