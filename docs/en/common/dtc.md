---
layout: page
title: common/dtc (English)
description: "The Device Tree Compiler, a tool for recompiling device trees between formats."
content_hash: f5173bf3eaa3d6cc0ddae6c76036cd48b7284f6d
last_modified_at: 2024-09-28
tldri18n_status: 2
---
# dtc

The Device Tree Compiler, a tool for recompiling device trees between formats.
More information: <https://github.com/dgibson/dtc>.

- Decompile a `.dtb` file into a readable `.dts` file:

`dtc -I dtb -O dts -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.dts</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.dtb</span>
