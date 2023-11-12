---
layout: page
title: common/tailscale-file (English)
description: "Send files across connected devices on a Tailscale network."
content_hash: 728491001aecbf98bdd3a2be0f3a767e6d442bed
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# tailscale file

Send files across connected devices on a Tailscale network.
It currently does not support sending files to devices owned by other users even on the same Tailscale network.
More information: <https://tailscale.com/kb/1106/taildrop/>.

- Send a file to a specific node:

`sudo tailscale file cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname|ip</span>`:`

- Store files that were sent to the current node into a specific directory:

`sudo tailscale file get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
