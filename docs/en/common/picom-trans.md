---
layout: page
title: common/picom-trans (English)
description: "Set the window opacity for the `picom` window compositor."
content_hash: 8928de784f040117479719dd926c365a62f654b3
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# picom-trans

Set the window opacity for the `picom` window compositor.
More information: <https://github.com/yshui/picom>.

- Set the currently focused window opacity to a specific percentage:

`picom-trans --current --opacity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">90</span>

- Set the opacity of a window with a specific name:

`picom-trans --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Firefox</span>` --opacity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">90</span>

- Set the opacity of a specific window selected via mouse cursor:

`picom-trans --select --opacity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">90</span>

- Toggle the opacity of a specific window:

`picom-trans --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Firefox</span>` --toggle`
