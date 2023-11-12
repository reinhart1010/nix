---
layout: page
title: common/box (English)
description: "A PHP application for building and managing Phars."
content_hash: e16f6ff05aed5508cd7d11ec6f5800b035afaed6
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/common/box.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/box.html
    icon: bi bi-globe
tldri18n_status: 2
---
# box

A PHP application for building and managing Phars.
More information: <https://github.com/box-project/box>.

- Compile a new Phar file:

`box compile`

- Compile a new Phar file using a specific config file:

`box compile -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config</span>

- Display information about the PHAR PHP extension:

`box info`

- Display information about a specific Phar file:

`box info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/phar_file</span>

- Validate the first found config file in the working directory:

`box validate`

- Verify the signature of a specific Phar file:

`box verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/phar_file</span>

- Display all available commands and options:

`box help`
