---
layout: page
title: common/mytop (English)
description: "Display MySQL server performance info like `top`."
content_hash: e90a5e2ffb120e87c67b78135ec98039421f45ce
---
# mytop

Display MySQL server performance info like `top`.
More information: <http://jeremy.zawodny.com/mysql/mytop/mytop.html>.

- Start mytop:

`mytop`

- Connect with a specified username and password:

`mytop -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Connect with a specified username (the user will be prompted for a password):

`mytop -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` --prompt`

- Do not show any idle (sleeping) threads:

`mytop -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` --noidle`
