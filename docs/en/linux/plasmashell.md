---
layout: page
title: linux/plasmashell (English)
description: "Start and restart Plasma Desktop."
content_hash: e5b38617e6921ba483bcd573c76ad6422d6d8625
last_modified_at: 2024-08-15
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/plasmashell.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># plasmashell

Start and restart Plasma Desktop.
More information: <https://invent.kde.org/plasma/plasma-desktop>.

- Restart `plasmashell`:

`systemctl restart --user plasma-plasmashell`

- Restart `plasmashell` without systemd:

`plasmashell --replace & disown`

- Display [h]elp on command-line options:

`plasmashell --help`

- Display help, including Qt options:

`plasmashell --help-all`
