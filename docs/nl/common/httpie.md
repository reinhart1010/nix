---
layout: page
title: common/httpie (Nederlands)
description: "Een gebruiksvriendelijke HTTP-tool."
content_hash: 765ca0574c4f5e98eee75338484dc853cd81d01d
last_modified_at: 2024-08-22
related_topics:
  - title: Deutsch version
    url: /de/common/httpie.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/httpie.html
    icon: bi bi-globe
tldri18n_status: 2
---
# httpie

Een gebruiksvriendelijke HTTP-tool.
Meer informatie: <https://github.com/httpie/httpie>.

- Verstuur een GET-verzoek (standaardmethode zonder verzoekgegevens):

`http `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Verstuur een POST-verzoek (standaardmethode met verzoekgegevens):

`http `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hello=World</span>

- Verstuur een POST-verzoek met omgeleide invoer:

`http `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestand.json</span>

- Verstuur een PUT-verzoek met een opgegeven JSON-body:

`http PUT `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/todos/7</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hello=world</span>

- Verstuur een DELETE-verzoek met een opgegeven verzoekheader:

`http DELETE `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/todos/7</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">API-Key:foo</span>

- Toon de hele HTTP-uitwisseling (zowel verzoek als antwoord):

`http -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Download een bestand:

`http --download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Volg redirects en toon tussenliggende verzoeken en antwoorden:

`http --follow --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>
