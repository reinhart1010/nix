---
layout: page
title: common/ghdl (English)
description: "Open-source simulator for the VHDL language."
content_hash: 0a60b9a8a81c3a65cfbc11d472cb71b4ce4e40cb
last_modified_at: 2024-01-30
related_topics:
  - title: français version
    url: /fr/common/ghdl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ghdl

Open-source simulator for the VHDL language.
More information: <http://ghdl.free.fr>.

- Analyze a VHDL source file and produce an object file:

`ghdl -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.vhdl</span>

- Elaborate a design (where `design` is the name of a configuration unit, entity unit or architecture unit):

`ghdl -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">design</span>

- Run an elaborated design:

`ghdl -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">design</span>

- Run an elaborated design and dump output to a waveform file:

`ghdl -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">design</span>` --wave=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.ghw</span>

- Check the syntax of a VHDL source file:

`ghdl -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.vhdl</span>

- Display help:

`ghdl --help`
