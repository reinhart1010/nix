---
layout: page
title: common/vhs (English)
description: "Generate terminal gifs from a tape file."
content_hash: 9126a699956bd156a15618de0908dcdaa2d3b975
last_modified_at: 2023-07-16
---
# vhs

Generate terminal gifs from a tape file.
More information: <https://github.com/charmbracelet/vhs>.

- Create a tape file (add commands to the tape file using an editor):

`vhs new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tape</span>

- Record inputs to a tape file (once done, exit the shell to create the tape):

`vhs record > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tape</span>

- Record inputs to a tape file using a specific shell:

`vhs record --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tape</span>

- Validate the syntax of a tape file:

`vhs validate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tape</span>

- Create a gif from a tape file:

`vhs < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tape</span>

- Publish a gif to <https://vhs.charm.sh> and get a shareable URL:

`vhs publish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.gif</span>
