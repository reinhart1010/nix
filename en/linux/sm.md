---
layout: page
title: linux/sm (English)
description: "Displays a short message fullscreen."
content_hash: 94074639ebae9329bd42fbda1f477f0e2eb72d29
---
# sm

Displays a short message fullscreen.
More information: <https://github.com/nomeata/screen-message>.

- Display a message in full-screen:

`sm "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World!</span>`"`

- Display a message with inverted colors:

`sm -i "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World!</span>`"`

- Display a message with a custom foreground color:

`sm -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blue</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World!</span>`"`

- Display a message with a custom background color:

`sm -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">#008888</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World!</span>`"`

- Display a message rotated 3 times (in steps of 90 degrees, counterclockwise):

`sm -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World!</span>`"`

- Display a message using the output from another command:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Hello World!"</span>` | sm -`
