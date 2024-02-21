---
layout: page
title: common/gocr (English)
description: "Optical Character Recognition tool."
content_hash: 4088c3ce1187d1a2e2ece8512d08a89df0b56360
last_modified_at: 2024-02-21
tldri18n_status: 2
---
# gocr

Optical Character Recognition tool.
Recognize characters using its engine, and prompt the user for unknown patterns to store them in a database.
More information: <https://manned.org/gocr.1>.

- Recognize characters in the [i]nput image and [o]utput it in the given file. Put the database ([p]) in `path/to/db_directory` (verify that the folder exists or DB usage will silently be skipped). [m]ode 130 means create + use + extend database:

`gocr -m 130 -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/db_directory</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_image.png</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.txt</span>

- Recognize characters and assume all [C]haracters are numbers:

`gocr -m 130 -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/db_directory</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_image.png</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.txt</span>` -C "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0..9</span>`"`

- Recognize characters with a cert[a]inty of 100% (characters have a higher chance to be treated as unknown):

`gocr -m 130 -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/db_directory</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_image.png</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.txt</span>` -a 100`
