---
layout: page
title: common/naabu (English)
description: "A fast port scanner written in Go with a focus on reliability and simplicity."
content_hash: ab2f041963daea7f8b615be65c66c5f68aa1440c
last_modified_at: 2024-02-12
related_topics:
  - title: español version
    url: /es/common/naabu.html
    icon: bi bi-globe
tldri18n_status: 2
---
# naabu

A fast port scanner written in Go with a focus on reliability and simplicity.
Note: Some features are only activated when `naabu` is run with root privileges such as SYN scan.
More information: <https://github.com/projectdiscovery/naabu>.

- Run a SYN scan against default (top 100) ports of remote host:

`sudo naabu -host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Display available network interfaces and public IP address of the local host:

`naabu -interface-list`

- Scan all ports of the remote host (CONNECT scan without `sudo`):

`naabu -p - -host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Scan the top 1000 ports of the remote host:

`naabu -top-ports 1000 -host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Scan TCP ports 80, 443 and UDP port 53 of the remote host:

`naabu -p 80,443,u:53 -host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Show CDN type the remote host is using, if any:

`naabu -p 80,443 -cdn -host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Run `nmap` from `naabu` for additional functionalities (`nmap` must be installed):

`sudo naabu -v -host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` -nmap-cli 'nmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v -T5 -sC</span>`'`
