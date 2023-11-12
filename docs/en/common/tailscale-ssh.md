---
layout: page
title: common/tailscale-ssh (English)
description: "SSH to a Tailscale machine (Linux Only)."
content_hash: 9310732ea7ff0b7e81097aa1c9913a36a8e606c1
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# tailscale ssh

SSH to a Tailscale machine (Linux Only).
More information: <https://tailscale.com/kb/1193/tailscale-ssh>.

- Advertise/Disable SSH on the host:

`sudo tailscale up --ssh=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true|false</span>

- SSH to a specific host which has Tailscale-SSH enabled:

`tailscale ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>
