---
layout: page
title: common/sshuttle (English)
description: "Transparent proxy server that tunnels traffic over an SSH connection."
content_hash: 6217dc4f04b1cad376f1ce9c03014f305e0e5618
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/common/sshuttle.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sshuttle

Transparent proxy server that tunnels traffic over an SSH connection.
Doesn't require root or any special setup on the remote SSH server, though root access on the local machine is prompted for.
More information: <https://manned.org/sshuttle>.

- Forward all IPv4 TCP traffic via a remote SSH server:

`sshuttle --remote=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sshserver</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.0.0.0/0</span>

- Also forward all DNS traffic to the server's default DNS resolver:

`sshuttle --dns --remote=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sshserver</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.0.0.0/0</span>

- Forward all traffic except that which is bound for a specific subnet:

`sshuttle --remote=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sshserver</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.0.0.0/0</span>` --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1/24</span>

- Use the tproxy method to forward all IPv4 and IPv6 traffic:

`sshuttle --method=tproxy --remote=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sshserver</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.0.0.0/0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">::/0</span>` --exclude=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">your_local_ip_address</span>` --exclude=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh_server_ip_address</span>
