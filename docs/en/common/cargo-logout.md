---
layout: page
title: common/cargo-logout (English)
description: "Remove an API token from the registry locally."
content_hash: f0d65a006ac895887a2211ba6e1148e5cafb2477
last_modified_at: 2023-10-08
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cargo logout

Remove an API token from the registry locally.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-logout.html>.

- Remove the API token from the local credential storage:

`cargo logout`

- Add the name of the registry to use:

`cargo logout --registry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">registry</span>

- Display verbose output:

`cargo logout --verbose`

- Do not print Cargo log message:

`cargo logout --quiet`

- Control when colored output is used:

`cargo logout --color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">auto|always|never</span>

- Override a Cargo configuration value:

`cargo logout --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">KEY=VALUE|PATH</span>

- Change the current directory before executing any specified operation:

`cargo logout -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PATH</span>

- Display help:

`cargo logout --help`
