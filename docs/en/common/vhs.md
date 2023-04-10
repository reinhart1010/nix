---
layout: page
title: common/vhs (English)
description: "CLI home video recorder to generate terminal gifs from code."
content_hash: f6a7b3a2b59884b252aa4ef19a310dc6de73ec69
last_modified_at: 2023-04-10
---
# vhs

CLI home video recorder to generate terminal gifs from code.
More information: <https://github.com/charmbracelet/vhs>.

- Create a tape file (Add commands to the tap file using your editor):

`vhs new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tape</span>

- Record inputs to a tape file (Once done, exit the shell to create the tape):

`vhs record > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tape</span>

- Record inputs to a tape file using a specific shell:

`vhs record --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tape</span>

- Validate a type file's syntax:

`vhs validate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tape</span>

- Create a gif from a tape file:

`vhs < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tape</span>

- Publish a gif to https://vhs.charm.sh and get a shareable URL:

`vhs publish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.gif</span>
