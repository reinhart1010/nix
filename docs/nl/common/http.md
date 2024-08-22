---
layout: page
title: common/http (Nederlands)
description: "HTTPie: HTTP client, bedoeld om gebruiksvriendelijker te zijn dan cURL."
content_hash: 8d1fe50f35ac95a67fa10bf50590e58e9d83b7cb
last_modified_at: 2024-08-22
related_topics:
  - title: English version
    url: /en/common/http.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/http.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/http.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># http

HTTPie: HTTP client, bedoeld om gebruiksvriendelijker te zijn dan cURL.
Meer informatie: <https://httpie.org>.

- Download een URL naar een bestand:

`http --download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.org</span>

- Verstuur formulier-gecodeerde data:

`http --form `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.org</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">naam='bob'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profielfoto@'bob.png'</span>

- Verstuur een JSON-object:

`http `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.org</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">naam='bob'</span>

- Specificeer een HTTP-methode:

`http `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.org</span>

- Voeg een extra header toe:

`http `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.org</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">X-MyHeader:123</span>

- Geef een gebruikersnaam en wachtwoord op voor serverauthenticatie:

`http --auth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam:wachtwoord</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.org</span>

- Specificeer de onbewerkte request body via `stdin`:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.txt</span>` | http PUT `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.org</span>
