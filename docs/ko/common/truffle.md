---
layout: page
title: common/truffle (한국어)
description: "Ethereum 블록체인에서 서비스를 실행하기 위한 스마트 계약 개발 도구."
content_hash: eb0d7b6da83a0aa3febe59cf2a6ed594156217c2
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/truffle.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/truffle.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># truffle

Ethereum 블록체인에서 서비스를 실행하기 위한 스마트 계약 개발 도구.
더 많은 정보: <https://www.trufflesuite.com/docs/truffle/reference/truffle-commands>.

- 미리 만들어진 Truffle 프로젝트(Truffle Box) 다운로드:

`truffle unbox `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">박스_이름</span>

- 현재 디렉토리의 계약 소스 파일 컴파일:

`truffle compile`

- JavaScript 및 Solidity 테스트 실행:

`truffle test`

- 계약 배포를 위한 마이그레이션 실행:

`truffle migrate`

- 하위 명령에 대한 도움말 표시:

`truffle help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위_명령</span>
