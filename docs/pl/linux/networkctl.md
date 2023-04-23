---
layout: page
title: linux/networkctl (polski)
description: "Zapytaj o stan łączy sieciowych."
content_hash: 86b35001c2bb668c0c5cf7dfe924ce0fc8885229
last_modified_at: 2023-04-23
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># networkctl

Zapytaj o stan łączy sieciowych.
Zarządzaj konfiguracją sieci za pomocą `systemd-networkd`.
Więcej informacji: <https://www.freedesktop.org/software/systemd/man/networkctl.html>.

- Wyświetl listę istniejących łączy i ich status:

`networkctl list`

- Wyświetl ogólny status sieci:

`networkctl status`

- Włącz urządzenia sieciowe:

`networkctl up `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interfejs1 interfejs2 ...</span>

- Wyłącz urządzenia sieciowe:

`networkctl down `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interfejs1 interfejs2 ...</span>

- Odnów konfiguracje dynamiczne (np. adresy IP przydzielone przez serwer DHCP):

`networkctl renew `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interfejs1 interfejs2 ...</span>

- Przeładuj pliki konfiguracyjne (.netdev i .network):

`networkctl reload`

- Rekonfiguruj interfejsy sieciowe (jeżeli pliki konfiguracyjne były edytowane, najpierw uruchom `networkctl reload`):

`networkctl reconfigure `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interfejs1 interfejs2 ...</span>
