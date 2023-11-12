---
layout: page
title: common/browser-sync (italiano)
description: "Avvia un web-server locale che si aggiorna al cambiamento dei file."
content_hash: 7d1f1b31ca77556a6ffae067179314744a09fa83
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/browser-sync.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/browser-sync.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/browser-sync.html
    icon: bi bi-globe
tldri18n_status: 2
---
# browser-sync

Avvia un web-server locale che si aggiorna al cambiamento dei file.
Maggiori informazioni: <https://browsersync.io/docs/command-line>.

- Avvia un server da una specifica directory:

`browser-sync start --server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>` --files `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>

- Avvia un server da una directory locale, monitorando tutti i file CSS:

`browser-sync start --server --files '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory/*.css</span>`'`

- Crea un file di configurazione:

`browser-sync init`

- Avvia bower-sync da un file di configurazione:

`browser-sync start --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_di_configurazione</span>
