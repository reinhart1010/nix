---
layout: page
title: common/httprobe (English)
description: "Take a list of domains and probe for working HTTP and HTTPS servers."
content_hash: 7ef2f11ca39f6635af6179b71b4853ec37b75a42
last_modified_at: 2023-11-12
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

- Output all available options:

`httprobe --help`
