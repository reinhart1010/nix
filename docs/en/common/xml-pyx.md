---
layout: page
title: common/xml-pyx (English)
description: "Convert an XML document to PYX (ESIS - ISO 8879) format."
content_hash: 23023e31eacbfb160396ace3c10d712987977fa8
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# xml pyx

Convert an XML document to PYX (ESIS - ISO 8879) format.
More information: <http://xmlstar.sourceforge.net/docs.php>.

- Convert an XML document to PYX format:

`xml pyx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml|URI</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pyx</span>

- Convert an XML document from `stdin` to PYX format:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml</span>` | xml pyx > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pyx</span>

- Display help:

`xml pyx --help`
