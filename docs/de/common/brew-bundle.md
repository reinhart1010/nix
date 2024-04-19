---
layout: page
title: common/brew-bundle (Deutsch)
description: "Bundler für Homebrew, Homebrew Cask und den Mac App Store."
content_hash: c86ea7e11101bfc0ad0267fead06a49b97b54943
last_modified_at: 2024-04-19
related_topics:
  - title: English version
    url: /en/common/brew-bundle.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/brew-bundle.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/brew-bundle.html
    icon: bi bi-globe
tldri18n_status: 2
---
# brew bundle

Bundler für Homebrew, Homebrew Cask und den Mac App Store.
Weitere Informationen: <https://github.com/Homebrew/homebrew-bundle>.

- Installiere Pakete aus einer Brewfile im aktuellen Pfad:

`brew bundle`

- Installiere Pakete aus einer bestimmten Brewfile:

`brew bundle --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/brewfile</span>

- Gib eine Liste mit allen installierten Paketen aus:

`brew bundle dump`

- Deinstalliere Pakete, die nicht in der Brewfile aufgelistet sind:

`brew bundle cleanup --force`

- Prüfe, ob von einem Paket die aktuellste Version installiert ist:

`brew bundle check`

- Zeige alle Pakete, die in der Brewfile aufgelistet sind:

`brew bundle list --all`
