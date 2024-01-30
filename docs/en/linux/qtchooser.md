---
layout: page
title: linux/qtchooser (English)
description: "A wrapper used to select between Qt development binary versions."
content_hash: aa5b8f3fc2eb4c3645437ae6f1ebb911c198e1f2
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# qtchooser

A wrapper used to select between Qt development binary versions.
More information: <https://manned.org/qtchooser>.

- List available Qt versions from the configuration files:

`qtchooser --list-versions`

- Print environment information:

`qtchooser --print-env`

- Run the specified tool using the specified Qt version:

`qtchooser --run-tool=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tool</span>` --qt=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version_name</span>

- Add a Qt version entry to be able to choose from:

`qtchooser --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/qmake</span>

- Display help:

`qtchooser --help`
