---
layout: page
title: linux/rpcinfo (Nederlands)
description: "Maak een RPC-oproep naar een RPC-server en rapporteert wat het vindt."
content_hash: e4b3b3466192ed738e205b355ad83b97821a7e5f
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/linux/rpcinfo.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/rpcinfo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rpcinfo

Maak een RPC-oproep naar een RPC-server en rapporteert wat het vindt.
Meer informatie: <https://manned.org/rpcinfo>.

- Toon volledige tabel van alle RPC-diensten geregistreerd op localhost:

`rpcinfo`

- Toon beknopte tabel van alle RPC-diensten geregistreerd op localhost:

`rpcinfo -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">localhost</span>

- Toon tabel met statistieken van rpcbind-operaties op localhost:

`rpcinfo -m`

- Toon lijst van items van een bepaalde service naam (mountd) en versienummer (2) op een remote nfs-share:

`rpcinfo -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_nfs_server_ip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mountd</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- Verwijder de registratie voor versie 1 van de mountd-service voor alle transporten:

`rpcinfo -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mountd</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>
