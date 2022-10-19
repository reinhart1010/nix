---
layout: page
title: common/mamba (English)
description: "Fast, cross-platform package manager, intended as a drop-in replacement for conda."
content_hash: 19c2d481a971aac42700b54fdc6c1beb88d64bb4
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mamba

Fast, cross-platform package manager, intended as a drop-in replacement for conda.
Some subcommands such as `mamba repoquery` have their own usage documentation.
More information: <https://mamba.readthedocs.io/en/latest/user_guide/mamba.html>.

- Create a new environment, installing the specified packages into it:

`mamba create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">python=3.10 matplotlib</span>

- Install packages into the current environment, specifying the package [c]hannel:

`mamba install -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">conda-forge</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">python=3.6 numpy</span>

- Update all packages in the current environment:

`mamba update --all`

- Search for a specific package across repositories:

`mamba repoquery search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numpy</span>

- List all environments:

`mamba info --envs`

- Remove unused [p]ackages and [t]arballs from the cache:

`mamba clean -pt`

- Activate an environment:

`mamba activate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment_name</span>

- List all installed packages in the currently activated environment:

`mamba list`
