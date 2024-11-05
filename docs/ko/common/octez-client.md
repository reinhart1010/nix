---
layout: page
title: common/octez-client (한국어)
description: "Tezos 블록체인과 상호작용."
content_hash: 717bab33b73679866eea04a74d1266591653fe51
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/octez-client.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/octez-client.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/octez-client.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># octez-client

Tezos 블록체인과 상호작용.
더 많은 정보: <https://tezos.gitlab.io/introduction/howtouse.html#client>.

- <https://rpc.ghostnet.teztnets.com>과 같은 Tezos RPC 노드에 연결하여 클라이언트 구성:

`octez-client -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">엔드포인트</span>` config update`

- 계정을 생성하고 로컬 별칭을 지정:

`octez-client gen keys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">별칭</span>

- 별칭이나 주소로 계정의 잔액 확인:

`octez-client get balance for `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">별칭_또는_주소</span>

- 다른 계정으로 tez 전송:

`octez-client transfer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">별칭|주소</span>` to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">별칭|주소</span>

- 스마트 계약 생성(배포), 로컬 별칭 지정 및 초기 저장소를 Michelson-인코딩된 값으로 설정:

`octez-client originate contract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">별칭</span>` transferring `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">별칭|주소</span>` running `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_파일.tz</span>` --init "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">초기_저장소</span>`" --burn_cap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- 별칭이나 주소로 스마트 계약 호출 및 Michelson-인코딩된 매개변수 전달:

`octez-client transfer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">별칭|주소</span>` to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">계약</span>` --entrypoint "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">엔트리포인트</span>`" --arg "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">매개변수</span>`" --burn-cap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- 도움말 표시:

`octez-client man`
