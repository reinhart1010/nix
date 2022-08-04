---
layout: page
title: common/dua (English)
description: "Dua (Disk Usage Analyzer) is a tool to conveniently learn about the usage of disk space of a given directory."
content_hash: afa100c831ec864f8ae32f32f3580d15fb2e305f
---
# dua

Dua (Disk Usage Analyzer) is a tool to conveniently learn about the usage of disk space of a given directory.
More information: <https://github.com/Byron/dua-cli>.

- Analyze specific directory:

`dua `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Display apparent size instead of disk usage:

`dua --apparent-size`

- Count hard-linked files each time they are seen:

`dua --count-hard-links`

- Aggregate the consumed space of one or more directories or files:

`dua aggregate`

- Launch the terminal user interface:

`dua interactive`

- Format printing byte counts:

`dua --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">metric|binary|bytes|GB|GiB|MB|MiB</span>

- Set the number of threads to be used:

`dua --threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>
