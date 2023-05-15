---
layout: page
title: linux/systemd-ac-power (English)
description: "Report whether the computer is connected to an external power source."
content_hash: 4c9f83a101cf843bee6ed3e82f507848932a0a0c
last_modified_at: 2023-05-15
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># systemd-ac-power

Report whether the computer is connected to an external power source.
More information: <https://www.freedesktop.org/software/systemd/man/systemd-ac-power.html>.

- Silently check and return a 0 status code when running on AC power, and a non-zero code otherwise:

`systemd-ac-power`

- Additionally print `yes` or `no` to `stdout`:

`systemd-ac-power --verbose`
