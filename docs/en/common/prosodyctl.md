---
layout: page
title: common/prosodyctl (English)
description: "The control tool for the Prosody XMPP server."
content_hash: 0fdfc116e5a36786711d64cd26048fc7a62400a4
last_modified_at: 2024-01-26
tldri18n_status: 2
---
# prosodyctl

The control tool for the Prosody XMPP server.
NOTE: process management through `prosodyctl` is discouraged. Instead, use the tools provided by your system (e.g. `systemctl`).
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
