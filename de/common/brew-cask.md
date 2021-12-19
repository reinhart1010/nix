---
layout: page
title: common/brew-cask (Deutsch)
description: "Paketmanager für macOS-Anwendungen, die als Binärdateien verteilt werden."
content_hash: d62aefaeb13d68b06fc17bebef94a17276e24ac4
related_topics:
  - title: English version
    url: /en/common/brew-cask.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/brew-cask.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/brew-cask.html
    icon: bi bi-globe
---
# brew cask

Paketmanager für macOS-Anwendungen, die als Binärdateien verteilt werden.
Weitere Informationen: <https://github.com/Homebrew/homebrew-cask>.

- Suche nach Formeln und Casks:

`brew search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>

- Installiere ein Cask:

`brew cask install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caskname</span>

- Liste alle installierten Casks auf:

`brew list --cask`

- Liste installierte Casks auf, für die neuere Versionen verfügbar sind:

`brew outdated --cask`

- Aktualisiere ein installiertes Cask (wenn kein Caskname angegeben wird, werden alle installierten Casks aktualisiert):

`brew upgrade --cask `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caskname</span>

- Deinstalliere ein Cask

`brew cask uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caskname</span>

- Deinstalliere ein Cask und entferne zugehörige Einstellungen und Dateien:

`brew upgrade --cask `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caskname</span>

- Zeige informationen zu einem bestimmten Cask an:

`brew cask uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caskname</span>
