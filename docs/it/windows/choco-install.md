---
layout: page
title: windows/choco-install (italiano)
description: "Installa uno o più pacchetti con Chocolatey."
content_hash: 48cb6ae910d43952cda66000793593ac81ff1141
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-install.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-install.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/choco-install.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-install.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-install.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-install.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-install.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco install

Installa uno o più pacchetti con Chocolatey.
Maggiori informazioni: <https://chocolatey.org/docs/commands-install>.

- Installa uno o più pacchetti separati da spazio:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacchetto1 pacchetto2 ...</span>

- Installa pacchetti da un file di configurazione personalizzato:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso\del\file_di_pacchetti.config</span>

- Installa un file nuspec o nupkg specifico:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso\del\file</span>

- Installa una nuova versione specifica di un pacchetto:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacchetto</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versione</span>

- Consenti l'installazione di più versioni di un pacchetto:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacchetto</span>` --allow-multiple`

- Conferma automaticamente tutte le richieste:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacchetto</span>` --yes`

- Specifica una fonte personalizzata per ricevere pacchetti:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacchetto</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_fonte|alias</span>

- Fornisci un nome utente e una password per l'autenticazione:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacchetto</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_utente</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>
