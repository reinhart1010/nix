---
layout: page
title: common/snmpgetnext (English)
description: "Query the next value in the MIB tree."
content_hash: f9344f703b76450db92736724f59d6e20b1ea58b
last_modified_at: 2025-03-02
tldri18n_status: 2
---
# snmpgetnext

Query the next value in the MIB tree.
More information: <https://manned.org/snmpgetnext>.

- Request the next value from the SNMP agent:

`snmpget -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">community</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">oid</span>

- Display the full Object Identifier (OID) path:

`snmpget -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">community</span>` -O f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">oid</span>
