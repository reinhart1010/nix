---
layout: page
title: osx/launchctl (Nederlands)
description: "Beheer Apple's `launchd` manager voor launch daemons (systeembrede diensten) en launch agents (programma's per gebruiker)."
content_hash: 0f721247fd94b18a3934673a34b268efb0bcbfb9
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/launchctl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/launchctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# launchctl

Beheer Apple's `launchd` manager voor launch daemons (systeembrede diensten) en launch agents (programma's per gebruiker).
`launchd` laadt op XML gebaseerde `*.plist`-bestanden die op de juiste locaties zijn geplaatst, en voert de corresponderende commando's uit volgens hun gedefinieerde schema.
Meer informatie: <https://manned.org/launchctl>.

- Activeer een gebruikersspecifieke agent die in `launchd` moet worden geladen wanneer de gebruiker inlogt:

`launchctl load ~/Library/LaunchAgents/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_script</span>`.plist`

- Activeer een agent die root-rechten vereist om te kunnen werken en/of moet worden geladen wanneer een gebruiker inlogt (let op de afwezigheid van `~` in het pad):

`sudo launchctl load /Library/LaunchAgents/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">root_script</span>`.plist`

- Activeer een systeembrede daemon die moet worden geladen wanneer het systeem opstart (zelfs als er geen gebruiker inlogt):

`sudo launchctl load /Library/LaunchDaemons/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system_daemon</span>`.plist`

- Toon alle geladen agenten/daemons, met de PID als het proces dat ze specificeren momenteel actief is, en de afsluitcode de laatste keer dat ze werden uitgevoerd terugstuurde:

`launchctl list`

- Een momenteel geladen agent ontladen, b.v. om wijzigingen aan te brengen (let op: het plist-bestand wordt automatisch in `launchd` geladen na een herstart en/of inloggen):

`launchctl unload ~/Library/LaunchAgents/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_script</span>`.plist`

- Voer handmatig een bekende (geladen) agent/daemon uit, zelfs als dit niet het juiste moment is (opmerking: deze opdracht gebruikt het label van de agent, in plaats van de bestandsnaam):

`launchctl start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script_bestand</span>

- Beëindig handmatig het proces dat is gekoppeld aan een bekende agent/daemon, als deze actief is:

`launchctl stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script_bestand</span>
