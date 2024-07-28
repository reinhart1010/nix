---
layout: page
title: common/curl (English)
description: "Transfers data from or to a server."
content_hash: b3131d492fd0786a969ef15d37f9148d11e8fb8d
last_modified_at: 2024-07-28
related_topics:
  - title: Deutsch version
    url: /de/common/curl.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/curl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/curl.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/curl.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/curl.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/curl.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/curl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/curl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/curl.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/curl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# curl

Transfers data from or to a server.
Supports most protocols, including HTTP, HTTPS, FTP, SCP, etc.
More information: <https://curl.se/docs/manpage.html>.

- Make an HTTP GET request and dump the contents in `stdout`:

`curl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Make an HTTP GET request, fo[L]low any `3xx` redirects, and [D]ump the reply headers and contents to `stdout`:

`curl --location --dump-header - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Download a file, saving the [O]utput under the filename indicated by the URL:

`curl --remote-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/filename.zip</span>

- Send form-encoded [d]ata (POST request of type `application/x-www-form-urlencoded`). Use `--data @file_name` or `--data @'-'` to read from `stdin`:

`curl -X POST --data `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'name=bob'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/form</span>

- Send a request with an extra header, using a custom HTTP method and over a pro[x]y (such as BurpSuite), ignoring insecure self-signed certificates:

`curl -k --proxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://127.0.0.1:8080</span>` --header `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'Authorization: Bearer token'</span>` --request `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GET|PUT|POST|DELETE|PATCH|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Send data in JSON format, specifying the appropriate Content-Type [H]eader:

`curl --data `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'{"name":"bob"}'</span>` --header `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'Content-Type: application/json'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/users/1234</span>

- Pass client certificate and key for a resource, skipping certificate validation:

`curl --cert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">client.pem</span>` --key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key.pem</span>` --insecure `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Resolve a hostname to a custom IP address, with [v]erbose output (similar to editing the `/etc/hosts` file for custom DNS resolution):

`curl --verbose --resolve `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>
