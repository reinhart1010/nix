---
layout: page
title: linux/blurlock (English)
description: "A simple wrapper around the i3 screen locker `i3lock`, which blurs the screen."
content_hash: 34bdbeb7305a744b7971c18011cd52b3ff0ac3c2
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# blurlock

A simple wrapper around the i3 screen locker `i3lock`, which blurs the screen.
See also: `i3lock`.
More information: <https://gitlab.manjaro.org/packages/community/i3/i3exit/-/blob/master/blurlock>.

- Lock the screen to a blurred screenshot of the current screen:

`blurlock`

- Lock the screen and disable the unlock indicator (removes feedback on keypress):

`blurlock --no-unlock-indicator`

- Lock the screen and don't hide the mouse pointer:

`blurlock --pointer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">default</span>

- Lock the screen and show the number of failed login attempts:

`blurlock --show-failed-attempts`
