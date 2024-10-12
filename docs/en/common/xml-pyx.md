---
layout: page
title: common/xml-pyx (English)
description: "Convert an XML document to PYX (ESIS - ISO 8879) format."
content_hash: aa6cc449a4f1b4b8b0a353040cd1f81cc76ca150
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# xml pyx

Convert an XML document to PYX (ESIS - ISO 8879) format.
More information: <https://xmlstar.sourceforge.net/docs.php>.

- Convert an XML document to PYX format:

`xml pyx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml|URI</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pyx</span>

- Convert an XML document from `stdin` to PYX format:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml</span>` | xml pyx > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pyx</span>

- Display help:

`xml pyx --help`
