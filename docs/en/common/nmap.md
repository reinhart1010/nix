---
layout: page
title: common/nmap (English)
description: "Network exploration tool and security/port scanner."
content_hash: 06cc334440626a92d05a60f39cc59cf2e06b7449
last_modified_at: 2024-08-04
related_topics:
  - title: Deutsch version
    url: /de/common/nmap.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/nmap.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/nmap.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/nmap.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/nmap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nmap

Network exploration tool and security/port scanner.
Some features (e.g. SYN scan) activate only when `nmap` is run with root privileges.
More information: <https://nmap.org/book/man.html>.

- Scan the top 1000 ports of a remote host with various [v]erbosity levels:

`nmap -v`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|2|3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_or_hostname</span>

- Run a ping sweep over an entire subnet or individual hosts very aggressively:

`nmap -T5 -sn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.0/24|ip_or_hostname1,ip_or_hostname2,...</span>

- Enable OS detection, version detection, script scanning, and traceroute of hosts from a file:

`sudo nmap -A -iL `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>

- Scan a specific list of ports (use `-p-` for all ports from 1 to 65535):

`nmap -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port1,port2,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_or_host1,ip_or_host2,...</span>

- Perform service and version detection of the top 1000 ports using default NSE scripts, writing results (`-oA`) to output files:

`nmap -sC -sV -oA `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">top-1000-ports</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_or_host1,ip_or_host2,...</span>

- Scan target(s) carefully using `default and safe` NSE scripts:

`nmap --script "default and safe" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_or_host1,ip_or_host2,...</span>

- Scan for web servers running on standard ports 80 and 443 using all available `http-*` NSE scripts:

`nmap --script "http-*" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_or_host1,ip_or_host2,...</span>` -p 80,443`

- Attempt evading IDS/IPS detection by using an extremely slow scan (`-T0`), decoy source addresses (`-D`), [f]ragmented packets, random data and other methods:

`sudo nmap -T0 -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">decoy_ip1,decoy_ip2,...</span>` --source-port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">53</span>` -f --data-length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16</span>` -Pn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_or_host</span>
