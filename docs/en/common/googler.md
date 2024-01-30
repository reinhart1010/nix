---
layout: page
title: common/googler (English)
description: "Search Google from command-line."
content_hash: 147b80e00d990f1630a007cc6f4fe2486fbfed32
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# googler

Search Google from command-line.
More information: <https://github.com/jarun/googler>.

- Search Google for a keyword:

`googler `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- Search Google and open the first result in web browser:

`googler -j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- Show N search results (default 10):

`googler -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- Disable automatic spelling correction:

`googler -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- Search one site for a keyword:

`googler -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">site</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- Show Google search result in JSON format:

`googler --json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- Perform in-place self-upgrade:

`googler -u`

- Display help in interactive mode:

`?`
