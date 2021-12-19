---
layout: page
title: common/gimp (English)
description: "GNU image manipulation program."
content_hash: 5c1aa3edd0bbf7d22ca9e0aca7389096a63d5cd6
---
# gimp

GNU image manipulation program.
More information: <https://docs.gimp.org/en/gimp-fire-up.html#gimp-concepts-running-command-line>.

- Launch GIMP:

`gimp`

- Launch GIMP without showing the splash screen:

`gimp --no-splash`

- Start a new GIMP instance, even if there is already a running one:

`gimp --new-instance`

- Open the given file as a new image:

`gimp --as-new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image</span>

- Print errors and warnings to the console instead of showing them in a dialog box:

`gimp --console-messages`

- Enable debugging signal handlers:

`gimp --debug-handlers`
