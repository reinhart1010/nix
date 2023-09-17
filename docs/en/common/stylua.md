---
layout: page
title: common/stylua (English)
description: "An opinionated Lua code formatter."
content_hash: 32f639bd0cd545497f7f914f26ed0a30c58b0a4d
last_modified_at: 2023-09-17
---
# stylua

An opinionated Lua code formatter.
More information: <https://github.com/JohnnyMorganz/StyLua>.

- Auto-format a file or an entire directory:

`stylua `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Check if a specific file has been formatted:

`stylua --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Run with a specific configuration file:

`stylua --config-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Format code from `stdin` and output to `stdout`:

`stylua - < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.lua</span>

- Format a file or directory using spaces and preferring single quotes:

`stylua --indent-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Spaces</span>` --quote-style `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AutoPreferSingle</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>
