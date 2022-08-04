---
layout: page
title: common/ghdl (English)
description: "Open-source simulator for the VHDL language."
content_hash: 6683b8bc33553c310c1f8818c8d0fc9ef2614f23
related_topics:
  - title: français version
    url: /fr/common/ghdl.html
    icon: bi bi-globe
---
# ghdl

Open-source simulator for the VHDL language.
More information: <http://ghdl.free.fr>.

- Analyze a VHDL source file and produce an object file:

`ghdl -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.vhdl</span>

- Elaborate a design (where <span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">design</span> is the name of a configuration unit, entity unit or architecture unit):

`ghdl -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">design</span>

- Run an elaborated design:

`ghdl -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">design</span>

- Run an elaborated design and dump output to a waveform file:

`ghdl -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">design</span>` --wave=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.ghw</span>

- Check the syntax of a VHDL source file:

`ghdl -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.vhdl</span>

- Display the help page:

`ghdl --help`
