---
layout: page
title: common/todo (italiano)
description: "Un semplice gestore per i todo da linea di comando."
content_hash: 0c34a04385da3e0d09ba7c89d4983edea3ca49a5
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/todo.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/todo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# todo

Un semplice gestore per i todo da linea di comando.
Maggiori informazioni: <https://todoman.readthedocs.io>.

- Elenco dei task che possono essere inizializzati:

`todo list --startable`

- Aggiungere un nuovo task alla lista delle cose da fare per lavoro:

`todo new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cose_da_fare</span>` --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lavoro</span>

- Aggiungere una località ad un task con un dato ID:

`todo edit --location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_località</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- Mostrare i dettagli di un task:

`todo show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- Contrassegnare un task con un ID specifico come completato:

`todo done `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id1 task_id2 ...</span>

- Eliminare un task:

`todo delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- Eliminare un task completato e ripristinare gli ID dei task rimanenti:

`todo flush`
