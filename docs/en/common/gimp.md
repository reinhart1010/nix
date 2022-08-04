---
layout: page
title: common/gimp (English)
description: "GNU image manipulation program."
content_hash: 6c420fb2ebc21949587aa480cd961763dcaea75a
related_topics:
  - title: français version
    url: /fr/common/gimp.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/gimp.html
    icon: bi bi-globe
---
# gimp

GNU image manipulation program.
See also: `krita`.
More information: <https://docs.gimp.org/en/gimp-fire-up.html#gimp-concepts-running-command-line>.

- Start GIMP:

`gimp`

- Open specific files:

`gimp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image1 path/to/image2 ...</span>

- Open specific files in a new window:

`gimp --new-instance `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image1 path/to/image2 ...</span>

- Start without a splash screen:

`gimp --no-splash`

- Print errors and warnings to the console instead of showing them in a dialog box:

`gimp --console-messages`

- Enable debugging signal handlers:

`gimp --debug-handlers`
