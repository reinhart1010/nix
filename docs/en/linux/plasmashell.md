---
layout: page
title: linux/plasmashell (English)
description: "Start and restart Plasma Desktop."
content_hash: e5b38617e6921ba483bcd573c76ad6422d6d8625
last_modified_at: 2024-08-16
tldri18n_status: 2
---
# plasmashell

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
