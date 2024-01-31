---
layout: page
title: common/xsv (English)
description: "A CSV command-line toolkit written in Rust."
content_hash: eb25f7045bd99f73d5be9d4c9cfb386ad86459bb
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# xsv

A CSV command-line toolkit written in Rust.
More information: <https://github.com/BurntSushi/xsv>.

- Inspect the headers of a file:

`xsv headers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.csv</span>

- Count the number of entries:

`xsv count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.csv</span>

- Get an overview of the shape of entries:

`xsv stats `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.csv</span>` | xsv table`

- Select a few columns:

`xsv select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">column1,column2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.csv</span>

- Show 10 random entries:

`xsv sample `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.csv</span>

- Join a column from one file to another:

`xsv join --no-case `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">column1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.csv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">column2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2.csv</span>` | xsv table`
