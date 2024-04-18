---
layout: page
title: linux/sm (English)
description: "Display a short message fullscreen."
content_hash: 223540121268ac71b7c78fbd94cee14535298528
last_modified_at: 2024-04-18
tldri18n_status: 2
---
# sm

Display a short message fullscreen.
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
