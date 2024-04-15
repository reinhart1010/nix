---
layout: page
title: common/masscan (English)
description: "Network scanner for scanning as fast as possible."
content_hash: a5bfabc687bf861a0b88e358651117f8f95c4b1b
last_modified_at: 2024-04-15
related_topics:
  - title: polski version
    url: /pl/common/masscan.html
    icon: bi bi-globe
tldri18n_status: 2
---
# masscan

Network scanner for scanning as fast as possible.
Best run with elevated privileges. Nmap compatibility run `masscan --nmap` to find out more.
More information: <https://github.com/robertdavidgraham/masscan>.

- Scan an IP or network subnet for [p]ort 80:

`masscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address|network_prefix</span>` --ports `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>

- Scan a class B subnet for the top 100 ports at 100,000 packets per second:

`masscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.0/16</span>` --top-ports `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --rate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100000</span>

- Scan a class B subnet avoiding ranges from a specific exclude file:

`masscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.0/16</span>` --top-ports `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --excludefile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Scan the Internet for web servers running on port 80 and 443:

`masscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.0.0.0/0</span>` --ports `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80,443</span>` --rate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10000000</span>

- Scan the Internet for DNS servers running on UDP port 53:

`masscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.0.0.0/0</span>` --ports `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">U:53</span>` --rate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10000000</span>

- Scan the Internet for a specific port range and export to a file:

`masscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.0.0.0/0</span>` --ports `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0-65535</span>` --output-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">binary|grepable|json|list|xml</span>` --output-filename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Read binary scan results from a file and output to `stdout`:

`masscan --readscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
