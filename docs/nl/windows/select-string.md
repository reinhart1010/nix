---
layout: page
title: windows/select-string (Nederlands)
description: "Vindt tekst in string en bestanden in PowerShell."
content_hash: 8b0c0756af64030d5422158634243af0cf5d607c
last_modified_at: 2023-11-23
related_topics:
  - title: English version
    url: /en/windows/select-string.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/select-string.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Select-String

Vindt tekst in string en bestanden in PowerShell.
Dit commando kan alleen gebruikt worden via PowerShell.
Je kan `Select-String` gebruiken zoals `grep` in UNIX of `findstr.exe` in Windows.
Meer informatie: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/select-string>.

- Zoek naar een patroon binnen een bestand:

`Select-String -Path "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand</span>`" -Pattern '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoek_patroon</span>`'`

- Zoek naar een exacte string (schakelt reguliere expressies uit):

`Select-String -SimpleMatch "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exacte_string</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand</span>

- Zoek naar een patroon in alle `.ext` bestanden in de huidige map:

`Select-String -Path "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>`" -Pattern '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoek_patroon</span>`'`

- Toon het opgegeven aantal regels voor en na de regel die overeenkomt met de patroon:

`Select-String --Context `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2,3</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoek_patroon</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand</span>

- Zoek in `stdin` voor regels die niet overeenkomen met een patroon:

`Get-Content `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand</span>` | Select-String --NotMatch "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoek_patroon</span>`"`
