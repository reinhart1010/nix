---
layout: page
title: linux/nologin (Deutsch)
description: "Alternative Shell, die verhindert, dass sich ein Benutzer einloggt."
content_hash: 7133ad43e102e4b79a5374f3725edbb56b6d7867
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/nologin.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/nologin.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nologin

Alternative Shell, die verhindert, dass sich ein Benutzer einloggt.
Weitere Informationen: <https://manned.org/nologin.5>.

- Setze die Login-Shell eines Benutzers auf `nologin`, um zu verhindern, dass der Benutzer sich anmeldet:

`chsh -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` nologin`

- Passe die Nachricht für Benutzer mit Login-Shell `nologin` an:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nachricht</span>`" > /etc/nologin.txt`
