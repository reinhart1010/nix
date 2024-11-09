---
layout: page
title: common/sui-client-faucet (한국어)
description: "Sui 파셋과 상호작용."
content_hash: ee0d3ad1a80f2c5b017ef47021b97e445268720c
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/sui-client-faucet.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sui-client-faucet.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sui client faucet

Sui 파셋과 상호작용.
더 많은 정보: <https://docs.sui.io/references/cli/client#request-a-sui-coin-from-faucet>.

- 활성 네트워크와 연관된 파셋에서 SUI 코인 받기:

`sui client faucet`

- 주소(별칭도 허용)에 대해 SUI 코인 받기:

`sui client faucet --address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주소</span>

- 커스텀 파셋에서 SUI 코인 받기:

`sui client faucet --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커스텀-파셋-URL</span>
