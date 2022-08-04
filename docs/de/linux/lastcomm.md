---
layout: page
title: linux/lastcomm (Deutsch)
description: "Zeige die zuletzt ausgeführten Befehle an."
content_hash: f60178784260cb4019bb60425b05cb75247579dc
related_topics:
  - title: English version
    url: /en/linux/lastcomm.html
    icon: bi bi-globe
---
# lastcomm

Zeige die zuletzt ausgeführten Befehle an.
Weitere Informationen: <https://manpages.debian.org/stable/acct/lastcomm.1.en.html>.

- Gib Informationen zu allen Befehlen in acct aus (Aufzeichnungsdatei):

`lastcomm`

- Zeige die ausgeführten Befehle eines bestimmten Benutzers an:

`lastcomm --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzer</span>

- Zeige Informationen zu einem bestimmten Befehl an, der auf dem System ausgeführt wird:

`lastcomm --command `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>

- Zeige Informationen zu Befehlen an, die auf einem bestimmten Terminal ausgeführt wurden:

`lastcomm --tty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">terminal_name</span>
