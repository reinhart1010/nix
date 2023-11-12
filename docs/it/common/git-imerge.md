---
layout: page
title: common/git-imerge (italiano)
description: "Esegui un'unione (merge) o rebase tra due rami Git in modo incrementale."
content_hash: 438c18f5fd18b5fe5b840b98f46fe9a4e75840e2
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-imerge.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-imerge.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-imerge.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-imerge.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git-imerge

Esegui un'unione (merge) o rebase tra due rami Git in modo incrementale.
Eventuali conflitti tra i due rami sono tracciati in coppie di commit distinti, per semplificarne la risoluzione.
Maggiori informazioni: <https://github.com/mhagger/git-imerge>.

- Avvia un rebase usando imerge (dopo aver fatto checkout sul ramo da spostare):

`git imerge rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ramo_su_cui_eseguire_il_rebase</span>

- Avvia un'unione usando imerge (dopo aver fatto checkout sul ramo di destinazione):

`git imerge merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ramo_da_unire</span>

- Mostra con un diagramma ASCII lo stato di esecuzione dell'unione o rebase:

`git imerge diagram`

- Continua con l'operazione di imerge dopo aver risolto i conflitti (dopo aver aggiunto i file in conflitto con `git add`):

`git imerge continue --no-edit`

- Concludi l'operazione di imerge dopo aver risolto tutti i conflitti:

`git imerge finish`

- Interrompi l'operazione di imerge e ritorna al ramo precedente:

`git-imerge remove && git checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ramo_precedente</span>
