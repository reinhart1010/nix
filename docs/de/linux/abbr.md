---
layout: page
title: linux/abbr (Deutsch)
description: "Abkürzungen für die fish shell verwalten."
content_hash: 6d4477df02a185c0cd37b28b53587dd1713e5c33
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/abbr.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/abbr.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/abbr.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/abbr.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/abbr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/abbr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/abbr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# abbr

Abkürzungen für die fish shell verwalten.
Die vom Nutzer definierten Abkürzungen werden nach der Eingabe durch die Langversionen ersetzt.
Weitere Informationen: <https://fishshell.com/docs/current/cmds/abbr.html>.

- Neue Abkürzung hinzufügen:

`abbr --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">abkürzungsname</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehlsparameter</span>

- Vorhandene Abkürzung umbenennen:

`abbr --rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alter_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">neuer_name</span>

- Vorhandene Abkürzung löschen:

`abbr --erase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">abkürzungsname</span>

- Abkürzungen eines anderen Host über SSH importieren:

`ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_name</span>` abbr --show | source`
