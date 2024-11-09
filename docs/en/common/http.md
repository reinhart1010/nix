---
layout: page
title: common/http (English)
description: "HTTPie: an HTTP client designed for testing, debugging, and generally interacting with APIs and HTTP servers."
content_hash: 4d6cfb680fe7cecf7b29bc1c2033bd6645346976
last_modified_at: 2024-11-09
related_topics:
  - title: Deutsch version
    url: /de/common/http.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/http.html
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

HTTPie: an HTTP client designed for testing, debugging, and generally interacting with APIs and HTTP servers.
More information: <https://httpie.io/docs/cli/usage>.

- Make a simple GET request (shows response headers and content):

`http `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Print specific parts of the content (`H`: request headers, `B`: request body, `h`: response headers, `b`: response body, `m`: response metadata):

`http --print `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">H|B|h|b|m|Hh|Hhb|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Specify the HTTP method when sending a request and use a proxy to intercept the request:

`http `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GET|POST|HEAD|PUT|PATCH|DELETE|...</span>` --proxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http|https</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://localhost:8080|socks5://localhost:9050|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Follow any `3xx` redirects and specify additional headers in a request:

`http `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-F|--follow</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'User-Agent: Mozilla/5.0' 'Accept-Encoding: gzip'</span>

- Authenticate to a server using different authentication methods:

`http --auth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username:password|token</span>` --auth-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">basic|digest|bearer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GET|POST|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/auth</span>

- Construct a request but do not send it (similar to a dry-run):

`http --offline `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GET|DELETE|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Use named sessions for persistent custom headers, auth credentials and cookies:

`http --session `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">session_name|path/to/session.json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--auth username:password https://example.com/auth API-KEY:xxx</span>

- Upload a file to a form (the example below assumes that the form field is `<input type="file" name="cv" />`):

`http --form `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">POST</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/upload</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cv@path/to/file</span>
