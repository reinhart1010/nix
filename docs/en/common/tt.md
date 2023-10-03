---
layout: page
title: common/tt (English)
description: "A terminal based typing test."
content_hash: 64a60eb6eb561c9b930998af9f98bae1cf152dd2
last_modified_at: 2023-10-03
---
# tt

A terminal based typing test.
More information: <https://github.com/lemnos/tt>.

- Start quote mode with the builtin quote list in English:

`tt -quotes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en</span>

- Produce a test consisting of 50 randomly drawn words in 5 groups of 10 words each:

`tt -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- Start a timed test lasting 10 seconds:

`tt -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Start `tt` with no theming and showing your WPM as you type:

`tt -showwpm -notheme`
