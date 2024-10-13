---
layout: page
title: common/git-rebase (italiano)
description: "Applica i commit di un ramo su un ramo differente."
content_hash: e28c0d6900a0348747f6824121a2e469eb6a7359
last_modified_at: 2024-10-13
related_topics:
  - title: Deutsch version
    url: /de/common/git-rebase.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-rebase.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-rebase.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-rebase.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-rebase.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-rebase.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-rebase.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-rebase.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-rebase.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git rebase

Applica i commit di un ramo su un ramo differente.
Tipicamente usato per riallineare (rebase) due rami, creando copie dei commit nella nuova posizione.
Maggiori informazioni: <https://git-scm.com/docs/git-rebase>.

- Riallinea il ramo corrente con il ramo specificato:

`git rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ramo_della_nuova_base</span>

- Avvia un rebase interattivo, che consente di riordinare, omettere, unire o modificare i commit:

`git rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--interactive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo_o_commit_hash</span>

- Prosegui con un rebase che era stato sospeso da un errore di unione, dopo aver risolto i conflitti:

`git rebase --continue`

- Prosegui con un rebase che era stato sospeso da conflitti di unione, ignorando i commit in conflitto:

`git rebase --skip`

- Interrompi un rebase in corso (ad esempio perché interrotto da un conflitto di unione):

`git rebase --abort`

- Sposta parti del ramo corrente su una base differente, specificando la vecchia base di partenza:

`git rebase --onto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nuova_base</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vecchia_base</span>

- Applica gli ultimi 5 commit locali, consentendo di riordinarli, ometterli, unirli o modificarli:

`git rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--interactive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD~5</span>

- Risolvi automaticamente i conflitti a favore del ramo di versione corrente (la parola chiave `theirs` ha qui un significato opposto):

`git rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-X|--strategy-option</span>` theirs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo</span>
