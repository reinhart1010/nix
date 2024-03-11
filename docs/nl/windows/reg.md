---
layout: page
title: windows/reg (Nederlands)
description: "Beheer sleutels en de waardes in een Windows registry."
content_hash: 467b345a19cecf8aabebb27e5e2760a8209ba4a3
last_modified_at: 2024-03-11
related_topics:
  - title: English version
    url: /en/windows/reg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/reg.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/reg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># reg

Beheer sleutels en de waardes in een Windows registry.
Sommige subcommando's zoals `reg add` hebben hun eigen documentatie.
Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg>.

- Voer een registry commando uit:

`reg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>

- Bekijk de documentatie voor het toevoegen en kopiëren van subsleutels:

`tldr reg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">add|copy</span>

- Bekijk de documentatie voor het verwijderen van sleutels en subsleutels:

`tldr reg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">delete|unload</span>

- Bekijk de documentatie voor het zoeken, bekijken en vergelijken van sleutels:

`tldr reg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">compare|flags|query</span>

- Bekijk de documentatie voor het exporteren en importeren van registry sleutels zonder de eigenaar en ACLs te bewaren:

`tldr reg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">export|import</span>

- Bekijk de documentatie voor het opslaan, herstellen en het lossen van sleutels met behoud van de eigenaar en ACLs:

`tldr reg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">save|restore|load|unload</span>

- Toon de help:

`reg /?`

- Toon de help voor een specifiek commando:

`reg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` /?`
