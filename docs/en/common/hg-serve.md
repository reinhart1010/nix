---
layout: page
title: common/hg-serve (English)
description: "Start a standalone Mercurial web server for browsing repositories."
content_hash: 3af36928ac798528ac9ec6312e0fd7c837a8f9d2
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# hg serve

Start a standalone Mercurial web server for browsing repositories.
More information: <https://www.mercurial-scm.org/doc/hg.1.html#serve>.

- Start a web server instance:

`hg serve`

- Start a web server instance on the specified port:

`hg serve --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Start a web server instance on the specified listening address:

`hg serve --address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address</span>

- Start a web server instance with a specific identifier:

`hg serve --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Start a web server instance using the specified theme (see the templates directory):

`hg serve --style `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">style</span>

- Start a web server instance using the specified SSL certificate bundle:

`hg serve --certificate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/certificate</span>
