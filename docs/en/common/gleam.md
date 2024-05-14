---
layout: page
title: common/gleam (English)
description: "The compiler, build tool, package manager and code formatter for Gleam, \"a friendly language for building type-safe systems that scale!\"."
content_hash: ec51e1611ed0337ce313927074ca411f0f0cf133
last_modified_at: 2024-05-14
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gleam.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gleam

The compiler, build tool, package manager and code formatter for Gleam, "a friendly language for building type-safe systems that scale!".
More information: <https://gleam.run/writing-gleam/command-line-reference/>.

- Create a new gleam project:

`gleam new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>

- Build and run a gleam project:

`gleam run`

- Build the project:

`gleam build`

- Run a project for a particular platform and runtime:

`gleam run --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">platform</span>` --runtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">runtime</span>

- Add a hex dependency to your project:

`gleam add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependency_name</span>

- Run project tests:

`gleam test`

- Format source code:

`gleam format`

- Type check the project:

`gleam check`
