---
layout: page
title: common/xml (English)
description: "XMLStarlet Toolkit: Query, edit, check, convert and transform XML documents."
content_hash: 2779593486d438d0f7b9a7d8d69e12b1ef74d932
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# xml

XMLStarlet Toolkit: Query, edit, check, convert and transform XML documents.
This command also has documentation about its subcommands, e.g. `xml validate`.
More information: <http://xmlstar.sourceforge.net/docs.php>.

- Display general help, including the list of subcommands:

`xml --help`

- Execute a subcommand with input from a file or URI, printing to `stdout`:

`xml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">options</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml|URI</span>

- Execute a subcommand using `stdin` and `stdout`:

`xml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">options</span>

- Execute a subcommand with input from a file or URI and output to a file:

`xml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">options</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml|URI</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output</span>

- Display help for a subcommand:

`xml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` --help`

- Display the version of the XMLStarlet Toolkit:

`xml --version`
