---
layout: page
title: common/lastcomm (Deutsch)
description: "Zeige die zuletzt ausgeführten Befehle an."
content_hash: fa680ee742429e86c32a15dd663827b16bca59d6
last_modified_at: 2024-05-12
related_topics:
  - title: English version
    url: /en/common/lastcomm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lastcomm

Zeige die zuletzt ausgeführten Befehle an.
Weitere Informationen: <https://manpages.debian.org/latest/acct/lastcomm.1.en.html>.

- Gib Informationen zu allen Befehlen in acct aus (Aufzeichnungsdatei):

`lastcomm`

- Zeige die ausgeführten Befehle eines bestimmten Benutzers an:

`lastcomm --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzer</span>

- Zeige Informationen zu einem bestimmten Befehl an, der auf dem System ausgeführt wird:

`lastcomm --command `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>

- Zeige Informationen zu Befehlen an, die auf einem bestimmten Terminal ausgeführt wurden:

`lastcomm --tty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">terminal_name</span>
