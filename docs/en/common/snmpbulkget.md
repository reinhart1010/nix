---
layout: page
title: common/snmpbulkget (English)
description: "Query the next value in the MIB tree and all of its adjacent values."
content_hash: c872a2d8743c7c0acdb0aa4e4c712d6c634b5b32
last_modified_at: 2025-03-02
tldri18n_status: 2
---
# snmpbulkget

Query the next value in the MIB tree and all of its adjacent values.
More information: <https://manned.org/snmpbulkget>.

- Request the next value from the SNMP agent:

`snmpbulkget -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">community</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">oid</span>

- Display the full Object Identifier (OID) path:

`snmpbulkget -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">community</span>` -O f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">oid</span>
