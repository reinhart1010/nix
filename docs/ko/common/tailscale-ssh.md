---
layout: page
title: common/tailscale-ssh (한국어)
description: "Tailscale 머신에 SSH 접속 (리눅스 전용)."
content_hash: 49ca94ddc86abeeee7fb7382bc359e1f4a80a2a1
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/tailscale-ssh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tailscale ssh

Tailscale 머신에 SSH 접속 (리눅스 전용).
더 많은 정보: <https://tailscale.com/kb/1193/tailscale-ssh>.

- 호스트에서 SSH 광고/비활성화:

`sudo tailscale up --ssh=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true|false</span>

- Tailscale-SSH가 활성화된 특정 호스트에 SSH 접속:

`tailscale ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>
