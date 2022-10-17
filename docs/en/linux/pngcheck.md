---
layout: page
title: linux/pngcheck (English)
description: "Forensics tool for validating the integrity of PNG based (`.png`, `.jng`, `.mng`) image files."
content_hash: 44e8c426ea561fff99e233fee3f3d75f1157f6ae
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pngcheck

Forensics tool for validating the integrity of PNG based (`.png`, `.jng`, `.mng`) image files.
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
