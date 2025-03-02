---
layout: page
title: common/snmpget (English)
description: "Query using the SNMP protocol."
content_hash: 6453d76a4c54c74e2e917a363de7f7da4d991716
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/common/snmpget.html
    icon: bi bi-globe
tldri18n_status: 2
---
# snmpget

Query using the SNMP protocol.
More information: <https://manned.org/snmpget>.

- Request a single value from the SNMP agent:

`snmpget -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">community</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">oid</span>

- Display the full Object Identifier (OID) path:

`snmpget -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">community</span>` -O f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">oid</span>
