---
layout: page
title: common/xml-depyx (English)
description: "Convert a PYX (ESIS - ISO 8879) document to XML format."
content_hash: dcc41cb546e6583f3e879ad968d5776d53cf7bc3
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# xml depyx

Convert a PYX (ESIS - ISO 8879) document to XML format.
More information: <http://xmlstar.sourceforge.net/docs.php>.

- Convert a PYX (ESIS - ISO 8879) document to XML format:

`xml depyx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pyx|URI</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.xml</span>

- Convert a PYX document from `stdin` to XML format:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pyx</span>` | xml depyx > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.xml</span>

- Display help:

`xml depyx --help`
