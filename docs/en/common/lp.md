---
layout: page
title: common/lp (English)
description: "Print files."
content_hash: b851c0e51cbdf142cc69e5f2f346927875e4d506
---
# lp

Print files.
More information: <https://manned.org/lp>.

- Print the output of a command to the default printer (see `lpstat` command):

`echo "test" | lp`

- Print a file to the default printer:

`lp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filename</span>

- Print a file to a named printer (see `lpstat` command):

`lp -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">printer_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filename</span>

- Print N copies of file to default printer (replace N with desired number of copies):

`lp -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filename</span>

- Print only certain pages to the default printer (print pages 1, 3-5, and 16):

`lp -P 1,3-5,16 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filename</span>

- Resume printing a job:

`lp -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>` -H resume`
