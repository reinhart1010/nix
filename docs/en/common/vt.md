---
layout: page
title: common/vt (English)
description: "Command-line interface for VirusTotal."
content_hash: 6ad81c85d75c9e5bb0bee788dec820c9bd409c0b
last_modified_at: 2024-03-14
related_topics:
  - title: தமிழ் version
    url: /ta/common/vt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vt

Command-line interface for VirusTotal.
API key from a VirusTotal account is required for this command.
More information: <https://github.com/VirusTotal/vt-cli>.

- Scan a specific file for viruses:

`vt scan file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Scan a URL for viruses:

`vt scan url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Display information from a specific analysis:

`vt analysis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_id|analysis_id</span>

- Download files in encrypted Zip format (requires premium account):

`vt download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_id</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --zip --zip-password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Initialize or re-initialize `vt` to enter API key interactively:

`vt init`

- Display information about a domain:

`vt domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Display information for a specific URL:

`vt url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Display information for a specific IP address:

`vt domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>
