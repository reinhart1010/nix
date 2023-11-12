---
layout: page
title: windows/get-alias (Nederlands)
description: "Toon en verkrijg commando aliases in de huidige PowerShell sessie."
content_hash: 152b92c36439f33a7dce840b343b6b2374aadecc
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/get-alias.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/get-alias.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Get-Alias

Toon en verkrijg commando aliases in de huidige PowerShell sessie.
Dit commando kan alleen worden uitgevoerd onder PowerShell.
Meer informatie: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/get-alias>.

- Toon alle aliases in de huidige sessie:

`Get-Alias`

- Ontvang de aliased commando naam:

`Get-Alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando_alias</span>

- Toon alle aliases toegewezen aan een specifiek commando:

`Get-Alias -Definition `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>

- Toon aliases die beginnen met `abc`, maar sluit die uit die eindigen op`def`:

`Get-Alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">abc</span>`* -Exclude *`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">def</span>
