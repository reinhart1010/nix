---
layout: page
title: common/calibre-server (English)
description: "A server application to distribute e-books over a network."
content_hash: 8bf7b39a2df2d0c25e5d08d673e238f11083c8a7
last_modified_at: 2024-02-15
related_topics:
  - title: italiano version
    url: /it/common/calibre-server.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/calibre-server.html
    icon: bi bi-globe
tldri18n_status: 2
---
# calibre-server

A server application to distribute e-books over a network.
Note: e-books must already be imported into the library using the GUI or the `calibredb` CLI.
More information: <https://manual.calibre-ebook.com/generated/en/calibre-server.html>.

- Start a server to distribute e-books. Access at <http://localhost:8080>:

`calibre-server`

- Start server on different port. Access at <http://localhost:port>:

`calibre-server --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Password protect the server:

`calibre-server --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>
