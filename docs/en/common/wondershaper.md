---
layout: page
title: common/wondershaper (English)
description: "Allows the user to limit the bandwidth of one or more network adapters."
content_hash: 3140ae294792122bf6294972c49ba27a95293d1e
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# wondershaper

Allows the user to limit the bandwidth of one or more network adapters.
More information: <https://github.com/magnific0/wondershaper#usage>.

- Display [h]elp:

`wondershaper -h`

- Show the current [s]tatus of a specific [a]dapter:

`wondershaper -s -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adapter_name</span>

- Clear limits from a specific [a]dapter:

`wondershaper -c -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adapter_name</span>

- Set a specific maximum [d]ownload rate (in Kbps):

`wondershaper -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adapter_name</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1024</span>

- Set a specific maximum [u]pload rate (in Kbps):

`wondershaper -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adapter_name</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">512</span>

- Set a specific maximum [d]ownload rate and [u]pload rate (in Kpbs):

`wondershaper -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adapter_name</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1024</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">512</span>
