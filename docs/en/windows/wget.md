---
layout: page
title: windows/wget (English)
description: "In PowerShell, this command may be an alias of `Invoke-WebRequest` when the original `wget` program (<https://www.gnu.org/software/wget>) is not properly installed."
content_hash: 2d654e4f1982200ff6f9438286a510f9a2e60d61
last_modified_at: 2023-11-12
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
  - title: polski version
    url: /pl/windows/wget.html
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
tldri18n_status: 2
---
# wget

In PowerShell, this command may be an alias of `Invoke-WebRequest` when the original `wget` program (<https://www.gnu.org/software/wget>) is not properly installed.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- Check whether `wget` is properly installed by printing its version number. If this command evaluates into an error, PowerShell may have substituted this command with `Invoke-WebRequest`:

`wget --version`

- View documentation for the original `wget` command:

`tldr wget -p common`

- View documentation for the original `wget` command in older versions of `tldr` command-line client:

`tldr wget -o common`

- View documentation for PowerShell's `Invoke-WebRequest` command:

`tldr invoke-webrequest`
