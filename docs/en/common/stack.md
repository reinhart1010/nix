---
layout: page
title: common/stack (English)
description: "Tool for managing Haskell projects."
content_hash: 06646b0a7ea06de259a399cad08aa99bc3ea8b97
---
# stack

Tool for managing Haskell projects.
More information: <https://github.com/commercialhaskell/stack>.

- Create a new package:

`stack new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">template_name</span>

- Compile a package:

`stack build`

- Run tests inside a package:

`stack test`

- Compile a project and re-compile every time a file changes:

`stack build --file-watch`

- Compile a project and execute a command after compilation:

`stack build --exec "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`

- Run a program and pass an argument to it:

`stack exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program_name</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument</span>
