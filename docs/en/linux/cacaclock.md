---
layout: page
title: linux/cacaclock (English)
description: "Display the current time as ASCII art."
content_hash: 8e1d6e6302e80b3222690fd5cbabbaa8995f2f6a
last_modified_at: 2024-04-02
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/cacaclock.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cacaclock

Display the current time as ASCII art.
More information: <https://packages.debian.org/sid/caca-utils>.

- Display the time:

`cacaclock`

- Change the font:

`cacaclock -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">font</span>

- Change the format using an `strftime` format specification:

`cacaclock -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">strftime_arguments</span>
