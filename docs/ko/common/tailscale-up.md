---
layout: page
title: common/tailscale-up (한국어)
description: "클라이언트를 Tailscale 네트워크에 연결."
content_hash: 968d64578933d35df05dc8eaac74d55c4bc18d7d
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/tailscale-up.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tailscale-up.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tailscale up

클라이언트를 Tailscale 네트워크에 연결.
버전 1.8 이상에서는 명령줄 인수가 저장되어 덮어쓰거나 `--reset`을 호출할 때까지 재사용됩니다.
더 많은 정보: <https://tailscale.com/kb/1080/cli/#up>.

- Tailscale에 연결:

`sudo tailscale up`

- 연결하고 현재 기기를 인터넷 트래픽의 종료 노드로 제공:

`sudo tailscale up --advertise-exit-node`

- 특정 노드를 인터넷 트래픽을 위한 종료 노드로 사용하여 연결:

`sudo tailscale up --exit-node=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">종료_노드_IP</span>

- 연결하고 현재 노드로의 수신 연결 차단:

`sudo tailscale up --shields-up`

- 연결하고 관리자 패널의 DNS 구성을 수락하지 않음 (기본값은 `true`):

`sudo tailscale up --accept-dns=false`

- 연결하고 Tailscale을 서브넷 라우터로 구성:

`sudo tailscale up --advertise-routes=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.0/24,10.0.1.0/24,...</span>

- 연결하고 Tailscale에서 서브넷 경로 수락:

`sudo tailscale up --accept-routes`

- 지정되지 않은 설정을 기본값으로 재설정하고 연결:

`sudo tailscale up --reset`
