---
layout: page
title: linux/systemd-inhibit (English)
description: "Prohibit the system from entering certain power states."
content_hash: 2cfcc674c55eef36420531d8a28b0fc472d9554b
last_modified_at: 2023-10-10
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># systemd-inhibit

Prohibit the system from entering certain power states.
Inhibitor locks may be used to block or delay system sleep and shutdown requests as well as automatic idle handling.
More information: <https://www.freedesktop.org/software/systemd/man/systemd-inhibit.html>.

- List all active inhibition locks and the reasons for their creation:

`systemd-inhibit --list`

- Block system shutdown for a specified number of seconds with the `sleep` command:

`systemd-inhibit --what shutdown sleep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- Keep the system from sleeping or idling until the download is complete:

`systemd-inhibit --what sleep:idle wget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/file</span>

- Ignore lid close switch until the script exits:

`systemd-inhibit --what sleep:handle-lid-switch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script</span>

- Ignore power button press while command is running:

`systemd-inhibit --what handle-power-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Describe who and why created the inhibitor (default: the command and its arguments for `--who` and `Unknown reason` for `--why`):

`systemd-inhibit --who `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$USER</span>` --why `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reason</span>` --what `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">operation</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
