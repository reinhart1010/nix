---
layout: page
title: common/prqlc (English)
description: "PRQL compiler."
content_hash: 14f49a388a5c9399c1820bb661caf6937431954b
last_modified_at: 2023-03-21
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># prqlc

PRQL compiler.
PRQL is a modern language for transforming data - a simple, powerful, pipelined SQL replacement.
More information: <https://prql-lang.org>.

- Run the compiler interactively:

`prqlc compile`

- Compile a specific `.prql` file to stdout:

`prqlc compile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.prql</span>

- Compile a `.prql` file to a `.sql` file:

`prqlc compile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.prql</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target.sql</span>

- Compile a query:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">from employees | filter has_dog | select salary</span>`" | prqlc compile`

- Watch a directory and compile on file modification:

`prqlc watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
