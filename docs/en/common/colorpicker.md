---
layout: page
title: common/colorpicker (English)
description: "A minimalist X11 colorpicker."
content_hash: a1558d386390d30b2bf7015f7732ec055a96a31e
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# colorpicker

A minimalist X11 colorpicker.
Any mouse gesture except left click will exit the program.
More information: <https://github.com/ym1234/colorpicker>.

- Launch colorpicker and print the hexadecimal and RGB value of each clicked pixel to `stdout`:

`colorpicker`

- Only print the color of one clicked pixel and then exit:

`colorpicker --one-shot`

- Print the color of each clicked pixel and quit when a key is pressed:

`colorpicker --quit-on-keypress`

- Only print the RGB value:

`colorpicker --rgb`

- Only print the hexadecimal value:

`colorpicker --hex`
