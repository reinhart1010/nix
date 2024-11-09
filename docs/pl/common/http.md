---
layout: page
title: common/http (polski)
description: "HTTPie: klient HTTP przeznaczony do testowania, debugowania i ogólnej interakcji z API i serwerami HTTP."
content_hash: 8ca8d6089ac31c0d7799d516ce2599fa940fda29
last_modified_at: 2024-11-09
related_topics:
  - title: Deutsch version
    url: /de/common/http.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/http.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/http.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/http.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># http

HTTPie: klient HTTP przeznaczony do testowania, debugowania i ogólnej interakcji z API i serwerami HTTP.
Więcej informacji: <https://httpie.io/docs/cli/usage>.

- Wykonaj proste żądanie GET (wyświetla nagłówki odpowiedzi i zawartość):

`http `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Wyświetl podane części treści (`H`: nagłówki żądania, `B`: treść żądania, `h`: nagłówki odpowiedzi, `b`: treść odpowiedzi, `m`: metadane odpowiedzi):

`http --print `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">H|B|h|b|m|Hh|Hhb|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Określ metodę HTTP używaną podczas wysyłania żądania i użyj serwera proxy do przechwycenia żądania:

`http `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GET|POST|HEAD|PUT|PATCH|DELETE|...</span>` --proxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http|https</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://localhost:8080|socks5://localhost:9050|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Podążaj za wszystkimi przekierowaniami `3xx` i określ dodatkowe nagłówki do żądania:

`http `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-F|--follow</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'User-Agent: Mozilla/5.0' 'Accept-Encoding: gzip'</span>

- Uwierzytelnij się na serwerze używając różnych metod uwierzytelniania:

`http --auth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_użytkownika:hasło|token</span>` --auth-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">basic|digest|bearer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GET|POST|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/auth</span>

- Skonstruuj żądanie, ale go nie wysyłaj:

`http --offline `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GET|DELETE|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Użyj nazwanych sesji do trwałych niestandardowych nagłówków, danych uwierzytelniających i ciasteczek:

`http --session `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_sesji|ścieżka/do/sesji.json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--auth nazwa_użytkownika:hasło https://example.com/auth API-KEY:xxx</span>

- Prześlij plik do formularza (poniższy przykład zakłada, że polem formularza jest `<input type="file" name="cv" />`):

`http --form `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">POST</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/upload</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cv@ścieżka/do/pliku</span>
