---
layout: page
title: common/darkhttpd (English)
description: "Darkhttpd web server."
content_hash: 9e64ac5df540fb9ccc436e37aa25a42947cc2e8c
related_topics:
  - title: italiano version
    url: /it/common/darkhttpd.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/darkhttpd.html
    icon: bi bi-globe
---
# darkhttpd

Darkhttpd web server.
More information: <https://unix4lyfe.org/darkhttpd>.

- Start server serving the specified document root:

`darkhttpd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/docroot</span>

- Start server on specified port (port 8080 by default if running as non-root user):

`darkhttpd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/docroot</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Listen only on specified IP address (by default, the server listens on all interfaces):

`darkhttpd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/docroot</span>` --addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>
