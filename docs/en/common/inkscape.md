---
layout: page
title: common/inkscape (English)
description: "An SVG (Scalable Vector Graphics) editing program."
content_hash: a52cc5bd03d04a3aa9b32ecd52f99c3df5899a57
related_topics:
  - title: Nederlands version
    url: /nl/common/inkscape.html
    icon: bi bi-globe
---
# inkscape

An SVG (Scalable Vector Graphics) editing program.
For Inkscape versions up to 0.92.x, use -e instead of -o.
More information: <https://inkscape.org>.

- Open an SVG file in the Inkscape GUI:

`inkscape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.svg</span>

- Export an SVG file into a bitmap with the default format (PNG) and the default resolution (96 DPI):

`inkscape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.svg</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.png</span>

- Export an SVG file into a bitmap of 600x400 pixels (aspect ratio distortion may occur):

`inkscape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.svg</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.png</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">600</span>` -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">400</span>

- Export the drawing (bounding box of all objects) of an SVG file into a bitmap:

`inkscape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.svg</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.png</span>` -D`

- Export a single object, given its ID, into a bitmap:

`inkscape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.svg</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">object.png</span>

- Export an SVG document to PDF, converting all texts to paths:

`inkscape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.svg</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.pdf</span>` --export-text-to-path`

- Duplicate the object with id="path123", rotate the duplicate 90 degrees, save the file, and quit Inkscape:

`inkscape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.svg</span>` --select=path123 --verb="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">EditDuplicate;ObjectRotate90;FileSave;FileQuit</span>`"`
