---
layout: page
title: common/jrnl (English)
description: "A simple journal application for your command-line."
content_hash: 4ecabf575b9451271493131576865f229e4b30ca
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/common/jrnl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jrnl

A simple journal application for your command-line.
More information: <http://jrnl.sh>.

- Insert a new entry with your editor:

`jrnl`

- Quickly insert a new entry:

`jrnl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">today at 3am</span>`: `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">title</span>`. `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">content</span>

- View the last ten entries:

`jrnl -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- View everything that happened from the start of last year to the start of last march:

`jrnl -from "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">last year</span>`" -until `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">march</span>

- Edit all entries tagged with "texas" and "history":

`jrnl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@texas</span>` -and `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@history</span>` --edit`
