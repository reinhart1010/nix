---
layout: page
title: common/chafa (English)
description: "Image printing in the terminal."
content_hash: 59243002330d37514e487ab736345301e66749eb
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# chafa

Image printing in the terminal.
See also: `catimg`, `pixterm`.
More information: <https://hpjansson.org/chafa>.

- Render an image directly in the terminal:

`chafa `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Render an image with 24-bit [c]olor:

`chafa -c full `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Improve image rendering with small color palettes using dithering:

`chafa -c 16 --dither ordered `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Render an image, making it appear pixelated:

`chafa --symbols vhalf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Render a monochrome image with only braille characters:

`chafa -c none --symbols braille `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
