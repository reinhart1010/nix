---
layout: page
title: common/guile (English)
description: "Guile Scheme interpreter."
content_hash: ae130ae6c66a8e918acf3364d08a70f9c3f514ae
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# guile

Guile Scheme interpreter.
More information: <https://www.gnu.org/software/guile>.

- Start a REPL (interactive shell):

`guile`

- Execute the script in a given Scheme file:

`guile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script.scm</span>

- Execute a Scheme expression:

`guile -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression</span>`"`

- Listen on a port or a Unix domain socket (the default is port 37146) for remote REPL connections:

`guile --listen=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_or_socket</span>
