---
layout: page
title: linux/xmodmap (English)
description: "Utility for modifying keymaps and pointer button mappings in X."
content_hash: 05b0b886b6ce31c47c59b1864686cfc8915915ef
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># xmodmap

Utility for modifying keymaps and pointer button mappings in X.
More information: <https://manned.org/xmodmap>.

- Swap left-click and right-click on the pointer:

`xmodmap -e 'pointer = 3 2 1'`

- Reassign a key on the keyboard to another key:

`xmodmap -e 'keycode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keycode</span>` = `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyname</span>

- Disable a key on the keyboard:

`xmodmap -e 'keycode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keycode</span>` ='`

- Execute all xmodmap expressions in the specified file:

`xmodmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
