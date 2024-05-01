---
layout: page
title: linux/sslstrip (English)
description: "Perform Moxie Marlinspike's Secure Sockets Layer (SSL) stripping attacks."
content_hash: 8b9d7f49cf96b470f15109dae4ae5d8e4d5a0fdc
last_modified_at: 2024-05-01
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/sslstrip.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sslstrip

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
