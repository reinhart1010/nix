---
layout: page
title: common/git-archive (Deutsch)
description: "Erstelle ein Archiv von Dateien."
content_hash: 37a2834e14e0fdc46ca5e14f515d649af6b6004e
last_modified_at: 2024-01-03
related_topics:
  - title: English version
    url: /en/common/git-archive.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-archive.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-archive.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-archive.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-archive.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git archive

Erstelle ein Archiv von Dateien.
Weitere Informationen: <https://git-scm.com/docs/git-archive>.

- Erstelle ein tar-Archiv aus dem Inhalt des aktuellen HEAD und gib dieses aus:

`git archive --verbose HEAD`

- Erstelle ein zip-Archiv aus dem Inhalt des aktuellen HEAD und gib dieses aus:

`git archive --verbose --format zip HEAD`

- Erstelle ein zip-Archiv aus dem Inhalt des aktuellen HEAD und speichere dieses in eine Datei:

`git archive --verbose --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.zip</span>` HEAD`

- Erstelle ein tar-Archiv aus dem Inhalt des letzten Commits eines bestimmten Branches:

`git archive --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Erstelle ein tar-Archiv aus dem Inhalt eines bestimmten Verzeichnisses:

`git archive --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.tar</span>` HEAD:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>

- Stelle jeder Datei einen Pfad voran, um sie in einem bestimmten Verzeichnis zu archivieren:

`git archive --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.tar</span>` --prefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>`/ HEAD`
