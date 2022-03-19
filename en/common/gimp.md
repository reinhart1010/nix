---
layout: page
title: common/gimp (English)
description: "GNU image manipulation program."
content_hash: 7dba1cb4f43843dc5aa7c4c4f18addd37c6ce287
---
# gimp

GNU image manipulation program.
See also: `krita`.
More information: <https://docs.gimp.org/en/gimp-fire-up.html#gimp-concepts-running-command-line>.

- Start GIMP:

`gimp`

- Start without the splash screen:

`gimp --no-splash`

- Open the specified files:

`gimp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image1 path/to/image2 ...</span>

- Start the new instance, even if there is already a running one:

`gimp --new-instance`

- Print errors and warnings to the console instead of showing them in a dialog box:

`gimp --console-messages`

- Enable debugging signal handlers:

`gimp --debug-handlers`
