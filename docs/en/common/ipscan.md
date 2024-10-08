---
layout: page
title: common/ipscan (English)
description: "A fast network scanner designed to be simple to use."
content_hash: edac5de74178948fb27056c0b98c33fc73095ab0
last_modified_at: 2024-08-24
tldri18n_status: 2
---
# ipscan

A fast network scanner designed to be simple to use.
Also known as Angry IP Scanner.
More information: <https://angryip.org/>.

- Scan a specific IP address:

`ipscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1</span>

- Scan a range of IP addresses:

`ipscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1-254</span>

- Scan a range of IP addresses and save the results to a file:

`ipscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1-254</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.txt</span>

- Scan IPs with a specific set of ports:

`ipscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1-254</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80,443,22</span>

- Scan with a delay between requests to avoid network congestion:

`ipscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1-254</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">200</span>

- Display help:

`ipscan --help`
