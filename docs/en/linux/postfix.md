---
layout: page
title: linux/postfix (English)
description: "Postfix mail transfer agent (MTA) control program."
content_hash: d2c221b398628a86cec7faf3375669c0d9abb21d
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# postfix

Postfix mail transfer agent (MTA) control program.
See also `dovecot`, a mail delivery agent (MDA) that integrates with Postfix.
More information: <https://www.postfix.org>.

- Check the configuration:

`sudo postfix check`

- Check the status of the Postfix daemon:

`sudo postfix status`

- Start Postfix:

`sudo postfix start`

- Gracefully stop Postfix:

`sudo postfix stop`

- Flush the mail queue:

`sudo postfix flush`

- Reload the configuration files:

`sudo postfix reload`
