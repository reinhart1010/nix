---
layout: page
title: common/ffe (English)
description: "Extract fields from a flat database file and write to another format."
content_hash: ff61d332b2b2dc1305f859458f1d5f881bb2e4be
last_modified_at: 2024-01-25
tldri18n_status: 2
---
# ffe

Extract fields from a flat database file and write to another format.
A configuration file is required to interpret the input and format the output.
More information: <http://ff-extractor.sourceforge.net/ffe.html>.

- Display all input data using the specified data configuration:

`ffe --configuration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.ffe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input</span>

- Convert an input file to an output file in a new format:

`ffe --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.ffe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input</span>

- Select input structure and print format from definitions in `~/.fferc` configuration file:

`ffe --structure=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">structure</span>` --print=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">format</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input</span>

- Write only the selected fields:

`ffe --field-list="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FirstName,LastName,Age</span>`" -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.ffe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input</span>

- Write only the records that match an expression:

`ffe -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">LastName=Smith</span>`" -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.ffe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input</span>

- Display help:

`ffe --help`
