---
layout: page
title: common/polybar (English)
description: "A fast and easy-to-use status bar."
content_hash: d32bbcdaafecceeb448797309cd0cd16a075c2e0
last_modified_at: 2023-08-02
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># polybar

A fast and easy-to-use status bar.
More information: <https://github.com/polybar/polybar/wiki>.

- Start Polybar (the bar name is optional if only one bar is defined in the config):

`polybar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar_name</span>

- Start Polybar with the specified config:

`polybar --config=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.ini</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar_name</span>

- Start Polybar and reload the bar when the config file is modified:

`polybar --reload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar_name</span>
