---
layout: page
title: linux/sslstrip (English)
description: "Perform Moxie Marlinspike's Secure Sockets Layer (SSL) stripping attacks."
content_hash: 8b9d7f49cf96b470f15109dae4ae5d8e4d5a0fdc
last_modified_at: 2024-05-02
tldri18n_status: 2
---
# sslstrip

Perform Moxie Marlinspike's Secure Sockets Layer (SSL) stripping attacks.
Perform an ARP spoofing attack in conjunction.
More information: <https://www.kali.org/tools/sslstrip/>.

- Log only HTTPS POST traffic on port 10000 by default:

`sslstrip`

- Log only HTTPS POST traffic on port 8080:

`sslstrip --listen=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8080</span>

- Log all SSL traffic to and from the server on port 8080:

`sslstrip --ssl --listen=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8080</span>

- Log all SSL and HTTP traffic to and from the server on port 8080:

`sslstrip --listen=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8080</span>` --all`

- Specify the file path to store the logs:

`sslstrip --listen=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8080</span>` --write=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display help:

`sslstrip --help`
