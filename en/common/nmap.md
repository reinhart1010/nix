---
layout: page
title: common/nmap (English)
description: "Network exploration tool and security / port scanner."
content_hash: bf6f93e3d413e3a54e656d9b13b78b38aeeb1cc2
related_topics:
  - title: español version
    url: /es/common/nmap.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/nmap.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/nmap.html
    icon: bi bi-globe
---
# nmap

Network exploration tool and security / port scanner.
Some features only activate when Nmap is run with privileges.
More information: <https://nmap.org>.

- Check if an IP address is up, and guess the remote host's operating system:

`nmap -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_or_hostname</span>

- Try to determine whether the specified hosts are up and what their names are:

`nmap -sn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_or_hostname</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">optional_another_address</span>

- Like above, but also run a default 1000-port TCP scan if host seems up:

`nmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_or_hostname</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">optional_another_address</span>

- Also enable scripts, service detection, OS fingerprinting and traceroute:

`nmap -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address_or_addresses</span>

- Assume good network connection and speed up execution:

`nmap -T4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address_or_addresses</span>

- Scan a specific list of ports (use `-p-` for all ports `1-65535`):

`nmap -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port1,port2,…,portN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address_or_addresses</span>

- Perform TCP and UDP scanning (use `-sU` for UDP only, `-sZ` for SCTP, `-sO` for IP):

`nmap -sSU `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address_or_addresses</span>

- Perform full port, service, version detection scan with all default NSE scripts active against a host to determine weaknesses and info:

`nmap -sC -sV `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address_or_addresses</span>
