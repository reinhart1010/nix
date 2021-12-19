---
layout: page
title: common/luac (English)
description: "Lua bytecode compiler."
content_hash: efdd88175949181c531ace67692c6e98b17a2a6b
---
# luac

Lua bytecode compiler.
More information: <https://www.lua.org>.

- Compile a Lua source file to Lua bytecode:

`luac -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">byte_code.luac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.lua</span>

- Do not include debug symbols in the output:

`luac -s -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">byte_code.luac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.lua</span>
