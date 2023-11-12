---
layout: page
title: common/jp2a (English)
description: "Convert JPEG images to ASCII."
content_hash: 32c2ca9fc9c18ca3a95b970e2fffa5233eace74e
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# jp2a

Convert JPEG images to ASCII.
More information: <https://csl.name/jp2a/>.

- Read JPEG image from a file and print in ASCII:

`jp2a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.jpeg</span>

- Read JPEG image from a URL and print in ASCII:

`jp2a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.example.com/image.jpeg</span>

- Colorize the ASCII output:

`jp2a --colors `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.jpeg</span>

- Specify characters to be used for the ASCII output:

`jp2a --chars='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">..-ooxx@@</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.jpeg</span>

- Write the ASCII output into a file:

`jp2a --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.jpeg</span>

- Write the ASCII output in HTML file format, suitable for viewing in web browsers:

`jp2a --html --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.jpeg</span>
