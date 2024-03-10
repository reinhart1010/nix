---
layout: page
title: common/open.fish (English)
description: "Opens files, directories, and URIs with default applications."
content_hash: c9be04ee0bdfa1fcc2067adfee87b74b7ea5511a
last_modified_at: 2024-03-10
related_topics:
  - title: Indonesia version
    url: /id/common/open.fish.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/open.fish.html
    icon: bi bi-globe
tldri18n_status: 2
---
# open

Opens files, directories, and URIs with default applications.
This command is available through fish on operating systems without the built-in `open` command (e.g. Haiku and macOS).
More information: <https://fishshell.com/docs/current/cmds/open.html>.

- Open a file with the associated application:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ext</span>

- Open all the files of a given extension in the current directory with the associated application:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>

- Open a directory using the default file manager:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Open a website using the default web browser:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Open a specific URI using the default application that can handle it:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tel:123</span>
