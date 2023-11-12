---
layout: page
title: linux/screenkey (English)
description: "A screencast tool to display keys pressed."
content_hash: 685b7b2f82d4cc8bf04bf9f62501fdda513d82ff
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# screenkey

A screencast tool to display keys pressed.
More information: <https://www.thregr.org/~wavexx/software/screenkey/>.

- Display keys which are currently being pressed on the screen:

`screenkey`

- Display keys and mouse buttons which are currently being pressed on the screen:

`screenkey --mouse`

- Launch the settings menu of screenkey:

`screenkey --show-settings`

- Launch screenkey at a specific position:

`screenkey --position `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">top|center|bottom|fixed</span>

- Change the format of the key modifiers displayed on screen:

`screenkey --mods-mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">normal|emacs|mac|win|tux</span>

- Change the appearance of screenkey:

`screenkey --bg-color "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">#a1b2c3</span>`" --font `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hack</span>` --font-color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yellow</span>` --opacity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.8</span>

- Drag and select a window on screen to display screenkey:

`screenkey --position fixed --geometry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$(slop -n -f '%g')</span>
