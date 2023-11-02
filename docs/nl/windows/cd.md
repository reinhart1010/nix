---
layout: page
title: windows/cd (Nederlands)
description: "Geef de naam van de huidige werkmap weer of wijzig deze."
content_hash: e1c3bc9d8709c562c37bc2e8d1d1fe1966479355
last_modified_at: 2023-11-02
related_topics:
  - title: বাংলা version
    url: /bn/windows/cd.html
    icon: bi bi-globe
  - title: čeština version
    url: /cs/windows/cd.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/windows/cd.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/cd.html
    icon: bi bi-globe
  - title: español version
    url: /es/windows/cd.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/cd.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/cd.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/cd.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/cd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/cd.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/cd.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/cd.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/windows/cd.html
    icon: bi bi-globe
---
# cd

Geef de naam van de huidige werkmap weer of wijzig deze.
In PowerShell is deze opdracht een alias van `Set-Location`. Deze documentatie is gebaseerd op de Command Prompt (`cmd`) versie van `cd`.
Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/cd>.

- Bekijk documentatie van het equivalente PowerShell-commando:

`tldr set-location`

- Geef de naam van de huidige map weer:

`cd`

- Ga naar een map in dezelfde drive:

`cd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\map</span>

- Ga naar een map in een andere drive:

`cd /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\map</span>

- Ga naar de bovenliggende map van de huidige map:

`cd ..`

- Ga naar de thuismap van de huidige gebruiker:

`cd %userprofile%`

- Ga naar de hoofdmap:

`cd \`
