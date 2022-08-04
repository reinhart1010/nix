---
layout: page
title: linux/postfix (English)
description: "Postfix mail transfer agent (MTA) control program."
content_hash: efa8ae12ee72f8523f64f2d50739c53d5baffc52
---
# postfix

Postfix mail transfer agent (MTA) control program.
See also `dovecot`, a mail delivery agent (MDA) that integrates with Postfix.
More information: <http://www.postfix.org>.

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
