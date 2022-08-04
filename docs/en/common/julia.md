---
layout: page
title: common/julia (English)
description: "A high-level, high-performance dynamic programming language for technical computing."
content_hash: 74ef029ff191bdf514381799244f3eadef607539
---
# julia

A high-level, high-performance dynamic programming language for technical computing.
More information: <https://docs.julialang.org/en/v1/manual/getting-started/>.

- Start a REPL (interactive shell):

`julia`

- Execute a Julia program and exit:

`julia `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program.jl</span>

- Execute a Julia program that takes arguments:

`julia `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program.jl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arguments</span>

- Evaluate a string containing Julia code:

`julia -e '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">julia_code</span>`'`

- Evaluate a string of Julia code, passing arguments to it:

`julia -e '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">for x in ARGS; println(x); end</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arguments</span>

- Evaluate an expression and print the result:

`julia -E '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(1 - cos(pi/4))/2</span>`'`

- Start Julia in parallel mode, using N worker processes:

`julia -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>
