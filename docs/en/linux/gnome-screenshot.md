---
layout: page
title: linux/gnome-screenshot (English)
description: "Capture the screen, a window, or a user-defined area and save the image to a file."
content_hash: ddd4ae4cfb2e151418640a6349aa37a1d6d98af9
last_modified_at: 2023-11-12
related_topics:
  - title: தமிழ் version
    url: /ta/linux/gnome-screenshot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gnome-screenshot

Capture the screen, a window, or a user-defined area and save the image to a file.
More information: <https://manned.org/gnome-screenshot>.

- Take a screenshot and save it to the default location, normally `~/Pictures`:

`gnome-screenshot`

- Take a screenshot and save it to the named file location:

`gnome-screenshot --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Take a screenshot and save it to the clipboard:

`gnome-screenshot --clipboard`

- Take a screenshot after the specified number of seconds:

`gnome-screenshot --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- Launch the GNOME Screenshot GUI:

`gnome-screenshot --interactive`

- Take a screenshot of the current window and save it to the specified file location:

`gnome-screenshot --window --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Take a screenshot after the specified number of seconds and save it to the clipboard:

`gnome-screenshot --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --clipboard`

- Display the version:

`gnome-screenshot --version`
