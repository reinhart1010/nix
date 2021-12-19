---
layout: page
title: common/nokogiri (English)
description: "An HTML, XML, SAX and Reader parser."
content_hash: 02222761ae65f4b66d49b90b04c6247efa2157d0
---
# nokogiri

An HTML, XML, SAX and Reader parser.
More information: <https://nokogiri.org>.

- Parse the contents of a URL or file:

`nokogiri `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|path/to/file</span>

- Parse as a specific type:

`nokogiri `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|path/to/file</span>` --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xml|html</span>

- Load a specific initialisation file before parsing:

`nokogiri `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|path/to/file</span>` -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config_file</span>

- Parse using a specific encoding:

`nokogiri `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|path/to/file</span>` --encoding `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encoding</span>

- Validate using a RELAX NG file:

`nokogiri `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|path/to/file</span>` --rng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|path/to/file</span>
