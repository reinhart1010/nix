---
layout: page
title: common/direnv (italiano)
description: "Estensione della shell per aggiungere o rimuovere variabili d'ambiente in base alla cartella corrente."
content_hash: 6c1058952d0cec3e5327ba61d1f859676da24037
related_topics:
  - title: English version
    url: /en/common/direnv.html
    icon: bi bi-globe
---
# direnv

Estensione della shell per aggiungere o rimuovere variabili d'ambiente in base alla cartella corrente.
Maggiori informazioni: <https://github.com/direnv/direnv>.

- Permette il caricamento del `.envrc` presente nella cartella corrente:

`direnv allow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>

- Revoca il permesso del `.envrc` presente nella cartella corrente:

`direnv deny `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>

- Permette la modifica del `.envrc` nell'editor di testo predefinito, in seguito ricarica l'ambiente:

`direnv edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>

- Ricarica l'ambiente corrente:

`direnv reload`

- Mostra delle informazioni di debug:

`direnv status`
