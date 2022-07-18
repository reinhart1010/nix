---
layout: page
title: osx/apachectl (português (Brasil))
description: "Interface de controle do Servidor HTTP Apache para macOS."
content_hash: 8975cea7d88b3c7762f3bbd7292204cb4b1c4f71
related_topics:
  - title: English version
    url: /en/osx/apachectl.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/apachectl.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/apachectl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/apachectl.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># apachectl

Interface de controle do Servidor HTTP Apache para macOS.
Mais informações: <https://www.unix.com/man-page/osx/8/apachectl/>.

- Iniciar o job launchd `org.apache.httpd`:

`apachectl start`

- Parar o job launchd:

`apachectl stop`

- Parar, e então iniciar o job launchd:

`apachectl restart`
