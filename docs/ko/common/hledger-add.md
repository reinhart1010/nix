---
layout: page
title: common/hledger-add (한국어)
description: "콘솔에서 대화형 프롬프트로 새로운 거래를 기록합니다."
content_hash: 33d651e70ae0e755057d9177a7087591356f0d42
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/hledger-add.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/hledger-add.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># hledger add

콘솔에서 대화형 프롬프트로 새로운 거래를 기록합니다.
더 많은 정보: <https://hledger.org/hledger.html#add>.

- 기본 저널 파일에 새로운 거래 기록:

`hledger add`

- `2024.journal`에 거래를 추가하되, 자동 완성을 위해 `2023.journal`도 로드:

`hledger add --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/2024.journal</span>` --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/2023.journal</span>

- 처음 네 개의 프롬프트에 대한 답변 제공:

`hledger add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">오늘</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">best buy</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">지출:용품</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$20</span>`'`

- `$PAGER`로 `add`의 옵션 및 문서 보기:

`hledger add --help`

- 사용 가능하면 `info` 또는 `man`으로 `add`의 문서 보기:

`hledger help add`
