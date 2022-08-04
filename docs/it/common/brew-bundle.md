---
layout: page
title: common/brew-bundle (italiano)
description: "Bundler per Homebrew, Homebrew Cask e per il Mac App Store."
content_hash: 91516a2e783a8986dcf8653bbdc466e494dd3f77
related_topics:
  - title: Deutsch version
    url: /de/common/brew-bundle.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/brew-bundle.html
    icon: bi bi-globe
---
# brew bundle

Bundler per Homebrew, Homebrew Cask e per il Mac App Store.
Maggiori informazioni: <https://github.com/Homebrew/homebrew-bundle>.

- Installa un pacchetto da un Brewfile nel percorso corrente:

`brew bundle`

- Installa pacchetti da un Brewfile specifico in un percorso specifico:

`brew bundle --file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>

- Crea un Brewfile con tutti i pacchetti installati:

`brew bundle dump`

- Disinstalla tutti i pacchetti non specificati nel Brewfile:

`brew bundle cleanup --force`

- Controlla se c'è qualcosa da installare o da aggiornare nel Brewfile:

`brew bundle check`

- Mostra una lista di tutte le righe presenti nel Brewfile:

`brew bundle list --all`
