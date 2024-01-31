---
layout: page
title: common/cs (English)
description: "Application and artifact manager for the Scala language."
content_hash: 5747864b3d7baddfa537dfb678d022553a691aff
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# cs

Application and artifact manager for the Scala language.
Installs Scala applications and sets up a Scala development environment.
Some subcommands such as `install`, `launch`, `java`, `fetch`, `resolve`, `complete-dep`, etc. have their own usage documentation.
More information: <https://get-coursier.io/docs/overview>.

- List installed applications:

`cs list`

- Install a specific application:

`cs install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application_name</span>

- Uninstall a specific application:

`cs uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application_name</span>

- Setup machine for the Scala development:

`cs setup`

- Update all the installed applications:

`cs update`

- Display version:

`cs version`
