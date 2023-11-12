---
layout: page
title: common/zeisstopnm (English)
description: "Convert a Zeiss confocal file to Netbpm format."
content_hash: e5372c5f613b5b50d96e1435e57da644c2e3a069
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# zeisstopnm

Convert a Zeiss confocal file to Netbpm format.
More information: <https://manned.org/zeisstopnm.1>.

- Convert a Zeiss cofocal file into either `.pgm` or `.ppm` format:

`zeisstopnm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Convert a Zeiss cofocal file to Netbpm format while explicitly specifying the target file type:

`zeisstopnm -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pgm|ppm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
