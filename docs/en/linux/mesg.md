---
layout: page
title: linux/mesg (English)
description: "Check or set a terminal's ability to receive messages from other users, usually from the `write` command."
content_hash: c58b3e04e638d3882b29586afce6facfe9f2aec7
last_modified_at: 2024-02-04
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mesg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mesg

Check or set a terminal's ability to receive messages from other users, usually from the `write` command.
See also `write`, `talk`.
More information: <https://manned.org/mesg.1>.

- Check terminal's openness to write messages:

`mesg`

- Disallow receiving messages from other users:

`mesg n`

- Allow receiving messages from other users:

`mesg y`

- Enable [v]erbose mode, printing a warning if the command is not executed from a terminal:

`mesg --verbose`
