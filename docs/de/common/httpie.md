---
layout: page
title: common/httpie (Deutsch)
description: "Ein benutzerfreundliches HTTP-Tool."
content_hash: 0071d4a3354cb475852ffd4b16d1ff27a41cf8ec
last_modified_at: 2023-10-19
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># HTTPie

Ein benutzerfreundliches HTTP-Tool.
Weitere Informationen: <https://github.com/httpie/httpie>.

- Sende eine GET-Anfrage (Standardmethode ohne Anfragedaten):

`http `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Sende eine POST-Anfrage (Standardmethode mit Anfragedaten):

`http `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hello=World</span>

- Sende eine POST-Anfrage mit einer Datei als Eingabe:

`http `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.json</span>

- Sende eine PUT-Anfrage mit einem bestimmten JSON-Body:

`http PUT `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/todos/7</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hello=world</span>

- Sende eine DELETE-Anfrage mit einem bestimmten Anfrage-Header:

`http DELETE `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/todos/7</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">API-Key:foo</span>

- Zeige den gesamten HTTP-Austausch (sowohl Anfrage als auch Antwort):

`http -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Lade eine Datei herunter:

`http --download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Folge Umleitungen und zeige Zwischenanfragen und -antworten:

`http --follow --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>
