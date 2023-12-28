---
layout: page
title: linux/pw-profiler (English)
description: "Profile a local or remote instance."
content_hash: e9da9e5154e7986cc3609a661791f88d0f378094
last_modified_at: 2023-12-28
tldri18n_status: 2
---
# pw-profiler

Profile a local or remote instance.
More information: <https://docs.pipewire.org/page_man_pw-profiler_1.html>.

- Profile the default instance, logging to `profile.log` (`gnuplot` files and a `.html` file for result visualizing are also generated):

`pw-profiler`

- Change the log output file:

`pw-profiler --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.log</span>

- Profile a remote instance:

`pw-profiler --remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>

- Display help:

`pw-profiler --help`
