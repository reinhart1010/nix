---
layout: page
title: common/xonsh (English)
description: "Python-powered, cross-platform, Unix-gazing shell."
content_hash: 8eb90e11fb13dd99fe3625da5ab57b9a319f17ba
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# xonsh

Python-powered, cross-platform, Unix-gazing shell.
Write and mix sh/Python code in Xonsh (pronounced conch).
More information: <https://xon.sh>.

- Start an interactive shell session:

`xonsh`

- Execute a single command and then exit:

`xonsh -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`

- Run commands from a script file and then exit:

`xonsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script_file.xonsh</span>

- Define environment variables for the shell process:

`xonsh -D`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name1</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value1</span>` -D`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name2</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value2</span>

- Load the specified `.xonsh` or `.json` configuration files:

`xonsh --rc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.xonsh</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2.json</span>

- Skip loading the `.xonshrc` configuration file:

`xonsh --no-rc`
