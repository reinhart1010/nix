---
layout: page
title: common/dub (English)
description: "Package manager for D packages."
content_hash: 43844292ae92bbe53c437463d3c5a452af9accaa
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# dub

Package manager for D packages.
More information: <https://dub.pm/commandline>.

- Interactively create a new D project:

`dub init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>

- Non-interactively create a new D project:

`dub init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>` -n`

- Build and run a D project:

`dub`

- Install dependencies specified in a D project's `dub.json` or `dub.sdl` file:

`dub fetch`

- Update the dependencies in a D project:

`dub upgrade`

- Display help:

`dub --help`
