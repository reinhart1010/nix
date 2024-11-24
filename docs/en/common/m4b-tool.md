---
layout: page
title: common/m4b-tool (English)
description: "Merge, split, and manipulate audiobook files with chapters."
content_hash: 246afa591934850998f6d1d351af80a31c6c3004
last_modified_at: 2024-11-24
tldri18n_status: 2
---
# m4b-tool

Merge, split, and manipulate audiobook files with chapters.
More information: <https://github.com/sandreas/m4b-tool>.

- Create an audiobook with the audio files in the input directory:

`m4b-tool merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_directory</span>` --output-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/merged.m4b</span>

- Make chapters using the input files' names:

`m4b-tool merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_directory</span>` --output-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/merged.m4b</span>` --use-filenames-as-chapters`
