---
layout: page
title: linux/fuzzel (English)
description: "A Wayland-native application launcher and fuzzy finder, inspired by `rofi` and `dmenu`."
content_hash: ade98937bef21860aaf928165563f50ad3b8f71a
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/linux/fuzzel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fuzzel

A Wayland-native application launcher and fuzzy finder, inspired by `rofi` and `dmenu`.
More information: <https://codeberg.org/dnkl/fuzzel>.

- Run applications:

`fuzzel`

- Run `fuzzel` in dmenu mode:

`fuzzel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--dmenu</span>

- Display a menu of the output of the `ls` command:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls</span>` | fuzzel -d`

- Display a menu with custom items separated by a new line (`\n`):

`echo -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">red</span>`\n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">green</span>`\n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blue</span>`" | fuzzel -d`

- Let the user choose between multiple items and save the selected one to a file:

`echo -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">red</span>`\n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">green</span>`\n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blue</span>`" | fuzzel -d > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">color.txt</span>

- Reset apps usage count (default cache directory: `$XDG_CACHE_HOME/fuzzel`):

`rm -v $HOME/.cache/fuzzel`

- Launch `fuzzel` on a specific monitor, see `wlr-randr` or `swaymsg -t get_outputs`:

`fuzzel -o "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DP-1</span>`"`

- Use `fuzzel` to do an online search:

`fuzzel -d -l 0 --placeholder "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Type your search</span>`" | sed 's/^/\"/g;s/$/\"/g' | xargs firefox --search`
