---
layout: page
title: common/syncthing (English)
description: "Continuous bidirectional decentralised folder synchronisation tool."
content_hash: 6b2b755a9adce723045b150d334fb698cf49f11c
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# syncthing

Continuous bidirectional decentralised folder synchronisation tool.
More information: <https://docs.syncthing.net/>.

- Start Syncthing:

`syncthing`

- Start Syncthing without opening a web browser:

`syncthing -no-browser`

- Print the device ID:

`syncthing -device-id`

- Change the home directory:

`syncthing -home=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Force a full index exchange:

`syncthing -reset-deltas`

- Change the address upon which the web interface listens:

`syncthing -gui-address=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address:port|path/to/socket.sock</span>

- Show filepaths to the files used by Syncthing:

`syncthing -paths`

- Disable the Syncthing monitor process:

`syncthing -no-restart`
