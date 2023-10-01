---
layout: page
title: osx/goku (English)
description: "Manage Karabiner configuration."
content_hash: d0c0f96a004a971c7ecb51eac547a7a2e80233a0
last_modified_at: 2023-10-01
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># goku

Manage Karabiner configuration.
More information: <https://github.com/yqrashawn/GokuRakuJoudo>.

- Generate `karabiner.json` using the default configuration:

`goku`

- Generate `karabiner.json` using the specific `config.edn` file:

`goku --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.edn</span>

- Dry run the new configuration into `stdout` instead of updating `karabiner.json`:

`goku --dry-run`

- Dry run the whole configuration into `stdout` instead of updating `karabiner.json`:

`goku --dry-run-all`

- Display help:

`goku --help`

- Display version:

`goku --version`
