---
layout: page
title: common/cake (English)
description: "The command-line processor for the CakePHP framework."
content_hash: 09cff9c52b744365d2f9f80d4577b6c39452c147
related_topics:
  - title: italiano version
    url: /it/common/cake.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cake.html
    icon: bi bi-globe
---
# cake

The command-line processor for the CakePHP framework.
More information: <https://cakephp.org>.

- Display basic information about the current app and available commands:

`cake`

- Display a list of available routes:

`cake routes`

- Clear configuration caches:

`cake cache clear_all`

- Build the metadata cache:

`cake schema_cache build --connection `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">connection</span>

- Clear the metadata cache:

`cake schema_cache clear`

- Clear a single cache table:

`cake schema_cache clear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table_name</span>

- Start a development web server (defaults to port 8765):

`cake server`

- Start a REPL (interactive shell):

`cake console`
