---
layout: page
title: linux/resolvectl (polski)
description: "Znajdź nazwy domen, adresy IPv4 i IPv6, rekordy zasobów DNS i usługi."
content_hash: 59aeeabf353514891c3b2f0972a45a957765d39f
last_modified_at: 2023-05-09
related_topics:
  - title: English version
    url: /en/linux/resolvectl.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># resolvectl

Znajdź nazwy domen, adresy IPv4 i IPv6, rekordy zasobów DNS i usługi.
Analizuj i rekonfiguruj resolwer DNS.
Więcej informacji: <https://www.freedesktop.org/software/systemd/man/resolvectl.html>.

- Wyświetl ustawienia DNS:

`resolvectl status`

- Znajdź adresy IPv4 i IPv6 jednej lub więcej domen:

`resolvectl query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domena1 domena2 ...</span>

- Znajdź domenę podanego adresu IP:

`resolvectl query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres_ip</span>

- Znajdź rekord MX podanej domeny:

`resolvectl --legend=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">no</span>` --type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MX</span>` query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domena</span>

- Znajdź rekord SRV, na przykład _xmpp-server._tcp gmail.com:

`resolvectl service _`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usługa</span>`._`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">protokół</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa</span>

- Pobierz klucz publiczny z adresu email z rekordu DNS OPENPGPGKEY:

`resolvectl openpgp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email</span>

- Znajdź klucz TLS:

`resolvectl tlsa tcp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domena</span>`:443`
