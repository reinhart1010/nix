---
layout: page
title: common/git-format-patch (Deutsch)
description: "Erstelle `.patch` Dateien. Ermöglicht das Senden von Commits per E-Mail."
content_hash: da2402a74cc0a94dca332ffb6f3a86975683749f
last_modified_at: 2024-06-15
related_topics:
  - title: English version
    url: /en/common/git-format-patch.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-format-patch.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-format-patch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-format-patch.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-format-patch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git format-patch

Erstelle `.patch` Dateien. Ermöglicht das Senden von Commits per E-Mail.
Siehe auch `git am`, womit `.patch` Datein lokal angewandt werden.
Weitere Informationen: <https://git-scm.com/docs/git-format-patch>.

- Erzeuge eine `.patch` Datei aus allen nicht gepushten Commits:

`git format-patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origin</span>

- Erstelle eine `.patch` Datei aus allen Commits zwischen den angegebenen Revisionen und schreibe diese nach `stdout`:

`git format-patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revision_1</span>`..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revision_2</span>

- Erstelle eine `.patch` Datei aus den letzten 3 Commits:

`git format-patch -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>
