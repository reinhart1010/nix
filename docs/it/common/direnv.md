---
layout: page
title: common/direnv (italiano)
description: "Estensione della shell per aggiungere o rimuovere variabili d'ambiente in base alla directory corrente."
content_hash: a1927c89f4fe8a2afb31d9c1c92d62e89802cb45
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/direnv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# direnv

Estensione della shell per aggiungere o rimuovere variabili d'ambiente in base alla directory corrente.
Maggiori informazioni: <https://github.com/direnv/direnv>.

- Permette il caricamento del `.envrc` presente nella directory corrente:

`direnv allow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>

- Revoca il permesso del `.envrc` presente nella directory corrente:

`direnv deny `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>

- Permette la modifica del `.envrc` nell'editor di testo predefinito, in seguito ricarica l'ambiente:

`direnv edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>

- Ricarica l'ambiente corrente:

`direnv reload`

- Mostra delle informazioni di debug:

`direnv status`
