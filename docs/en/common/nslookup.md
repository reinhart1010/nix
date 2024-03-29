---
layout: page
title: common/nslookup (English)
description: "Query name servers for various domain records."
content_hash: b9e008a3f6a61e580d44c106627c34be0b6d05a9
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# nslookup

Query name servers for various domain records.
More information: <https://manned.org/nslookup>.

- Query your system's default name server for an IP address (A record) of the domain:

`nslookup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Query a given name server for a NS record of the domain:

`nslookup -type=NS `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>

- Query for a reverse lookup (PTR record) of an IP address:

`nslookup -type=PTR `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">54.240.162.118</span>

- Query for ANY available records using TCP protocol:

`nslookup -vc -type=ANY `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Query a given name server for the whole zone file (zone transfer) of the domain using TCP protocol:

`nslookup -vc -type=AXFR `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name_server</span>

- Query for a mail server (MX record) of the domain, showing details of the transaction:

`nslookup -type=MX -debug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Query a given name server on a specific port number for a TXT record of the domain:

`nslookup -port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_number</span>` -type=TXT `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name_server</span>
