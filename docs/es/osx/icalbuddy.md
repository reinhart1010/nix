---
layout: page
title: osx/icalbuddy (español)
description: "Utilidad de línea de comandos para imprimir eventos y tareas desde la base de datos del calendario de macOS."
content_hash: e337db17b7a13fed0b38efdd72e53128460e1e59
last_modified_at: 2024-01-02
related_topics:
  - title: English version
    url: /en/osx/icalbuddy.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/icalbuddy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# icalBuddy

Utilidad de línea de comandos para imprimir eventos y tareas desde la base de datos del calendario de macOS.
Más información: <https://hasseg.org/icalBuddy/>.

- Muestra los eventos de hoy más tarde:

`icalBuddy --includeOnlyEventsFromNowOn eventsToday`

- Muestra tareas no completadas:

`icalBuddy uncompletedTasks`

- Muestra una lista formateada y discriminada de acuerdo al calendario de todos los eventos en el día de hoy:

`icalBuddy --formatOutput --separateByCalendar eventsToday`

- Muestra las tareas para un número determinado de días:

`icalBuddy --includeOnlyEventsFromNowOn "tasksDueBefore:today+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">days</span>`"`

- Muestra los eventos en un rango de tiempo:

`icalBuddy eventsFrom:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start_date</span>` to:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">end_date</span>
