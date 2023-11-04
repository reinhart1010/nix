---
layout: page
title: windows/wget (Nederlands)
description: "In PowerShell kan dit commando een alias zijn van `Invoke-WebRequest` als het originele `wget` programma (<https://www.gnu.org/software/wget>) niet correct is geïnstalleerd."
content_hash: f5ebca71b6f0025730ba6013ce7b61781042b197
last_modified_at: 2023-11-04
related_topics:
  - title: العربية version
    url: /ar/windows/wget.html
    icon: bi bi-globe
  - title: বাংলা version
    url: /bn/windows/wget.html
    icon: bi bi-globe
  - title: bosanski version
    url: /bs/windows/wget.html
    icon: bi bi-globe
  - title: català version
    url: /ca/windows/wget.html
    icon: bi bi-globe
  - title: čeština version
    url: /cs/windows/wget.html
    icon: bi bi-globe
  - title: dansk version
    url: /da/windows/wget.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/windows/wget.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/wget.html
    icon: bi bi-globe
  - title: español version
    url: /es/windows/wget.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/windows/wget.html
    icon: bi bi-globe
  - title: suomi version
    url: /fi/windows/wget.html
    icon: bi bi-globe
  - title: français version
    url: /fr/windows/wget.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/wget.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/wget.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/wget.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/wget.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/wget.html
    icon: bi bi-globe
  - title: ລາວ version
    url: /lo/windows/wget.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/windows/wget.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/windows/wget.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/windows/wget.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/wget.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/wget.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/windows/wget.html
    icon: bi bi-globe
  - title: română version
    url: /ro/windows/wget.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/wget.html
    icon: bi bi-globe
  - title: српски version
    url: /sr/windows/wget.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/windows/wget.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/wget.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/windows/wget.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/windows/wget.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/windows/wget.html
    icon: bi bi-globe
  - title: o‘zbek version
    url: /uz/windows/wget.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/wget.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/wget.html
    icon: bi bi-globe
---
# wget

In PowerShell kan dit commando een alias zijn van `Invoke-WebRequest` als het originele `wget` programma (<https://www.gnu.org/software/wget>) niet correct is geïnstalleerd.

- Controleer of `wget` correct is geïnstalleerd door het versienummer te printen. Als dit commando resulteert in een error, heeft PowerShell dit commando mogelijk vervangen met `Invoke-WebRequest`:

`wget --version`

- Bekijk de documentatie van het originele `wget` commando:

`tldr wget -p common`

- Bekijk de documentatie van het originele `wget` commando in een oudere versie van de `tldr` command-line client:

`tldr wget -o common`

- Bekijk de documentatie van het PowerShell's `Invoke-WebRequest` commando:

`tldr invoke-webrequest`
