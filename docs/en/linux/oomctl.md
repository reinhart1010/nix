---
layout: page
title: linux/oomctl (English)
description: "Analyze the state stored in `systemd-oomd`."
content_hash: cee13899bbff9064c93e4a24cbc270e781786eec
last_modified_at: 2023-04-26
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># oomctl

Analyze the state stored in `systemd-oomd`.
More information: <https://www.freedesktop.org/software/systemd/man/oomctl.html>.

- Show the current state of the cgroups and system contexts stored by `systemd-oomd`:

`oomctl dump`
