---
layout: page
title: common/hugo-server (English)
description: "Build and serve a site with Hugo's built-in webserver."
content_hash: 81f9745237f57e5d5fd472d277830f782c8396fb
last_modified_at: 2024-11-24
related_topics:
  - title: español version
    url: /es/common/hugo-server.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/hugo-server.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hugo server

Build and serve a site with Hugo's built-in webserver.
More information: <https://gohugo.io/commands/hugo_server/>.

- Build and serve a site:

`hugo server`

- Build and serve a site on a specified port number:

`hugo server --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_number</span>

- Build and serve a site while minifying supported output formats (HTML, XML, etc.):

`hugo server --minify`

- Build and serve a site in the production environment with full re-renders while minifying supported formats:

`hugo server --environment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">production</span>` --disableFastRender --minify`

- Display help:

`hugo server --help`
