---
layout: page
title: linux/pngcheck (English)
description: "Forensics tool for validating the integrity of PNG based (PNG, JNG, MNG) image files."
content_hash: eba569cad0701958a7c6e1e586b2bf0d5b2dc7b1
last_modified_at: 2024-03-14
tldri18n_status: 2
---
# pngcheck

Forensics tool for validating the integrity of PNG based (PNG, JNG, MNG) image files.
Can also extract embedded images and text from a file.
More information: <http://www.libpng.org/pub/png/apps/pngcheck.html>.

- Verify the integrity of an image file:

`pngcheck `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>

- Check the file with [v]erbose and [c]olorized output:

`pngcheck -vc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>

- Display contents of [t]ext chunks and [s]earch for PNGs within a specific file:

`pngcheck -ts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>

- Search for, and e[x]tract embedded PNGs within a specific file:

`pngcheck -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>
