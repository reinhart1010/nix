---
layout: page
title: common/crontab (Nederlands)
description: "Plan cron jobs zodat deze volgens een tijdsinterval voor de huidige gebruiker worden uitgevoerd."
content_hash: 37aada46bc25575f66a99391623141226c1042a2
last_modified_at: 2023-11-27
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
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/crontab.html
    icon: bi bi-globe
tldri18n_status: 2
---
# crontab

Plan cron jobs zodat deze volgens een tijdsinterval voor de huidige gebruiker worden uitgevoerd.
Meer informatie: <https://crontab.guru/>.

- Pas het crontab bestand aan voor de huidige gebruiker:

`crontab -e`

- Pas het crontab bestand aan voor een specifieke gebruiker:

`sudo crontab -e -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruiker</span>

- Vervang de huidige crontab met de inhoud van een opgegeven bestand:

`crontab `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Bekijk een lijst van bestaande cron jobs voor de huidige gebruiker:

`crontab -l`

- Verwijder alle cron jobs voor de huidige gebruiker:

`crontab -r`

- Voorbeeld crontab entry, welke iedere dag om 10:00 draait (* betekent elke waarde):

`0 10 * * * `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando_om_uit_te_voeren</span>

- Voorbeeld crontab entry, welke iedere 10 minuten een commando uitvoert:

`*/10 * * * * `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando_om_uit_te_voeren</span>

- Voorbeeld crontab entry, welke iedere vrijdag om 02:30 een specifiek script draait:

`30 2 * * Fri `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/absoluut/pad/naar/script.sh</span>
