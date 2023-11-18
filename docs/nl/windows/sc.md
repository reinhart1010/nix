---
layout: page
title: windows/sc (Nederlands)
description: "Communiceer met de Service Control Manager en services."
content_hash: 304cb73a97dec0522aee12543d88eb55ff398952
last_modified_at: 2023-11-18
related_topics:
  - title: English version
    url: /en/windows/sc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/sc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sc

Communiceer met de Service Control Manager en services.
Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/sc-query>.

- Toon de status van een service (geen service naam zal alle services tonen):

`sc.exe query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_naam</span>

- Start een service asynchroon:

`sc.exe create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_naam</span>` binpath= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\service_binary_bestand</span>

- Stop een service asynchroon:

`sc.exe delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_naam</span>

- Zet het type van een service:

`sc.exe config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_naam</span>` type= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_type</span>
