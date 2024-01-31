---
layout: page
title: osx/emond (English)
description: "Event Monitor service that accepts events from various services, runs them through a simple rules engine, and takes action."
content_hash: 2a6a7c0f6ee7f752b891c91908df892cbe5bc3ee
last_modified_at: 2024-01-31
related_topics:
  - title: español version
    url: /es/osx/emond.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/emond.html
    icon: bi bi-globe
tldri18n_status: 2
---
# emond

Event Monitor service that accepts events from various services, runs them through a simple rules engine, and takes action.
The actions can run commands, send email, or SMS messages.
More information: <https://keith.github.io/xcode-man-pages/emond.8.html>.

- Start the daemon:

`emond`

- Specify rules for emond to process by giving a path to a file or directory:

`emond -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Use a specific configuration file:

`emond -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config_file</span>
