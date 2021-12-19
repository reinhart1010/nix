---
layout: page
title: linux/xdg-mime (English)
description: "Query and manage MIME types according to the XDG standard."
content_hash: 3cd7b9c595e39dcc8c244e4dc021fb27cfa9e603
---
# xdg-mime

Query and manage MIME types according to the XDG standard.
More information: <https://portland.freedesktop.org/doc/xdg-mime.html>.

- Display the MIME type of a file:

`xdg-mime query filetype `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display the default application for opening PNGs:

`xdg-mime query default `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image/png</span>

- Display the default application for opening a specific file:

`xdg-mime query default $(xdg-mime query filetype `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`)`

- Set imv as the default application for opening PNG and JPEG images:

`xdg-mime default `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imv.desktop</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image/png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image/jpeg</span>
