---
layout: page
title: common/rsstail (English)
description: "`tail` for RSS feeds."
content_hash: 25782b140a53071a6d997a6857ffa6fb700ef23f
---
# rsstail

`tail` for RSS feeds.
More information: <https://github.com/gvalkov/rsstail.py>.

- Show the feed of a given URL and wait for new entries appearing at the bottom:

`rsstail -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Show the feed in reverse chronological order (newer at the bottom):

`rsstail -r -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Include publication date and link:

`rsstail -pl -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Set update interval:

`rsstail -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interval_in_seconds</span>

- Show feed and exit:

`rsstail -1 -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>
