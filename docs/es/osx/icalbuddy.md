---
layout: page
title: osx/icalbuddy (español)
description: "Utilidad de línea de comandos para imprimir eventos y tareas desde la base de datos del calendario de macOS."
content_hash: 4e748111d2f3c0a8d68278decec03df448086b43
last_modified_at: 2023-11-12
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

- Mostrar los eventos de hoy más tarde:

`icalBuddy -n eventsToday`

- Mostrar tareas no completadas:

`icalBuddy uncompletedTasks`

- Mostrar una lista formateada y discriminada de acuerdo al calendario de todos los eventos en el día de hoy:

`icalBuddy -f -sc eventsToday`

- Mostrar las tareas para un número determinado de días:

`icalBuddy -n "tasksDueBefore:today+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">days</span>`"`

- Mostrar los eventos en un rango de tiempo:

`icalBuddy eventsFrom:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start_date</span>` to:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">end_date</span>
