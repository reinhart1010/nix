---
layout: page
title: common/xml-pyx (English)
description: "Convert an XML document to PYX (ESIS - ISO 8879) format."
content_hash: f87fb1fe7e0c56093fd2f21f9ba55c04c2e9a20a
last_modified_at: 2022-12-04
---
# xml pyx

Convert an XML document to PYX (ESIS - ISO 8879) format.
More information: <http://xmlstar.sourceforge.net/docs.php>.

- Convert an XML document to PYX format:

`xml pyx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml|URI</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pyx</span>

- Convert an XML document from `stdin` to PYX format:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml</span>` | xml pyx > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pyx</span>

- Display help for the `pyx` subcommand:

`xml pyx --help`
