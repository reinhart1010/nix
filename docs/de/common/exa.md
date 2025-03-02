---
layout: page
title: common/exa (Deutsch)
description: "Ein moderner Ersatz für `ls` (Verzeichnisinhalte auflisten)."
content_hash: 9a1df5d05df3619718c37700165c3d367d722d10
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/exa.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/exa.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/exa.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/exa.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/exa.html
    icon: bi bi-globe
tldri18n_status: 2
---
# exa

Ein moderner Ersatz für `ls` (Verzeichnisinhalte auflisten).
Weitere Informationen: <https://github.com/ogham/exa>.

- Liste eine Datei pro Zeile auf:

`exa --oneline`

- Liste alle Dateien auf, einschließlich versteckter Dateien:

`exa --all`

- Liste alle Dateien im langen Format auf (Berechtigungen, Eigentümer, Größe und Änderungsdatum):

`exa --long --all`

- Liste Dateien nach Größe absteigend sortiert auf:

`exa --reverse --sort=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size</span>

- Zeige Dateien in einer Baumstruktur an, die drei Ebenen tief ist:

`exa --long --tree --level=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- Liste Dateien nach Änderungsdatum aufsteigend sortiert auf:

`exa --long --sort=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modified</span>

- Liste Dateien inklusive Header, Icons und Git-Status:

`exa --long --header --icons --git`

- Liste keine Dateien auf, die in `.gitignore` erwähnt werden:

`exa --git-ignore`
