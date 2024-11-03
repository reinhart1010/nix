---
layout: page
title: common/warp-cli (한국어)
description: "Cloudflare의 WARP 서비스에 대한 연결을 연결, 연결 해제하고 모드를 전환."
content_hash: 843d96d5f6405f60316d66c89bc9c6b3c48d7353
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/warp-cli.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/warp-cli.html
    icon: bi bi-globe
tldri18n_status: 2
---
# warp-cli

Cloudflare의 WARP 서비스에 대한 연결을 연결, 연결 해제하고 모드를 전환.
WARP는 개인정보 보호, 보안, 속도를 위해 트래픽을 암호화하는 VPN입니다.
같이 보기: `fastd`, `ivpn`, `mozillavpn`, `mullvad`.
더 많은 정보: <https://developers.cloudflare.com/warp-client/>.

- 현재 장치를 WARP에 등록 (첫 연결 전에 실행 필요):

`warp-cli registration new`

- WARP에 연결:

`warp-cli connect`

- WARP에서 연결 해제:

`warp-cli disconnect`

- WARP 연결 상태 표시:

`warp-cli status`

- 특정 모드로 전환:

`warp-cli set-mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모드</span>

- 도움말 표시:

`warp-cli help`

- 하위 명령에 대한 도움말 표시:

`warp-cli help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위_명령</span>
