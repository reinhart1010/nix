---
layout: page
title: linux/swww (English)
description: "Efficient animated wallpaper daemon for Wayland."
content_hash: 224bb8f5eaf3122d3802ef3c7ff4f445ec9074db
last_modified_at: 2024-10-28
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/swww.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># swww

Efficient animated wallpaper daemon for Wayland.
See also: `swww-daemon`.
More information: <https://github.com/LGFae/swww>.

- Set wallpaper:

`swww img `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image</span>

- Set wallpaper to specified [o]utputs:

`swww img -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output1,output2,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image</span>

- Restore last wallpaper:

`swww restore`

- Kill daemon:

`swww kill`

- Display output information:

`swww query`
