---
layout: page
title: common/brew (italiano)
description: "Gestore di pacchetti per macOS."
content_hash: 3bfa220639bd6fa660ed4af95ee4f991be36a5a4
related_topics:
  - title: English version
    url: /en/common/brew.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/brew.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/brew.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/brew.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/brew.html
    icon: bi bi-globe
---
# brew

Gestore di pacchetti per macOS.
Maggiori informazioni: <https://brew.sh>.

- Cerca formule e cask:

`brew search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">testo</span>

- Installa l'ultima versione stabile di una formula (usa `--devel` per le versioni in sviluppo):

`brew install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula</span>

- Mostra tutte le formule installate:

`brew list`

- Mostra le formule installate che non sono dipendenze di un'altra formula installata:

`brew leaves`

- Aggiorna una formula installata (se non viene fornito il nome di nessuna formula, tutte le formule installate verranno aggiornate):

`brew upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula</span>

- Trova la versione più aggiornata di Homebrew e di tutte le formule da GitHub:

`brew update`

- Mostra le informazioni su una specifica formula (versione, percorso di installazione, dipendenze, ecc...):

`brew info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula</span>

- Verifica se la versione installata di Homebrew presenta dei problemi:

`brew doctor`
