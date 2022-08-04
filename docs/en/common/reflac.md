---
layout: page
title: common/reflac (English)
description: "Recompress FLAC files in-place while preserving metadata."
content_hash: 6af3e039bae9fe4ce58ee97f656ee3b36d68a809
---
# reflac

Recompress FLAC files in-place while preserving metadata.
More information: <https://github.com/chungy/reflac>.

- Recompress a directory of FLAC files:

`reflac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Enable maximum compression (very slow):

`reflac --best `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Display filenames as they are processed:

`reflac --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Recurse into subdirectories:

`reflac --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Preserve file modification times:

`reflac --preserve `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
