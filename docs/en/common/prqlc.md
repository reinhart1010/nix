---
layout: page
title: common/prqlc (English)
description: "PRQL compiler."
content_hash: abbc5266f372c9491794c45da69c8e84e963ac03
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# prqlc

PRQL compiler.
PRQL is a modern language for transforming data - a simple, powerful, pipelined SQL replacement.
More information: <https://prql-lang.org>.

- Run the compiler interactively:

`prqlc compile`

- Compile a specific `.prql` file to `stdout`:

`prqlc compile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.prql</span>

- Compile a `.prql` file to a `.sql` file:

`prqlc compile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.prql</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target.sql</span>

- Compile a query:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">from employees | filter has_dog | select salary</span>`" | prqlc compile`

- Watch a directory and compile on file modification:

`prqlc watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
