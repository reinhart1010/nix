---
layout: page
title: common/entr (English)
description: "Run arbitrary commands when files change."
content_hash: 3adc1d47907c4eee78026631cdb81b9a6bf51179
related_topics:
  - title: italiano version
    url: /it/common/entr.html
    icon: bi bi-globe
---
# entr

Run arbitrary commands when files change.
More information: <https://manned.org/entr>.

- Rebuild with `make` if any file in any subdirectory changes:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ag -l</span>` | entr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make</span>

- Rebuild and test with `make` if any `.c` source files in the current directory change:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls *.c</span>` | entr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'make && make test'</span>

- Send a `SIGTERM` to any previously spawned ruby subprocesses before executing `ruby main.rb`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls *.rb</span>` | entr -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby main.rb</span>

- Run a command with the changed file (`/_`) as an argument:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls *.sql</span>` | entr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">psql -f</span>` /_`
