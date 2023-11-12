---
layout: page
title: linux/tcpflow (polski)
description: "Przechwytuje ruch TCP do debugowania i analizy."
content_hash: c41f11496d6920fdbe8ae76eae8b26cdaac8b006
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/tcpflow.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/tcpflow.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/tcpflow.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tcpflow

Przechwytuje ruch TCP do debugowania i analizy.
Więcej informacji: <https://manned.org/tcpflow>.

- Pokaż wszystkie dane z interfejsu `eth0` i portu `80`:

`tcpflow -c -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>
