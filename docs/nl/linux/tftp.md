---
layout: page
title: linux/tftp (Nederlands)
description: "Trivial File Transfer Protocol client."
content_hash: 6e295116ad0b1296070ab48a7eeda376400502f2
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/linux/tftp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/tftp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tftp

Trivial File Transfer Protocol client.
Meer informatie: <https://manned.org/tftp.1>.

- Maak verbinding met een TFTP-server door het IP-adres en de poort op te geven:

`tftp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_ip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">poort</span>

- Maak verbinding met een TFTP-server en voer een TFTP-[c]ommand uit:

`tftp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_ip</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Maak verbinding met een TFTP-server met IPv6 en forceer dat de oorspronkelijke poort binnen een [R]ange ligt:

`tftp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_ip</span>` -6 -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">poort</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">poort</span>

- Stel de overdrachtsmodus in op binaire of ASCIi via de tftp-client:

`mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">binary|ascii</span>

- Download een bestand van een server via de tftp-client:

`get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Upload een bestand naar een server via de tftp-client:

`put `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Verlaat de tftp-client:

`quit`
