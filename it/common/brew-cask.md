---
layout: page
title: common/brew-cask (italiano)
description: "Gestore di pacchetti per applicazioni macOS distribuite sotto forma di file binari."
content_hash: b46e5931b633bb949007d1378dc6b56011fbb8d7
related_topics:
  - title: Deutsch version
    url: /de/common/brew-cask.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/brew-cask.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/brew-cask.html
    icon: bi bi-globe
---
# brew cask

Gestore di pacchetti per applicazioni macOS distribuite sotto forma di file binari.
Maggiori informazioni: <https://github.com/Homebrew/homebrew-cask>.

- Cerca formule e cask:

`brew search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">testo</span>

- Installa un cask:

`brew cask install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_del_cask</span>

- Elenca tutti i cask installati:

`brew cask list`

- Elenca i cask installati con versioni più nuove disponibili:

`brew cask outdated`

- Aggiorna un cask installato (se non viene fornito il nome di nessun cask, tutti i cask saranno aggiornati):

`brew cask upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_del_cask</span>

- Disinstalla un cask:

`brew cask uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_del_cask</span>

- Disinstalla un cask e rimuovi i relativi file e impostazioni:

`brew cask zap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_del_cask</span>

- Mostra informazioni su uno specifico cask:

`brew cask info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_del_cask</span>
