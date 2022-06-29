---
layout: page
title: common/nmap (English)
description: "Network exploration tool and security / port scanner."
content_hash: 44d5187bba6631bc4c9578b7148173bcc01ba9e7
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
Some features only activate when Nmap is run with root privileges.
More information: <https://nmap.org>.

- Check if an IP address is up, and guess the remote host's operating system:

`nmap -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_or_hostname</span>

- Try to determine whether the specified hosts are up (ping scan) and what their names are:

`nmap -sn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_or_hostname</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">optional_another_address</span>

- Also enable scripts, service detection, OS fingerprinting and traceroute:

`nmap -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address_or_addresses</span>

- Scan a specific list of ports (use '-p-' for all ports from 1 to 65535):

`nmap -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port1,port2,...,portN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address_or_addresses</span>

- Perform service and version detection of the top 1000 ports using default NSE scripts; writing results ('-oN') to output file:

`nmap -sC -sV -oN `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">top-1000-ports.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address_or_addresses</span>

- Scan target(s) carefully using 'default and safe' NSE scripts:

`nmap --script "default and safe" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address_or_addresses</span>

- Scan web server running on standard ports 80 and 443 using all available 'http-*' NSE scripts:

`nmap --script "http-*" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address_or_addresses</span>` -p 80,443`

- Perform a stealthy very slow scan ('-T0') trying to avoid detection by IDS/IPS and use decoy ('-D') source IP addresses:

`nmap -T0 -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">decoy1_ipaddress,decoy2_ipaddress,...,decoyN_ipaddress</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address_or_addresses</span>
