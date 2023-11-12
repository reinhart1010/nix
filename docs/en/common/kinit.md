---
layout: page
title: common/kinit (English)
description: "Authenticate a principal with a Kerberos server to gain and cache a ticket."
content_hash: 21395a3b8a65d54be94e475e97bee57279427430
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# kinit

Authenticate a principal with a Kerberos server to gain and cache a ticket.
Note: A Kerberos principal can be either a user, service, or application.
More information: <https://web.mit.edu/kerberos/krb5-1.12/doc/user/user_commands/kinit.html>.

- Authenticate a user and obtain a ticket-granting ticket:

`kinit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Renew a ticket-granting ticket:

`kinit -R`

- Specify a lifetime for the ticket:

`kinit -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5h</span>

- Specify a total renewable lifetime for the ticket:

`kinit -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1w</span>

- Specify a different principal name to authenticate as:

`kinit -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">principal@REALM</span>

- Specify a different keytab file to authenticate with:

`kinit -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/keytab</span>
