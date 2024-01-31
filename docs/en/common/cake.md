---
layout: page
title: common/cake (English)
description: "The command-line processor for the CakePHP framework."
content_hash: 9a68f337d8c5fde5874eeeddb0c450595b155fad
last_modified_at: 2024-01-31
related_topics:
  - title: italiano version
    url: /it/common/cake.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cake.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cake

The command-line processor for the CakePHP framework.
More information: <https://cakephp.org>.

- Display basic information about the current app and available commands:

`cake`

- List available routes:

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
