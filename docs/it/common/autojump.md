---
layout: page
title: common/autojump (italiano)
description: "Salta velocemente tra le directory che usi più spesso."
content_hash: e8e745faa367ff95b2feb4c7d9749234c7282f49
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/autojump.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/autojump.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/autojump.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/autojump.html
    icon: bi bi-globe
tldri18n_status: 2
---
# autojump

Salta velocemente tra le directory che usi più spesso.
Alias come j o jc sono disponibili per una maggiore velocità di scrittura.
Maggiori informazioni: <https://github.com/wting/autojump>.

- Muoviti in una directory il cui nome contiene una parola chiave:

`j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parola_chiave</span>

- Salta in una sotto-directory della directory corrente il quale nome contiene una parola chiave:

`jc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parola_chiave</span>

- Apri una directory il cui nome contiene una parola chiave nel gestore file di sistema:

`jo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parola_chiave</span>

- Rimuovi directory non esistenti dal database di autojump:

`j --purge`

- Mostra le voci nel database di autojump:

`j -s`
