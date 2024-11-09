---
layout: page
title: common/solcjs (한국어)
description: "Solidity 컴파일러를 위한 JavaScript 바인딩 세트."
content_hash: 08875832475a3d5d694d8886dfcd39014f42ae29
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/solcjs.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/solcjs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># solcjs

Solidity 컴파일러를 위한 JavaScript 바인딩 세트.
더 많은 정보: <https://github.com/ethereum/solc-js>.

- 특정 계약을 16진수로 컴파일:

`solcjs --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.sol</span>

- 특정 계약의 ABI를 컴파일:

`solcjs --abi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.sol</span>

- 가져오기를 해석할 기본 경로 지정:

`solcjs --bin --base-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.sol</span>

- 외부 코드가 포함된 하나 이상의 경로 지정:

`solcjs --bin --include-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.sol</span>

- 생성된 바이트코드 최적화:

`solcjs --bin --optimize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.sol</span>
