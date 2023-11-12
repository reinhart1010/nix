---
layout: page
title: common/nokogiri (English)
description: "An HTML, XML, SAX and Reader parser."
content_hash: cee175e78480ec5e81a88a252b4a6cbcee93d23e
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# nokogiri

An HTML, XML, SAX and Reader parser.
More information: <https://nokogiri.org>.

- Parse the contents of a URL or file:

`nokogiri `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|path/to/file</span>

- Parse as a specific type:

`nokogiri `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|path/to/file</span>` --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xml|html</span>

- Load a specific initialization file before parsing:

`nokogiri `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|path/to/file</span>` -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config_file</span>

- Parse using a specific encoding:

`nokogiri `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|path/to/file</span>` --encoding `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encoding</span>

- Validate using a RELAX NG file:

`nokogiri `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|path/to/file</span>` --rng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|path/to/file</span>
