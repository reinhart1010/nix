---
layout: page
title: common/wal (English)
description: "Create color schemes based on the dominant colors of a wallpaper."
content_hash: 8f051d52713b660324d889ead695cc715d587a44
last_modified_at: 2024-02-15
related_topics:
  - title: català version
    url: /ca/common/wal.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wal

Create color schemes based on the dominant colors of a wallpaper.
More information: <https://github.com/dylanaraps/pywal>.

- Preview color scheme:

`wal --preview `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.png</span>

- Create color scheme:

`wal -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.png</span>

- Create a light color scheme:

`wal -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.png</span>` -l`

- Skip setting the desktop wallpaper:

`wal -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.png</span>` -n`

- Skip setting the terminal colors:

`wal -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.png</span>` -s`

- Restore the previously generated color scheme and wallpaper:

`wal -R`
