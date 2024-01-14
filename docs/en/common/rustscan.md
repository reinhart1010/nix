---
layout: page
title: common/rustscan (English)
description: "Fast Port Scanner written in Rust with `nmap` built in."
content_hash: 6a86bba8c294c21a3c6c94d8e7e0dc7d907ea5b1
last_modified_at: 2024-01-14
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rustscan.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rustscan

Fast Port Scanner written in Rust with `nmap` built in.
More information: <https://github.com/RustScan/RustScan>.

- Scan all ports of one or more comma-delimited [a]ddresses using the default values:

`rustscan --addresses `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_or_hostname</span>

- Scan the [t]op 1000 ports with service and version detection:

`rustscan --top --addresses `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address_or_addresses</span>

- Scan a specific list of [p]orts:

`rustscan --ports `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port1,port2,...,portN</span>` --addresses `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address_or_addresses</span>

- Scan a specific range of ports:

`rustscan --range `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start-end</span>` --addresses `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address_or_addresses</span>

- Add script arguments to `nmap`:

`rustscan --addresses `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address_or_addresses</span>` -- -A -sC`

- Scan with custom [b]atch size (default: 4500) and [t]imeout (default: 1500ms):

`rustscan --batch-size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">batch_size</span>` --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">timeout</span>` --addresses `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address_or_addresses</span>

- Scan with specific port order:

`rustscan --scan-order `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">serial|random</span>` --addresses `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address_or_addresses</span>

- Scan in greppable mode (only output of the ports, no `nmap`):

`rustscan --greppable --addresses `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address_or_addresses</span>
