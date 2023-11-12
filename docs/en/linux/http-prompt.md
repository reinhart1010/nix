---
layout: page
title: linux/http-prompt (English)
description: "An interactive command-line HTTP client featuring autocomplete and syntax highlighting."
content_hash: bf964f43dbf27633cfbd20158a0f63bd711aa4cc
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# http-prompt

An interactive command-line HTTP client featuring autocomplete and syntax highlighting.
More information: <https://github.com/httpie/http-prompt>.

- Launch a session targeting the default URL of <http://localhost:8000> or the previous session:

`http-prompt`

- Launch a session with a given URL:

`http-prompt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>

- Launch a session with some initial options:

`http-prompt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">localhost:8000/api</span>` --auth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username:password</span>
