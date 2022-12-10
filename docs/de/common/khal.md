---
layout: page
title: common/khal (Deutsch)
description: "Eine textbasierte Kalender- und Planungsanwendung für die Kommandozeile."
content_hash: 53cf37f48b3719acee2dfb3aea26a7069b05727a
last_modified_at: 2022-12-10
related_topics:
  - title: English version
    url: /en/common/khal.html
    icon: bi bi-globe
---
# khal

Eine textbasierte Kalender- und Planungsanwendung für die Kommandozeile.
Weitere Informationen: <https://lostpackets.de/khal>.

- Starte khal im interaktiven Modus:

`ikhal`

- Gib alle Termine aus, die im Kalender "privat" in den nächsten sieben Tagen geplant sind:

`khal list -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">privat</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">today</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7d</span>

- Gib alle Termine aus, die in Kalendern außer "privat" für morgen um 10 Uhr geplant sind:

`khal at -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">privat</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tomorrow</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10:00</span>

- Gib einen Kalender mit einer Liste an Terminen für die nächsten drei Monate aus:

`khal calendar`

- Füge dem Kalender "privat" einen neuen Termin hinzu:

`khal new -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">privat</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2020-09-08</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">18:00</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">18:30</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Zahnarzttermin</span>`"`
