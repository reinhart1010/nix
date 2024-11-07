---
layout: page
title: common/ledger (한국어)
description: "강력한 복식부기 회계 시스템."
content_hash: fa064a71931ee8740489886af05ebaf997035adc
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/ledger.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ledger.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ledger

강력한 복식부기 회계 시스템.
더 많은 정보: <https://www.ledger-cli.org>.

- 총계를 보여주는 잔액 보고서 출력:

`ledger balance --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/ledger.journal</span>

- 금액순으로 정렬된 지출 내역의 모든 게시물 나열:

`ledger register `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">지출</span>` --sorted `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">금액</span>

- 음료 및 음식 이외의 총 지출 출력:

`ledger balance `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">지출</span>` and not (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">음료</span>` or `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">음식</span>`)`

- 예산 보고서 출력:

`ledger budget`

- 모든 게시물에 대한 요약 정보 출력:

`ledger stats`
