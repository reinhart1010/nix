---
layout: page
title: common/xargs (English)
description: "Execute a command with piped arguments coming from another command, a file, etc."
content_hash: cfe731366607536e34f4f98a6bf78b00c0db4084
last_modified_at: 2024-06-26
tldri18n_status: 2
---
# xargs

Execute a command with piped arguments coming from another command, a file, etc.
The input is treated as a single block of text and split into separate pieces on spaces, tabs, newlines and end-of-file.
More information: <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/xargs.html>.

- Run a command using the input data as arguments:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arguments_source</span>` | xargs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Run multiple chained commands on the input data:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arguments_source</span>` | xargs sh -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command1</span>` && `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command2</span>` | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command3</span>`"`

- Delete all files with a `.backup` extension (`-print0` uses a null character to split file names, and `-0` uses it as delimiter):

`find . -name '*.backup' -print0 | xargs -0 rm -v`

- Execute the command once for each input line, replacing any occurrences of the placeholder (here marked as `_`) with the input line:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arguments_source</span>` | xargs -I _ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` _ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">optional_extra_arguments</span>

- Parallel runs of up to `max-procs` processes at a time; the default is 1. If `max-procs` is 0, xargs will run as many processes as possible at a time:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arguments_source</span>` | xargs -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">max-procs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
