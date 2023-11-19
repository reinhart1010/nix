---
layout: page
title: windows/curl (Nederlands)
description: "In PowerShell kan dit commando een alias zijn van `Invoke-WebRequest` als het originele `curl` programma (<https://curl.se/>) niet correct is geïnstalleerd."
content_hash: 3a00ccd21062ce5997badec5ebdfce414cb44c4e
last_modified_at: 2023-11-19
related_topics:
  - title: العربية version
    url: /ar/windows/curl.html
    icon: bi bi-globe
  - title: বাংলা version
    url: /bn/windows/curl.html
    icon: bi bi-globe
  - title: bosanski version
    url: /bs/windows/curl.html
    icon: bi bi-globe
  - title: català version
    url: /ca/windows/curl.html
    icon: bi bi-globe
  - title: dansk version
    url: /da/windows/curl.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/windows/curl.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/curl.html
    icon: bi bi-globe
  - title: español version
    url: /es/windows/curl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/windows/curl.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/curl.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/curl.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/curl.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/curl.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/curl.html
    icon: bi bi-globe
  - title: ລາວ version
    url: /lo/windows/curl.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/windows/curl.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/windows/curl.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/windows/curl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/curl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/curl.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/windows/curl.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/curl.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/windows/curl.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/curl.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/windows/curl.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/windows/curl.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/windows/curl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/curl.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/curl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# curl

In PowerShell kan dit commando een alias zijn van `Invoke-WebRequest` als het originele `curl` programma (<https://curl.se/>) niet correct is geïnstalleerd.
Meer informatie: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- Controleer of `curl` correct is geïnstalleerd door het versienummer te printen. Als dit commando resulteert in een error, heeft PowerShell dit commando mogelijk vervangen met `Invoke-WebRequest`:

`curl --version`

- Bekijk de documentatie van het originele `curl` commando:

`tldr curl -p common`

- Bekijk de documentatie van het PowerShell's `Invoke-WebRequest` commando:

`tldr invoke-webrequest`
