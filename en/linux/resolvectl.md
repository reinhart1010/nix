---
layout: page
title: linux/resolvectl (English)
description: "Resolve domain names, IPV4 and IPv6 addresses, DNS resource records, and services."
content_hash: 2b15c9aa1d5e765d15331ae9bc6c09476d47f1e2
---
# resolvectl

Resolve domain names, IPV4 and IPv6 addresses, DNS resource records, and services.
Introspect and reconfigure the DNS resolver.
More information: <https://www.freedesktop.org/software/systemd/man/resolvectl.html>.

- Show DNS settings:

`resolvectl status`

- Resolve the IPv4 and IPv6 addresses for one or more domains:

`resolvectl query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain1 domain2 ...</span>

- Retrieve the domain of a specified IP:

`resolvectl query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>

- Retrieve an MX record of domain:

`resolvectl --legend=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">no</span>` --type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MX</span>` query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain</span>

- Resolve an SRV record, for example _xmpp-server._tcp gmail.com:

`resolvectl service _`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service</span>`._`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">protocol</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Retrieve the public key from an email address from an OPENPGPKEY DNS record:

`resolvectl opengpg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email</span>

- Retrieve a TLS key:

`resolvectl tlsa tcp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain</span>`:443`
