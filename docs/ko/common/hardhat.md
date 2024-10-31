---
layout: page
title: common/hardhat (한국어)
description: "Ethereum 소프트웨어 개발 환경."
content_hash: 9a155eca73b12d11f0cc6f993f3ffdc9c347bbe0
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/hardhat.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/hardhat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># hardhat

Ethereum 소프트웨어 개발 환경.
더 많은 정보: <https://hardhat.org>.

- 사용 가능한 하위 명령어를 나열 (또는 구성 파일이 없는 경우, 새로운 프로젝트 생성):

`hardhat`

- 현재 프로젝트를 컴파일하고, 모든 아티팩트를 빌드:

`hardhat compile`

- 프로젝트를 컴파일한 후 사용자 정의 스크립트를 실행:

`hardhat run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.js</span>

- Mocha 테스트 실행:

`hardhat test`

- 주어진 모든 테스트 파일을 실행:

`hardhat test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.js</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2.js</span>

- 개발을 위해 로컬 Ethereum JSON-RPC 노드를 시작:

`hardhat node`

- 특정 호스트 이름과 포트를 사용하여 로컬 Ethereum JSON-RPC 노드를 시작:

`hardhat node --hostname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 캐시 및 모든 아티팩트 정리:

`hardhat clean`
