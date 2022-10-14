---
layout: page
title: windows/curl (Deutsch)
description: "In PowerShell kann dieser Befehl ein Alias von `Invoke-WebRequest` sein, wenn das Originalprogramm `curl` (<https://curl.se>) nicht ordnungsgemäß installiert wurde."
content_hash: ec255c47f38f2e692d23dec301c929349fbb9388
related_topics:
  - title: English version
    url: /en/windows/curl.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/curl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/curl.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># curl

In PowerShell kann dieser Befehl ein Alias von `Invoke-WebRequest` sein, wenn das Originalprogramm `curl` (<https://curl.se>) nicht ordnungsgemäß installiert wurde.

- Überprüfen Sie, ob `curl` ordnungsgemäß installiert ist, indem Sie sich die Versionsnummer ausgeben lassen. Wenn nachfolgender Befehl einen Fehler ausgibt, hat PowerShell diesen Befehl möglicherweise durch `Invoke-WebRequest` ersetzt:

`curl --version`

- Schaue dir hier die Dokumentation für den ursprünglichen `curl`-Befehl an:

`tldr curl -p common`

- Schaue dir hier die Dokumentation für den PowerShell-Befehl `Invoke-WebRequest` an:

`tldr invoke-webrequest`
