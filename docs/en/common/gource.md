---
layout: page
title: common/gource (English)
description: "Renders an animated tree diagram of Git, SVN, Mercurial and Bazaar repositories."
content_hash: 8e259863434ccd3878a5264e1834eb26fe0165b0
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# gource

Renders an animated tree diagram of Git, SVN, Mercurial and Bazaar repositories.
It shows files and directories being created, modified or removed over time.
More information: <https://gource.io>.

- Run gource in a directory (if it isn't the repository's root directory, the root is sought up from there):

`gource `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repository</span>

- Run gource in the current directory, with a custom output resolution:

`gource -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height</span>

- Set a custom timescale for the animation:

`gource -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">time_scale_multiplier</span>

- Set how long each day should be in the animation (this combines with -c, if provided):

`gource -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>

- Set fullscreen mode and a custom background color:

`gource -f -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hex_color_code</span>

- Set a title for the animation:

`gource --title `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">title</span>
