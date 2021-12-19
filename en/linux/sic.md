---
layout: page
title: linux/sic (English)
description: "Simple IRC client."
content_hash: fd2f3d7c7daf2ddc14450c8c4711fb9a355ee773
---
# sic

Simple IRC client.
Part of the suckless tools.
More information: <https://tools.suckless.org/sic/>.

- Connect to the default host (irc.ofct.net) with the nickname set in the `$USER` environment variable:

`sic`

- Connect to a given host, using a given nickname:

`sic -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nickname</span>

- Connect to a given host, using a given nickname and password:

`sic -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nickname</span>` -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Join a channel:

`:j #`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">channel</span>`<Enter>`

- Send a message to a channel or user:

`:m #`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">channel|user</span>`<Enter>`

- Set default channel or user:

`:s #`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">channel|user</span>`<Enter>`
