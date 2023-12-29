---
layout: page
title: common/git-format-patch (italiano)
description: "Prepara file .patch. Utile per l'invio di commit via email."
content_hash: 36b53be33a2f2e36e10651fd3b065b8aafcba122
last_modified_at: 2023-12-29
related_topics:
  - title: English version
    url: /en/common/git-format-patch.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-format-patch.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-format-patch.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-format-patch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git format-patch

Prepara file .patch. Utile per l'invio di commit via email.
Vedi anche `git am`, che permette di applicare file .patch.
Maggiori informazioni: <https://git-scm.com/docs/git-format-patch>.

- Crea un file `.patch` (il nome è assegnato automaticamente) con i commit non ancora inviati al repository remoto:

`git format-patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origin</span>

- Scrivi su `stdout` un file `.patch` per l'intervallo di commit definito dai due commit dati:

`git format-patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_1</span>`..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_2</span>

- Scrivi un file `.patch` per gli ultimi 3 commit:

`git format-patch -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>
