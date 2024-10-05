---
layout: page
title: common/todo (português (Brasil))
description: "Um gerenciador de tarefas simples, de interface de linha de comando e em conformidade com os padrões."
content_hash: 4368a7b02150f5450272c94dfb0d4273a6d15dde
last_modified_at: 2024-10-05
related_topics:
  - title: English version
    url: /en/common/todo.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/todo.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/todo.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/todo.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/todo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# todo

Um gerenciador de tarefas simples, de interface de linha de comando e em conformidade com os padrões.
Mais informações: <https://todoman.readthedocs.io>.

- Lista tarefas iniciáveis:

`todo list --startable`

- Adiciona uma nova tarefa à lista de trabalho:

`todo new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">coisas_para_fazer</span>` --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">trabalho</span>

- Adiciona um local para uma tarefa com um ID provido:

`todo edit --location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_local</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_tarefa</span>

- Mostra detalhes sobre uma tarefa:

`todo show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_tarefa</span>

- Marca tarefas com os IDs especificados como concluídas:

`todo done `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_tarefa1 id_tarefa2 ...</span>

- Exclui uma tarefa:

`todo delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- Exclui tarefas concluídas e redefine os IDs das tarefas restantes:

`todo flush`
