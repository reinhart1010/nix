---
layout: page
title: linux/kscreen-doctor (English)
description: "Change and manipulate the screen setup."
content_hash: 6b97667c618cb9e72da0132f6b4cc81cb4283ef8
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# kscreen-doctor

Change and manipulate the screen setup.
More information: <https://invent.kde.org/plasma/libkscreen>.

- Show display output information:

`kscreen-doctor --outputs`

- Set the rotation of a display output with an ID of 1 to the right:

`kscreen-doctor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.1.rotation.right</span>

- Set the scale of a display output with an ID of `HDMI-2` to 2 (200%):

`kscreen-doctor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.HDMI-2.scale.2</span>
