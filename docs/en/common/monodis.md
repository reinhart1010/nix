---
layout: page
title: common/monodis (English)
description: "The Mono Common Intermediate Language (CIL) disassembler."
content_hash: 9580017435b1d625bd5bd5603815a25233663b6a
last_modified_at: 2024-01-31
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

- List resources embedded within an assembly:

`monodis --manifest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/assembly.dll</span>

- Extract all the embedded resources to the current directory:

`monodis --mresources `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/assembly.dll</span>
