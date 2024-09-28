---
layout: page
title: windows/wget (polski)
description: "W PowerShell to polecenie może być aliasem `Invoke-WebRequest`, gdy oryginalny program `wget` (<https://www.gnu.org/software/wget>) nie jest poprawnie zainstalowany."
content_hash: c14e7574fbe5820a48873c1c67fa939f9fd95460
last_modified_at: 2024-09-28
related_topics:
  - title: العربية version
    url: /ar/windows/wget.html
    icon: bi bi-globe
  - title: bosanski version
    url: /bs/windows/wget.html
    icon: bi bi-globe
  - title: català version
    url: /ca/windows/wget.html
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
  - title: Nederlands version
    url: /nl/windows/wget.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/windows/wget.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/wget.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/windows/wget.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/wget.html
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
  - title: 中文 version
    url: /zh/windows/wget.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/wget.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># wget

W PowerShell to polecenie może być aliasem `Invoke-WebRequest`, gdy oryginalny program `wget` (<https://www.gnu.org/software/wget>) nie jest poprawnie zainstalowany.
Więcej informacji: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- Zobacz dokumentację oryginalnego polecenia `wget`:

`tldr wget -p common`

- Zobacz dokumentację polecenia PowerShell `Invoke-WebRequest`:

`tldr invoke-webrequest`

- Zweryfikuj, czy `wget` jest poprawnie zainstalowany poprzez sprawdzenie jego wersji. Jeśli to polecenie zwraca błąd, PowerShell mógł je zastąpić poleceniem `Invoke-WebRequest`:

`wget --version`
