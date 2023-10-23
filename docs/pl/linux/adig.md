---
layout: page
title: linux/adig (polski)
description: "Wyświetla informacje otrzymane z serwerów DNS (Domain Name System)."
content_hash: b19d55cbd7225f3bfde100eac320ffe0c53639df
last_modified_at: 2023-10-23
related_topics:
  - title: English version
    url: /en/linux/adig.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/adig.html
    icon: bi bi-globe
---
# adig

Wyświetla informacje otrzymane z serwerów DNS (Domain Name System).
Więcej informacji: <https://manned.org/adig>.

- Wyświetl rekord A (domyślny) z DNS dla hosta(-ów):

`adig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Wyświetl dodatkowe wyjście [d]ebugowania:

`adig -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Podłącz do określonego [s]erwera DNS:

`adig -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.3.4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Użyj określonego portu TCP łącząc się do serwera DNS:

`adig -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Użyj określonego portu UDP łącząc się do serwera DNS:

`adig -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
