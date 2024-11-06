---
layout: page
title: common/hledger-accounts (한국어)
description: "계정 이름 목록."
content_hash: 8f273bc7a2ad0a2027f8b035b616d32b91e3f9da
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/hledger-accounts.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/hledger-accounts.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># hledger accounts

계정 이름 목록.
더 많은 정보: <https://hledger.org/hledger.html#accounts>.

- 기본 저널 파일에 사용되거나 선언된 모든 계정 표시:

`hledger accounts`

- 거래에 사용된 계정 표시:

`hledger accounts --used`

- 계정 지시문으로 선언된 계정 표시:

`hledger accounts --declared`

- 사용되었지만 선언되지 않은 계정에 대한 새 계정 지시문을 저널에 추가:

`hledger accounts --undeclared --directives >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2024-계정.journal</span>

- 이름에 `asset`이 포함된 계정 및 선언/추론된 유형 표시:

`hledger accounts asset --types`

- `Asset` 유형의 계정 표시:

`hledger accounts type:A`

- 계정 계층 구조의 처음 두 레벨 표시:

`hledger accounts --tree --depth 2`

- 위의 명령의 축약형:

`hledger acc -t -2`
