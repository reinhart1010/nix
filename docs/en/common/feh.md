---
layout: page
title: common/feh (English)
description: "Lightweight image viewing utility."
content_hash: 49835643fdfb432f2c066e7e6bdc9f0519e9e031
last_modified_at: 2024-02-09
related_topics:
  - title: español version
    url: /es/common/feh.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/feh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# feh

Lightweight image viewing utility.
More information: <https://feh.finalrewind.org>.

- View images locally or using a URL:

`feh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/images</span>

- View images recursively:

`feh --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/images</span>

- View images without window borders:

`feh --borderless `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/images</span>

- Exit after the last image:

`feh --cycle-once `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/images</span>

- Use a specific slideshow cycle delay:

`feh --slideshow-delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/images</span>

- Use a specific wallpaper mode (centered, filled, maximized, scaled or tiled):

`feh --bg-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">center|fill|max|scale|tile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image</span>

- Create a montage of all images within a directory, outputting as a new image:

`feh --montage --thumb-height `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">150</span>` --thumb-width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">150</span>` --index-info "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%nn%wx%h</span>`" --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/montage_image.png</span>
