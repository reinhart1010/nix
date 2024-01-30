---
layout: page
title: common/httprobe (English)
description: "Take a list of domains and probe for working HTTP and HTTPS servers."
content_hash: 8435fe6bac2ef8ba2885169ad1bc0a8af4c42d7f
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# httprobe

Take a list of domains and probe for working HTTP and HTTPS servers.
More information: <https://github.com/tomnomnom/httprobe>.

- Probe a list of domains from a text file:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file</span>` | httprobe`

- Only check for HTTP if HTTPS is not working:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file</span>` | httprobe --prefer-https`

- Probe additional ports with a given protocol:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file</span>` | httprobe -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https:2222</span>

- Display help:

`httprobe --help`
