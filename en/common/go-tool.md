---
layout: page
title: common/go-tool (English)
description: "Run a specific Go tool or command."
content_hash: 076a67b38ad8aba7b0af3496141c8f7ef43bffc9
---
# go tool

Run a specific Go tool or command.
Execute a Go command as a stand-alone binary, typically for debugging.
More information: <https://pkg.go.dev/cmd/go#hdr-Run_specified_go_tool>.

- List available tools:

`go tool`

- Run the go link tool:

`go tool link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/main.o</span>

- Print the command that would be executed, but do not execute it (similar to `whereis`):

`go tool -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arguments</span>

- Display documentation for a specified tool:

`go tool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` --help`
