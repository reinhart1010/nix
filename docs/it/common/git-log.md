---
layout: page
title: common/git-log (italiano)
description: "Mostra la cronologia dei commit."
content_hash: d7a22e9a4c09ccaf3d62731ac5a035d33fe631eb
related_topics:
  - title: Deutsch version
    url: /de/common/git-log.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-log.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-log.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-log.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-log.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-log.html
    icon: bi bi-globe
---
# git log

Mostra la cronologia dei commit.
Maggiori informazioni: <https://git-scm.com/docs/git-log>.

- Mostra la sequenza dei commit del ramo del repository in uso, a partire dal commit corrente e andando in ordine cronologico inverso:

`git log`

- Mostra la cronologia di un dato file o directory, mostrando anche le modifiche:

`git log -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_o_directory</span>

- Offri una panoramica dei file che sono cambiati ad ogni commit:

`git log --stat`

- Mostra il grafo dei commit nel ramo corrente, includendo solo la prima riga di ogni messaggio di commit:

`git log --oneline --graph`

- Mostra il grafo di tutti i commit, tag e rami dell'intero repository:

`git log --oneline --decorate --all --graph`

- Mostra solo i commit il cui messaggio contiene una data stringa (ignorando maiuscole/minuscole):

`git log -i --grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stringa_da_cercare</span>

- Mostra gli ultimi N commit di un certo autore:

`git log -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero</span>` --author=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">autore</span>

- Mostra i commit effettuati tra due date (yyyy-mm-dd):

`git log --before="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2017-01-29</span>`" --after="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2017-01-17</span>`"`
