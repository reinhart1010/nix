---
layout: page
title: linux/abbr (Deutsch)
description: "Abkürzungen für die fish shell verwalten."
content_hash: 36639dc9e5d26ef35f989a0c53113dd291592b76
related_topics:
  - title: English version
    url: /en/linux/abbr.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># abbr

Abkürzungen für die fish shell verwalten.
Die vom Nutzer definierten Abkürzungen werden nach der Eingabe durch die Langversionen ersetzt.
Mehr Informationen: <https://fishshell.com/docs/current/cmds/abbr.html>.

- Neue Abkürzung hinzufügen:

`abbr --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">abkürzungsname</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehlsparameter</span>

- Vorhandene Abkürzung umbenennen:

`abbr --rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alter_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">neuer_name</span>

- Vorhandene Abkürzung löschen:

`abbr --erase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">abkürzungsname</span>

- Abkürzungen eines anderen Host über SSH importieren:

`ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_name</span>` abbr --show | source`
