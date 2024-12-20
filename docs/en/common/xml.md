---
layout: page
title: common/xml (English)
description: "XMLStarlet Toolkit: query, edit, check, convert and transform XML documents."
content_hash: 996ee123f286a29c56d3dfa14a1b0ad47d06c4c2
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# xml

XMLStarlet Toolkit: query, edit, check, convert and transform XML documents.
Some subcommands such as `xml validate` have their own usage documentation.
More information: <https://xmlstar.sourceforge.net/docs.php>.

- Display general help, including the list of subcommands:

`xml --help`

- Execute a subcommand with input from a file or URI, printing to `stdout`:

`xml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">options</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml|URI</span>

- Execute a subcommand using `stdin` and `stdout`:

`xml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">options</span>

- Execute a subcommand with input from a file or URI and output to a file:

`xml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">options</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml|URI</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output</span>

- Display help for a specific subcommand:

`xml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` --help`

- Display version:

`xml --version`
