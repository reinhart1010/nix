---
layout: page
title: netbsd/sockstat (polski)
description: "Wyświetl listę otwartych gniazd internetowych lub UNIX-owych."
content_hash: 704f6f12385343b6d2c8a9b92854311eaaeac895
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/netbsd/sockstat.html
    icon: bi bi-globe
  - title: español version
    url: /es/netbsd/sockstat.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/netbsd/sockstat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/netbsd/sockstat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/netbsd/sockstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sockstat

Wyświetl listę otwartych gniazd internetowych lub UNIX-owych.
Uwaga: ten program jest przeróbką programu `sockstat` z FreeBSD dla NetBSD 3.0.
Zobacz także: `netstat`.
Więcej informacji: <https://man.netbsd.org/sockstat.1>.

- Pokaż informacje o gniazdach IPv4, IPv6 i Unix, zarówno nasłuchujących jak i połączonych:

`sockstat`

- Pokaż informacje o gniazdach IPv[4]/IPv[6] nasłuchujących (z ang. [l]istening) na określonych [p]ortach używając określonego [P]rotokołu:

`sockstat -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4|6</span>` -l -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp|udp|sctp|divert</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port1,port2...</span>

- Pokaż również połączone (z ang. [c]onnected) gniazda, wyświetlając gniazda [u]nixowe:

`sockstat -cu`

- Pokaż tylko wynik [n]umeryczny, bez rozwiązywania symbolicznych nazw dla adresów i portów:

`sockstat -n`

- Pokaż tylko gniazda dla określonej rodziny (z ang. [f]amily) adresów:

`sockstat -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">inet|inet6|local|unix</span>
