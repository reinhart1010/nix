---
layout: page
title: linux/lookandfeeltool (English)
description: "Switch Plasma global themes."
content_hash: c8b0cd324fee93c6e5c17ce710f42e6b28e354f4
last_modified_at: 2025-01-01
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/lookandfeeltool.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># lookandfeeltool

Switch Plasma global themes.
More information: <https://userbase.kde.org/System_Settings/Look_And_Feel>.

- List available global themes:

`lookandfeeltool --list`

- Apply a global theme:

`lookandfeeltool --apply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.example.theme.desktop</span>

- Operate `lookandfeeltool` without a display server:

`lookandfeeltool --platform offscreen`

- Display help:

`lookandfeeltool --help`
