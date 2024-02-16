---
layout: page
title: linux/pacman (italiano)
description: "Gestore pacchetti di Arch Linux."
content_hash: 9b0da902f9bace023a7c8467b30116ad23870127
last_modified_at: 2024-02-16
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/pacman.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacman.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/pacman.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/pacman.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/pacman.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman

Gestore pacchetti di Arch Linux.
Vedi anche: `pacman-database`, `pacman-deptest`, `pacman-files`, `pacman-key`, `pacman-mirrors`, `pacman-query`, `pacman-remove`, `pacman-sync`, `pacman-upgrade`.
Per comandi equivalenti in altri gestori pacchetti, vedi <https://wiki.archlinux.org/title/Pacman/Rosetta>.
Maggiori informazioni: <https://man.archlinux.org/man/pacman.8>.

- Sincronizza e aggiorna tutti i pacchetti:

`sudo pacman -Syu`

- Installa un nuovo pacchetto:

`sudo pacman -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_pacchetto</span>

- Rimuovi un pacchetto e le sue dipendenze:

`sudo pacman -Rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_pacchetto</span>

- Cerca nel database un pacchetto contenente uno specifico file:

`pacman -F "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_file</span>`"`

- Mostra i pacchetti installati e le versioni:

`pacman -Q`

- Mostra solo i pacchetti esplicitamente installati e le versioni:

`pacman -Qe`

- Mostra i pacchetti orfani (installati come dipendenze ma attualmente non richiesti da nessun altro pacchetto):

`pacman -Qtdq`

- Svuota l'intera cache di `pacman`:

`sudo pacman -Scc`
