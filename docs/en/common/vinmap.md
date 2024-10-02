---
layout: page
title: common/vinmap (English)
description: "A multithreaded Nmap scanner that splits IP ranges into chunks, performs parallel scans, and merges XML or JSON results."
content_hash: 3b07cb6ed1829af2cd13b8c6fc8b160b270341d7
last_modified_at: 2024-10-02
tldri18n_status: 2
---
# vinmap

A multithreaded Nmap scanner that splits IP ranges into chunks, performs parallel scans, and merges XML or JSON results.
More information: <https://pypi.org/project/vinmap>.

- Perform a basic scan of a subnet:

`vinmap -ip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.0/24</span>

- Scan a domain with version and OS detection, saving results to a specific file:

`vinmap -ip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` -s "-sV -O" -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/scan_results.xml</span>

- Scan an IP range using 10 chunks and 20 concurrent threads, uses half of the system's CPU cores if not specified:

`vinmap -ip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.1-10.0.0.255</span>` -n 10 -t 20`

- Output scan results in JSON format:

`vinmap -ip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.1-192.168.1.100</span>` -f json`

- Scan multiple IPs with default settings and save merged XML output:

`vinmap -ip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.1,192.168.1.2,...</span>
