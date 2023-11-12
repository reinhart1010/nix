---
layout: page
title: common/raco (English)
description: "Racket command-line tools."
content_hash: c4efc505f67f1f189dbc7073cb7d703060f9aeed
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# raco

Racket command-line tools.
More information: <https://docs.racket-lang.org/raco/>.

- Install a package, automatically installing dependencies:

`raco pkg install --auto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_source</span>

- Install the current directory as a package:

`raco pkg install`

- Build (or rebuild) bytecode, documentation, executables, and metadata indexes for collections:

`raco setup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">collection1 collection2 ...</span>

- Run tests in files:

`raco test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/tests1.rkt path/to/tests2.rkt ...</span>

- Search local documentation:

`raco docs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_terms ...</span>

- Display help:

`raco help`
