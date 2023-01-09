---
layout: page
title: common/cs (English)
description: "Application and artifact manager for the Scala language, it can install Scala applications and setup your Scala development environment."
content_hash: 3c25d60c2f426688bddb2fce1bced22adccaebd9
last_modified_at: 2023-01-09
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># coursier

Application and artifact manager for the Scala language, it can install Scala applications and setup your Scala development environment.
Some subcommands such as `install`, `launch`, `java`, `fetch`, `resolve`, `complete-dep`, etc. have their own usage documentation, accessible via `tldr cs subcommand`.
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
