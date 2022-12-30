---
layout: page
title: linux/autorandr (English)
description: "Automatically change screen layout."
content_hash: 481a8b1690235c044c6bdce2a77903b2a47e0448
last_modified_at: 2022-12-30
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/autorandr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/autorandr.html
    icon: bi bi-globe
---
# autorandr

Automatically change screen layout.
More information: <https://github.com/phillipberndt/autorandr>.

- Save the current screen layout:

`autorandr --save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile_name</span>

- Show the saved profiles:

`autorandr`

- Load the first detected profile:

`autorandr --change`

- Load a specific profile:

`autorandr --load `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile_name</span>

- Set the default profile:

`autorandr --default `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile_name</span>
