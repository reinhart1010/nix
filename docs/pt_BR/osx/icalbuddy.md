---
layout: page
title: osx/icalbuddy (português (Brasil))
description: "Utilitário de linha de comando para exibir eventos e tarefas do banco de dados do calendário do macOS."
content_hash: 0662d8ad248ede91257ee22117fed373402d9759
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/icalbuddy.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/icalbuddy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# icalBuddy

Utilitário de linha de comando para exibir eventos e tarefas do banco de dados do calendário do macOS.
Mais informações: <https://hasseg.org/icalBuddy/>.

- Exibe eventos que acontecerão hoje:

`icalBuddy --includeOnlyEventsFromNowOn eventsToday`

- Exibe tarefas incompletas:

`icalBuddy uncompletedTasks`

- Exibe uma lista formatada separada por calendário para todos os eventos de hoje:

`icalBuddy --formatOutput --separateByCalendar eventsToday`

- Exibe tarefas para um determinado número de dias:

`icalBuddy --includeOnlyEventsFromNowOn "tasksDueBefore:today+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dias</span>`"`

- Exibe eventos em um intervalo de tempo:

`icalBuddy eventsFrom:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data_inicial</span>` to:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data_final</span>
