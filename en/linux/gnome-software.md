---
layout: page
title: linux/gnome-software (English)
description: "Add and remove applications and update your system."
content_hash: 6f926de5f94e94c513a936973a43e71b303795e7
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># gnome-software

Add and remove applications and update your system.
More information: <https://apps.gnome.org/app/org.gnome.Software/>.

- Launch the GNOME Software GUI if it's not already running:

`gnome-software`

- Launch the GNOME Software GUI if it's not open, and navigate to the specified page:

`gnome-software --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">updates|updated|installed|overview</span>

- Launch the GNOME Software GUI if it's not open, and view the specified package:

`gnome-software --details `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Display the version:

`gnome-software --version`
