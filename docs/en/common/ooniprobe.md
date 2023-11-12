---
layout: page
title: common/ooniprobe (English)
description: "Open Observatory of Network Interference (OONI)."
content_hash: 21e1c79809d7846b970d62c9458fdc3c68c007db
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# ooniprobe

Open Observatory of Network Interference (OONI).
Test the blocking of websites and apps. Measure the speed and performance of your network.
More information: <https://ooni.org/support/ooni-probe-cli/>.

- List all tests performed:

`ooniprobe list`

- Show information about a specific test:

`ooniprobe list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>

- Run all available tests:

`ooniprobe run all`

- Perform a specific test:

`ooniprobe run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">performance</span>

- Check the availability of a specific website:

`ooniprobe run websites --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://ooni.org/</span>

- Check the availability of all websites listed in a file:

`ooniprobe run websites --input-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/my-websites.txt</span>

- Display detailed information about a test in JSON format:

`ooniprobe show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9</span>
