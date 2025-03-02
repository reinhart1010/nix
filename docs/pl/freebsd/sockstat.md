---
layout: page
title: freebsd/sockstat (polski)
description: "Wyświetl listę otwartych gniazd internetowych lub UNIX-owych."
content_hash: 7e2a4a8a77505268cd69a1aad03fbb1456ac4810
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/freebsd/sockstat.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/freebsd/sockstat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/freebsd/sockstat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/freebsd/sockstat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/freebsd/sockstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sockstat

Wyświetl listę otwartych gniazd internetowych lub UNIX-owych.
Więcej informacji: <https://man.freebsd.org/cgi/man.cgi?sockstat>.

- Zobacz, którzy użytkownicy/procesy nasłuchują na których portach:

`sockstat -l`

- Pokaż informacje o gniazdach IPv[4]/IPv[6] nasłuchujących (z ang. [l]istening) na określonych [p]ortach używając określonego [P]rotokołu:

`sockstat -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4|6</span>` -l -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp|udp|sctp|divert</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port1,port2...</span>

- Pokaż również połączone (z ang. [c]onnected) gniazda, nie rozwiązując [n]umerycznych identyfikatorów UID do nazw użytkowników i używając szerszego (z ang. [w]ider) rozmiaru pola:

`sockstat -cnw`

- Pokaż tylko gniazda dla konkretnego [j]ail-a (ID/nazwa) w trybie informacji pełnej (z ang. [v]erbose mode):

`sockstat -jv`

- Wyświetl [s]tan protokołu i numer zdalnego portu enkapsulacji [U]DP, jeśli dotyczy (obecnie zaimplementowane tylko dla SCTP i TCP):

`sockstat -sU`

- Wyświetl moduł kontroli przeciążenia (z ang. [C]ongestion) i [S]tos protokołu, jeśli dotyczy (obecnie zaimplementowane tylko dla TCP):

`sockstat -CS`

- Pokaż tylko gniazda internetowe, których adresy (lokalne i zewnętrzne) nie należą do sieci pętli zwrotnej 127.0.0.0/8 ani nie zawierają adresu IPv6 ::1:

`sockstat -L`

- Nie pokazuj nagłówka (tryb cichy (z ang. [q]uiet)), pokazując gniazda [u]nix i wyświetlając `inp_gencnt`:

`sockstat -qui`
