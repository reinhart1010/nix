---
layout: page
title: common/crontab (português (Brasil))
description: "Agenda tarefas cron para serem executadas em um intervalo de tempo para o usuário atual."
content_hash: 95d57ef66d0192723718e8169ac81aa468cae61d
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/crontab.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/crontab.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/crontab.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/crontab.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/crontab.html
    icon: bi bi-globe
tldri18n_status: 2
---
# crontab

Agenda tarefas cron para serem executadas em um intervalo de tempo para o usuário atual.
Mais informações: <https://crontab.guru/>.

- Edita o arquivo crontab para o usuário atual:

`crontab -e`

- Edita o arquivo crontab para um usuário específico:

`sudo crontab -e -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuário</span>

- Substitui o crontab atual pelo conteúdo do arquivo fornecido:

`crontab `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Exibe uma lista de tarefas cron existentes para o usuário atual:

`crontab -l`

- Remove todos as tarefas de cron do usuário atual:

`crontab -r`

- Exemplo de tarefa executada às 10:00 todos os dias (* significa qualquer valor):

`0 10 * * * `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando_para_executar</span>

- Exemplo de entrada do crontab, que executa um comando a cada 10 minutos:

`*/10 * * * * `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando_para_executar</span>

- Exemplo de entrada do crontab, que executa um determinado script às 02:30 todas as sextas-feiras:

`30 2 * * Fri `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/caminho/absoluto/para/script.sh</span>
