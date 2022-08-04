---
layout: page
title: common/git-apply (Deutsch)
description: "Integriere eine Patch-Datei und/oder füge sie zum Index hinzu."
content_hash: 1fcd2ad72a43d65bf7408f3a21e35f2407b0ba7d
related_topics:
  - title: English version
    url: /en/common/git-apply.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-apply.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-apply.html
    icon: bi bi-globe
---
# git apply

Integriere eine Patch-Datei und/oder füge sie zum Index hinzu.
Weitere Informationen: <https://git-scm.com/docs/git-apply>.

- Gib Informationen über gepatchte Dateien aus:

`git apply --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Integriere die Patch-Datei und füge sie zum Index hinzu:

`git apply --index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Integriere eine externe Patch-Datei:

`curl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://beispiel.de/datei.patch</span>` | git apply`

- Gib diffstat des Inputs aus und integriere die Patch-Datei:

`git apply --stat --apply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Integriere eine Patch-Datei in umgekehrter Reihenfolge:

`git apply --reverse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Speichere das Ergebnis einer Patch-Datei im Index, ohne den Arbeitsbaum zu verändern:

`git apply --cache `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>
