---
layout: page
title: common/cs (English)
description: "Application and artifact manager for the Scala language."
content_hash: 2bb4ce7f649deb7a5373250de14f0964b3f16f95
last_modified_at: 2023-12-30
tldri18n_status: 2
---
# cs

Application and artifact manager for the Scala language.
Installs Scala applications and sets up a Scala development environment.
Some subcommands such as `install`, `launch`, `java`, `fetch`, `resolve`, `complete-dep`, etc. have their own usage documentation.
More information: <https://get-coursier.io/docs/overview>.

- Display version:

`cs version`

- Show a list of the installed applications:

`cs list`

- Install a specific application:

`cs install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application_name</span>

- Uninstall a specific application:

`cs uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application_name</span>

- Setup machine for the Scala development:

`cs setup`

- Update all the installed applications:

`cs update`
