---
layout: page
title: common/cs (English)
description: "Application and artifact manager for the Scala language, it can install Scala applications and setup your Scala development environment."
content_hash: d5097079598191bae16a3625d54e17c18c28b15a
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# coursier

Application and artifact manager for the Scala language, it can install Scala applications and setup your Scala development environment.
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
