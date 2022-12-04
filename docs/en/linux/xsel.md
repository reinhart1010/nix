---
layout: page
title: linux/xsel (English)
description: "X11 selection and clipboard manipulation tool."
content_hash: 38dba975a37b26be53bb121ac383357da4aa4d06
last_modified_at: 2022-12-04
related_topics:
  - title: français version
    url: /fr/linux/xsel.html
    icon: bi bi-globe
---
# xsel

X11 selection and clipboard manipulation tool.
More information: <https://manned.org/xsel>.

- Use a command's output as input of the clip[b]oard (equivalent to `Ctrl + C`):

`echo 123 | xsel -ib`

- Use the contents of a file as input of the clipboard:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | xsel -ib`

- Output the clipboard's contents into the terminal (equivalent to `Ctrl + V`):

`xsel -ob`

- Output the clipboard's contents into a file:

`xsel -ob > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Clear the clipboard:

`xsel -cb`

- Output the X11 primary selection's contents into the terminal (equivalent to a mouse middle-click):

`xsel -op`
