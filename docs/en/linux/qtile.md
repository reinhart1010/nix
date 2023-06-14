---
layout: page
title: linux/qtile (English)
description: "A full-featured, hackable tiling window manager written and configured in Python."
content_hash: 0aa0019c0ffa6a536c9d24f8e09159e6b6c53aa3
last_modified_at: 2023-06-14
---
# qtile

A full-featured, hackable tiling window manager written and configured in Python.
More information: <https://docs.qtile.org/en/latest/manual/commands/shell/index.html>.

- Start the window manager, if it is not running already (should ideally be run from `.xsession` or similar):

`qtile start`

- Check the configuration file for any compilation errors (default location is `~/.config/qtile/config.py`):

`qtile check`

- Show current resource usage information:

`qtile top --force`

- Open the program `xterm` as a floating window on the group named `test-group`:

`qtile run-cmd --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test-group</span>` --float `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xterm</span>

- Restart the window manager:

`qtile cmd-obj --object cmd --function restart`
