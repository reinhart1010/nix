---
layout: page
title: linux/ahost (polski)
description: "Narzędzie zapytań DNS do wyświetlania rekordów A lub AAAA powiązanych z nazwą hosta lub adresem IP."
content_hash: d38445d29bd7a8a9c41d4a741983bf6cf236fed5
last_modified_at: 2023-10-23
related_topics:
  - title: English version
    url: /en/linux/ahost.html
    icon: bi bi-globe
---
# ahost

Narzędzie zapytań DNS do wyświetlania rekordów A lub AAAA powiązanych z nazwą hosta lub adresem IP.
Więcej informacji: <https://manned.org/ahost>.

- Wyświetl rekord `A` lub `AAAA` powiązany z nazwą hosta lub adresem IP::

`ahost `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Wyświetl dodatkowe wyjście debugowe:

`ahost -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Wyświetl rekord wskazanego typu:

`ahost -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a|aaaa|u</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
