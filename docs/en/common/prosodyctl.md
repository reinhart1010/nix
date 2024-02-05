---
layout: page
title: common/prosodyctl (English)
description: "The control tool for the Prosody XMPP server."
content_hash: 2617e9d63220ce5ba6769601ccd1b660c9782c9c
last_modified_at: 2024-02-05
tldri18n_status: 2
---
# prosodyctl

The control tool for the Prosody XMPP server.
Note: process management through `prosodyctl` is discouraged. Instead, use the tools provided by your system (e.g. `systemctl`).
More information: <https://prosody.im/doc/prosodyctl>.

- Show the status of the Prosody server:

`sudo prosodyctl status`

- Reload the server's configuration files:

`sudo prosodyctl reload`

- Add a user to the Prosody XMPP server:

`sudo prosodyctl adduser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user@example.com</span>

- Set a user's password:

`sudo prosodyctl passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user@example.com</span>

- Permanently delete a user:

`sudo prosodyctl deluser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user@example.com</span>
