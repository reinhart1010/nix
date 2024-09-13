---
layout: page
title: common/http (Deutsch)
description: "HTTPie: ein benutzerfreundliches HTTP-Tool."
content_hash: 2add21fbd7a5ed61274a1d299103a6c580ae60f6
last_modified_at: 2024-09-13
related_topics:
  - title: English version
    url: /en/common/http.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/http.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/http.html
    icon: bi bi-globe
tldri18n_status: 2
---
# http

HTTPie: ein benutzerfreundliches HTTP-Tool.
Weitere Informationen: <https://httpie.io/docs/cli/usage>.

- Sende eine GET-Anfrage (Zeigt ddie Header und den Body der Antwort):

`http `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Zeige nur den angegebenen Teil der Anfrage und der Antwort (`H`: Header der Anfrage, `B`: Body der Anfrage, `h`: Header der Antwort, `b`: Body der Antwort, `m`: Metadaten der Antwort):

`http --print `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">H|B|h|b|m|Hh|Hhb|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Spezifiziere die zu nutzende HTTP-Methode und nutze den angegebenen Proxy:

`http `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GET|POST|HEAD|PUT|PATCH|DELETE|...</span>` --proxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http|https</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://localhost:8080|socks5://localhost:9050|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Folge `3xx`-Umleitungen und spezifiziere zusätzliche Header für die Anfrage:

`http `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-F|--follow</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'User-Agent: Mozilla/5.0' 'Accept-Encoding: gzip'</span>

- Authentisiere gegenüber einem Server mithilfe unterschiedlicher Anthentisierungsmethoden:

`http --auth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username:password|token</span>` --auth-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">basic|digest|bearer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GET|POST|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/auth</span>

- Erstelle eine Anfrage ohne diese zu senden (ähnlich zu dry-run):

`http --offline `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GET|DELETE|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Nutze die angegebene Session für persistente benutzerdefinierte Header, Credentials für die Authentisierung und Cookies:

`http --session `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">session_name|path/to/session.json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--auth username:password https://example.com/auth API-KEY:xxx</span>

- Lade eine Datei in ein Formular hoch (das folgende Beispiel geht davon aus, dass das Formularfeld als `<input type="file" name="cv" />` definiert ist):

`http --form `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">POST</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/upload</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cv@path/to/file</span>
