---
layout: page
title: common/racket (English)
description: "Racket language interpreter."
content_hash: 52fee3c55af3f35e490622c2d3757051ed9180d1
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# racket

Racket language interpreter.
More information: <https://racket-lang.org>.

- Start a REPL (interactive shell):

`racket`

- Execute a Racket script:

`racket `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.rkt</span>

- Execute a Racket expression:

`racket --eval "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression</span>`"`

- Run module as a script (terminates option list):

`racket --lib `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>` --main `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arguments</span>

- Start a REPL (interactive shell) for the `typed/racket` hashlang:

`racket -I typed/racket`
