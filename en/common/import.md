---
layout: page
title: common/import (English)
description: "Capture some or all of an X server screen, and save the image to a file."
content_hash: 0c05bc291c6157725fdba16365cc8d418156dda8
---
# import

Capture some or all of an X server screen, and save the image to a file.
Part of the ImageMagick library.
More information: <https://imagemagick.org/script/import.php>.

- Capture the entire X server screen in the PostScript image format:

`import -window root `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.postscript</span>

- Capture contents of a remote X server screen in the PNG format:

`import -window root -display `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">screen</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">display</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.png</span>

- Capture a specific window, given its ID as displayed by `xwininfo`, into the JPEG format:

`import -window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">window_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.jpg</span>
