---
layout: page
title: common/cradle-install (italiano)
description: "Installa i componenti del framework Cradle per PHP."
content_hash: 894bfa229c85e3440d0561b32c631ca5ff43bf5c
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/cradle-install.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cradle-install.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cradle-install.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cradle install

Installa i componenti del framework Cradle per PHP.
Maggiori informazioni: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#install>.

- Installa i componenti di Cradle (maggiori dettagli verranno richiesti all'utente):

`cradle install`

- Sovrascrivi i file forzatamente:

`cradle install --force`

- Salta l'esecuzione di migrazioni SQL:

`cradle install --skip-sql`

- Salta l'esecuzione di aggiornamenti dei pacchetti:

`cradle install --skip-versioning`

- Utilizza specifici dettagli per il database:

`cradle install -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_utente</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>
