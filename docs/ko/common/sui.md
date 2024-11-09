---
layout: page
title: common/sui (한국어)
description: "Sui 네트워크와 상호작용."
content_hash: 7ae7bb7cc9ae2fb819f3041a0ffd9449bef0f7fa
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/sui.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sui.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sui

Sui 네트워크와 상호작용.
더 많은 정보: <https://docs.sui.io/references/cli/cheatsheet>.

- Sui 하위 명령 실행:

`sui `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위_명령</span>

- 스마트 계약을 위한 도구 빌드:

`sui move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위_명령</span>

- 스마트 계약 게시, 객체 정보 가져오기, 트랜잭션 실행 등:

`sui client `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위_명령</span>

- 로컬 네트워크 시작:

`sui start`

- 소스에서 업데이트:

`cargo install --locked --git https://github.com/MystenLabs/sui.git --branch testnet sui`
