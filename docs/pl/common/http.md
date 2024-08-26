---
layout: page
title: common/http (polski)
description: "HTTPie: HTTP client, ma być łatwiejszy w użyciu niż cURL."
content_hash: bdcb59e5eb3316d787ddf51c9fda5548dec10645
last_modified_at: 2024-08-26
related_topics:
  - title: English version
    url: /en/common/http.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/http.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># http

HTTPie: HTTP client, ma być łatwiejszy w użyciu niż cURL.
Więcej informacji: <https://httpie.org>.

- Pobierz adres URL do pliku:

`http --download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">przyklad.org</span>

- Wyślij dane zakodowane w formularzu:

`http --form `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">przyklad.org</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa='bob'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zdjecie_profilowe@'bob.png'</span>

- Wyślij obiekt JSON:

`http `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">przyklad.org</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name='bob'</span>

- Określ metodę HTTP:

`http `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">przyklad.org</span>

- Dołącz dodatkowy nagłówek:

`http `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">przyklad.org</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">X-MyHeader:123</span>

- Podaj nazwę użytkownika i hasło do uwierzytelnienia serwera:

`http --auth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwauzytkownika:haslo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">przyklad.org</span>

- Określ surowe ciało żądania za pośrednictwem `stdin`:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dane.txt</span>` | http PUT `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">przyklad.org</span>
