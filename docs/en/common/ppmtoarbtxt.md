---
layout: page
title: common/ppmtoarbtxt (English)
description: "Convert a PPM image to an arbitrary text format according to a template."
content_hash: 8317ba1113911ac5c0967f5e3027d7bbabf4ca8e
last_modified_at: 2023-11-07
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ppmtoarbtxt

Convert a PPM image to an arbitrary text format according to a template.
More information: <https://netpbm.sourceforge.net/doc/ppmtoarbtxt.html>.

- Convert a PPM image to text as specified by the given template:

`ppmtoarbtxt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/template</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.txt</span>

- Convert a PPM image to text as specified by the given template, prepend the contents of the specified head template:

`ppmtoarbtxt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/template</span>` -hd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/head_template</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.txt</span>

- Convert a PPM image to text as specified by the given template, append the contents of the specified tail template:

`ppmtoarbtxt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/template</span>` -hd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/tail_template</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.txt</span>

- Display version:

`ppmtoarbtxt -version`
