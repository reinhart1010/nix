---
layout: page
title: common/magick-import (English)
description: "Capture some or all of an X server screen and save the image to a file."
content_hash: 72d3c39a3980b38687900c6dc17e98028a22257a
last_modified_at: 2024-06-04
tldri18n_status: 2
---
# magick import

Capture some or all of an X server screen and save the image to a file.
See also: `magick`.
More information: <https://imagemagick.org/script/import.php>.

- Capture the entire X server screen into a PostScript file:

`magick import -window root `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ps</span>

- Capture contents of a remote X server screen into a PNG image:

`magick import -window root -display `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">screen</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">display</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.png</span>

- Capture a specific window given its ID as displayed by `xwininfo` into a JPEG image:

`magick import -window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">window_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.jpg</span>
