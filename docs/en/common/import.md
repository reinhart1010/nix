---
layout: page
title: common/import (English)
description: "Capture some or all of an X server screen, and save the image to a file."
content_hash: 152602a8b52b55ca32896f858e6b7a5c5c2c8cd0
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# import

Capture some or all of an X server screen, and save the image to a file.
Part of ImageMagick.
More information: <https://imagemagick.org/script/import.php>.

- Capture the entire X server screen into a PostScript file:

`import -window root `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ps</span>

- Capture contents of a remote X server screen into a PNG image:

`import -window root -display `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">screen</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">display</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.png</span>

- Capture a specific window given its ID as displayed by `xwininfo` into a JPEG image:

`import -window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">window_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.jpg</span>
