---
layout: page
title: common/birdc (Deutsch)
description: "Bird remote control."
content_hash: 0b8b6dcef48c3db9128f34fc9ddc3803fa5a0dc9
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/birdc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# birdc

Bird remote control.
Kommandozeilenwerkzeug zum Abrufen von Informationen wie Routen von bird und zur Durchführung von Konfigurationen während der Laufzeit.
Weitere Informationen: <https://bird.network.cz/>.

- Öffne die remote control Konsole:

`birdc`

- Lade die Konfiguration neu, ohne Bird neu zu starten:

`birdc configure`

- Zeige den aktuellen Status von Bird an:

`birdc show status`

- Zeige alle konfigurierten Protokolle an:

`birdc show protocols`

- Zeige alle Details zu einem Protokoll an:

`birdc show protocols `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">upstream1</span>` all`

- Zeige alle Routen an, die eine bestimmte AS-Nummer enthalten:

`birdc "show route where bgp_path ~ [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4242120045</span>`]"`

- Zeige alle besten Routen an:

`birdc show route primary`

- Zeige alle Details zu allen Routen von einem bestimmten Präfix an:

`birdc show route for `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fd00:/8</span>` all`
