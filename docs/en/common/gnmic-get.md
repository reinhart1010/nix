---
layout: page
title: common/gnmic-get (English)
description: "Get a snapshot of a gnmi network device operation data."
content_hash: ecebbb530fed161dfa9b0d702b8ad149887fda20
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# gnmic get

Get a snapshot of a gnmi network device operation data.
More information: <https://gnmic.kmrd.dev/cmd/get>.

- Get a snapshot of the device state at a specific path:

`gnmic --address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip:port</span>` get --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path</span>

- Query the device state at multiple paths:

`gnmic -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip:port</span>` get --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1</span>` --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory2</span>

- Query the device state at multiple paths with a common prefix:

`gnmic -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip:port</span>` get --prefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>` --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1</span>` --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory2</span>

- Query the device state and specify response encoding (json_ietf):

`gnmic -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip:port</span>` get --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path</span>` --encoding json_ietf`
