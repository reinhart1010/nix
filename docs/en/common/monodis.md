---
layout: page
title: common/monodis (English)
description: "The Mono Common Intermediate Language (CIL) disassembler."
content_hash: 88f32a9532b9ec017e57a12459c8ad107b1aeacc
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# monodis

The Mono Common Intermediate Language (CIL) disassembler.
More information: <https://www.mono-project.com/docs/tools+libraries/tools/monodis/>.

- Disassemble an assembly to textual CIL:

`monodis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/assembly.exe</span>

- Save the output to a file:

`monodis --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.il</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/assembly.exe</span>

- Show information about an assembly:

`monodis --assembly `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/assembly.dll</span>

- List the references of an assembly:

`monodis --assemblyref `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/assembly.exe</span>

- List all the methods in an assembly:

`monodis --method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/assembly.exe</span>

- Show a list of resources embedded within an assembly:

`monodis --manifest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/assembly.dll</span>

- Extract all the embedded resources to the current directory:

`monodis --mresources `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/assembly.dll</span>
