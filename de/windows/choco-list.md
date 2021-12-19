---
layout: page
title: windows/choco-list (Deutsch)
description: "Zeige mit Chocolatey eine Liste von Paketen an."
content_hash: d46ca8fa856aba8cc871edcb26621f155f000237
related_topics:
  - title: English version
    url: /en/windows/choco-list.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-list.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-list.html
    icon: bi bi-globe
---
# choco list

Zeige mit Chocolatey eine Liste von Paketen an.
Weitere Informationen: <https://chocolatey.org/docs/commands-list>.

- Zeige alle verfügbaren Pakete an:

`choco list`

- Zeige alle lokal installierten Pakete an:

`choco list --local-only`

- Zeige eine Liste einschließlich der lokalen Windows-Programme an:

`choco list --include-programs`

- Zeige nur zugelassene Pakete an:

`choco list --approved-only`

- Gib eine eigene Quelle an, von der Paket-Informationen abgerufen werden:

`choco list --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quell_url|alias</span>

- Gib einen Benutzernamen und ein Passwort für die Authentifizierung an:

`choco list --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzername</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">passwort</span>
