---
layout: page
title: common/topydo (français)
description: "Une application de liste de choses à faire qui utilise le format todo.txt."
content_hash: 88b78fbae79f88954461d4d1946b638fc7cd0c60
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/topydo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# topydo

Une application de liste de choses à faire qui utilise le format todo.txt.
Plus d'informations : <https://github.com/topydo/topydo>.

- Ajouter une tâche à un projet spécifique avec un contexte donné :

`topydo add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">todo_message</span>` +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">projet_nom</span>` @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">context_nom</span>`"`

- Ajouter une tâche à faire avec une date d'échéance de demain et une priorité de `A` :

`topydo add "(A) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">todo _message</span>` due:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1d</span>`"`

- Ajouter une tâche à faire dont la date d'échéance est le vendredi :

`topydo add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">todo_message</span>` due:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fri</span>`"`

- Ajouter une tâche répétitive non stricte (jour + récurrence) :

`topydo add "water flowers due:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mon</span>` rec:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1w</span>`"`

- Ajouter une tâche répétitive stricte (prochaine échéance = date + récurrence) :

`topydo add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">todo_message</span>` due:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2020-01-01</span>` rec:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+1m</span>`"`

- Revenir sur la dernière commande `topydo` exécutée :

`topydo revert`
