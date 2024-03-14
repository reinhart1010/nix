---
layout: page
title: linux/pw-profiler (English)
description: "Profile a local or remote instance."
content_hash: 43f7d03fcbc9f6ad188cd051ab436f1022d78590
last_modified_at: 2024-03-14
tldri18n_status: 2
---
# pw-profiler

Profile a local or remote instance.
More information: <https://docs.pipewire.org/page_man_pw-profiler_1.html>.

- Profile the default instance, logging to `profile.log` (`gnuplot` files and a HTML file for result visualizing are also generated):

`pw-profiler`

- Change the log output file:

`pw-profiler --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.log</span>

- Profile a remote instance:

`pw-profiler --remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>

- Display help:

`pw-profiler --help`
