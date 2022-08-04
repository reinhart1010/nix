---
layout: page
title: linux/tic (English)
description: "Compile terminfo and install for ncurses."
content_hash: 43895a53aa3dc28b3e034fceeebd4baf38a8e143
---
# tic

Compile terminfo and install for ncurses.
More information: <https://pubs.opengroup.org/onlinepubs/007908799/xcurses/terminfo.html>.

- Compile and install terminfo for a terminal:

`tic -xe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">terminal</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/terminal.info</span>

- Check terminfo file for errors:

`tic -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/terminal.info</span>

- Print database locations:

`tic -D`
