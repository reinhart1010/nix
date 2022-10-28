---
layout: page
title: linux/qtile (English)
description: "A full-featured, hackable tiling window manager written and configured in Python."
content_hash: f11d29b56c81fa6b9cbf71a1202459e13d0a1edc
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># qtile

A full-featured, hackable tiling window manager written and configured in Python.
More information: <https://docs.qtile.org/en/latest/manual/commands/shell/index.html>.

- Start the window manager, if it is not running already (should ideally be run from `.xsession` or similar):

`qtile start`

- Check the configuration file for any compilation errors (default location is  `~/.config/qtile/config.py`):

`qtile check`

- Show current resource usage information:

`qtile top --force`

- Open the program `xterm` as a floating window on the group named `test-group`:

`qtile run-cmd --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test-group</span>` --float `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xterm</span>

- Restart the window manager:

`qtile cmd-obj --object cmd --function restart`
