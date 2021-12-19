---
layout: page
title: linux/nologin (Deutsch)
description: "Alternative Shell, die verhindert, dass sich ein Benutzer einloggt."
content_hash: a8ff3f6f594d1979cb4a924b7766a27d04ba10bd
related_topics:
  - title: English version
    url: /en/linux/nologin.html
    icon: bi bi-globe
---
# nologin

Alternative Shell, die verhindert, dass sich ein Benutzer einloggt.

- Setze die Login-Shell eines Benutzers auf `nologin`, um zu verhindern, dass der Benutzer sich anmeldet:

`chsh -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` nologin`

- Passe die Nachricht für Benutzer mit Login-Shell `nologin` an:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nachricht</span>`" > /etc/nologin.txt`
