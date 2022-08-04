---
layout: page
title: common/gnucash-cli (English)
description: "A command-line version of GnuCash."
content_hash: c54a4faa4414336f2df880668abf1483c17bb039
---
# gnucash-cli

A command-line version of GnuCash.
More information: <https://gnucash.org>.

- Get quotes for currencies and stocks specified in a file and print them:

`gnucash-cli --quotes get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.gnucash</span>

- Generate a financial report of a specific type, specified by `--name`:

`gnucash-cli --report run --name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Balance Sheet</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.gnucash</span>
