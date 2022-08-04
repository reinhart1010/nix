---
layout: page
title: linux/kscreen-doctor (English)
description: "Change and manipulate the screen setup from the command-line."
content_hash: 3bdf9a7f082bd78c1c60e6b7ce90d37255b95131
---
# kscreen-doctor

Change and manipulate the screen setup from the command-line.
More information: <https://invent.kde.org/plasma/libkscreen>.

- Show display output information:

`kscreen-doctor --outputs`

- Set the rotation of a display output with an ID of 1 to the right:

`kscreen-doctor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.1.rotation.right</span>

- Set the scale of a display output with an ID of `HDMI-2` to 2 (200%):

`kscreen-doctor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.HDMI-2.scale.2</span>
