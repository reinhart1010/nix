---
layout: page
title: common/prosodyctl (English)
description: "The control tool for the Prosody XMPP server."
content_hash: db2a912eb196417cb1c812e25d724f14ffa1df3c
---
# prosodyctl

The control tool for the Prosody XMPP server.
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
