---
layout: page
title: common/shotcut (English)
description: "A program for video editing."
content_hash: faa53d1b5f8e273673e7315bbfb47b4ea45e7b1c
last_modified_at: 2024-10-06
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/shotcut.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># shotcut

A program for video editing.
More information: <https://shotcut.org/notes/command-line-options/>.

- Start Shotcut:

`shotcut`

- Open audio/video files:

`shotcut `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Start with a specific audio driver:

`shotcut --SDL_AUDIODRIVER "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pulseaudio</span>`"`

- Start in fullscreen:

`shotcut --fullscreen`

- Start with GPU processing:

`shotcut --gpu`
