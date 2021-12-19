---
layout: page
title: common/stty (English)
description: "Set options for a terminal device interface."
content_hash: 42d57bfeaaa8eea1f71139629e01855aea005e39
related_topics:
  - title: 中文 version
    url: /zh/common/stty.html
    icon: bi bi-globe
---
# stty

Set options for a terminal device interface.
More information: <https://www.gnu.org/software/coreutils/stty>.

- Display all settings for the current terminal:

`stty -a`

- Set the number of rows:

`stty rows `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rows</span>

- Set the number of columns:

`stty cols `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cols</span>

- Get the actual transfer speed of a device:

`stty -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/device_file</span>` speed`

- Reset all modes to reasonable values for the current terminal:

`stty sane`
