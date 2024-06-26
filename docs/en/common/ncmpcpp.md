---
layout: page
title: common/ncmpcpp (English)
description: "A music player client for the Music Player Daemon."
content_hash: 06549477736a1878aef4951c7927682164205fb2
last_modified_at: 2024-04-04
tldri18n_status: 2
---
# ncmpcpp

A music player client for the Music Player Daemon.
See also: `mpd`, `mpc`, `qmmp`, `termusic`.
More information: <https://rybczak.net/ncmpcpp>.

- Connect to a music player daemon on a given host and port:

`ncmpcpp --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Display metadata of the current song to console:

`ncmpcpp --current-song`

- Use a specified configuration file:

`ncmpcpp --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Use a different set of key bindings from a file:

`ncmpcpp --bindings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>
