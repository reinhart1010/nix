---
layout: page
title: common/borg (italiano)
description: "Strumento di backup con deduplicazione."
content_hash: 0a6e50ea1abf6fdccc221c81225c243451555768
related_topics:
  - title: Deutsch version
    url: /de/common/borg.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/borg.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/borg.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/borg.html
    icon: bi bi-globe
---
# borg

Strumento di backup con deduplicazione.
Crea backup locali o remoti che sono montabili come filesystem.
Maggiori informazioni: <https://borgbackup.readthedocs.io/en/stable/usage/general.html>.

- Inizializza una repository (locale):

`borg init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/percorso/a/repo_o_directory</span>

- Esegui il backup di una directory nella repository, creando un archivio chiamato "Lunedi":

`borg create --progress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/percorso/a/repo_o_directory</span>`::`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Lunedi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/percorso/a/directory_sorgente</span>

- Lista tutti gli archivi in una repository:

`borg list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/percorso/a/repo_o_directory</span>

- Estrai una specifica directory dall'archivio "Lunedi" in una repository remota, escludendo tutti i file `.ext`:

`borg extract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utente</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/percorso/a/repo_o_directory</span>`::`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Lunedi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/cartella_destinazione</span>` --exclude '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>`'`

- Riduci una repository eliminando tutti gli archivi più vecchi di 7 giorni, elencando i cambiamenti:

`borg prune --keep-within `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7d</span>` --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/percorso/a/repo_o_directory</span>

- Monta una repository come filesystem FUSE:

`borg mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/percorso/a/repo_o_directory</span>`::`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Lunedi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/percorso/a/mountpoint</span>

- Mostra aiuto sul come creare archivi:

`borg create --help`
