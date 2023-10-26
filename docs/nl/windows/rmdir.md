---
layout: page
title: windows/rmdir (Nederlands)
description: "Verwijdert een map en zijn inhoud."
content_hash: 643dbc4a202f23a9d16307e9ea3cef7eec9361f4
last_modified_at: 2023-10-26
related_topics:
  - title: English version
    url: /en/windows/rmdir.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/rmdir.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/rmdir.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/rmdir.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/rmdir.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rmdir

Verwijdert een map en zijn inhoud.
In PowerShell is deze opdracht een alias van `Remove-Item`. Deze documentatie is gebaseerd op de Command Prompt (`cmd`) versie van `rmdir`.
Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/rmdir>.

- Bekijk documentatie van het equivalente PowerShell-commando:

`tldr remove-item`

- Verwijder een lege map:

`rmdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>

- Verwijder een map en zen inhoud recursief:

`rmdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>` /s`

- Verwijder een map en zen inhoud recursief zonder te vragen:

`rmdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>` /s /q`
