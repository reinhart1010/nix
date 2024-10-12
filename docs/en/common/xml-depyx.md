---
layout: page
title: common/xml-depyx (English)
description: "Convert a PYX (ESIS - ISO 8879) document to XML format."
content_hash: 4e010ed3b9395f5c2c96868e2c81654e3b41409f
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# xml depyx

Convert a PYX (ESIS - ISO 8879) document to XML format.
More information: <https://xmlstar.sourceforge.net/docs.php>.

- Convert a PYX (ESIS - ISO 8879) document to XML format:

`xml depyx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pyx|URI</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.xml</span>

- Convert a PYX document from `stdin` to XML format:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pyx</span>` | xml depyx > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.xml</span>

- Display help:

`xml depyx --help`
