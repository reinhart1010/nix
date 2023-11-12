---
layout: page
title: common/git-push (italiano)
description: "Invia i commit ad un repository remoto."
content_hash: a49861fcd900a77bff45d22ed655ac3c15c7f107
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-push.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-push.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-push.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-push.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-push.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-push.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-push.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git push

Invia i commit ad un repository remoto.
Maggiori informazioni: <https://git-scm.com/docs/git-push>.

- Invia le modifiche fatte nel ramo corrente locale al corrispondente ramo remoto:

`git push`

- Invia le modifiche fatte in uno specifico ramo locale al corrispondente ramo remoto:

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_repository_remoto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo</span>

- Invia le modifiche fatte in uno specifico ramo locale al corrispondente ramo remoto ed imposta il ramo remoto come destinazione di default per i push/pull del ramo locale:

`git push -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_repository_remoto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo</span>

- Invia le modifiche fatte in uno specifico ramo locale ad uno specifico ramo remoto:

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_repository_remoto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo_remoto</span>

- Invia le modifiche fatte in ogni ramo locale ai corrispondenti rami remoti in uno specifico repository remoto:

`git push --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_repository_remoto</span>

- Cancella un ramo di un repository remoto:

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_repository_remoto</span>` --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo_remoto</span>

- Cancella i rami remoti che non hanno un ramo locale corrispondente:

`git push --prune `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_repository_remoto</span>

- Pubblica i tag che non sono già presenti nel repository remoto:

`git push --tags`
