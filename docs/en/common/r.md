---
layout: page
title: common/r (English)
description: "R language interpreter."
content_hash: 47dacc188a76086c8fd25a5c35eff6a8f55e1ccf
last_modified_at: 2024-01-30
related_topics:
  - title: français version
    url: /fr/common/r.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/r.html
    icon: bi bi-globe
tldri18n_status: 2
---
# R

R language interpreter.
More information: <https://www.r-project.org>.

- Start a REPL (interactive shell):

`R`

- Start R in vanilla mode (i.e. a blank session that doesn't save the workspace at the end):

`R --vanilla`

- Execute a file:

`R -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.R</span>

- Execute an R expression and then exit:

`R -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expr</span>

- Run R with a debugger:

`R -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">debugger</span>

- Check R packages from package sources:

`R CMD check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package_source</span>

- Display version:

`R --version`
