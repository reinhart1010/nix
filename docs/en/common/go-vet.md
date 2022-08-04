---
layout: page
title: common/go-vet (English)
description: "Check Go source code and report suspicious constructs (e.g. lint your Go source files)."
content_hash: 8f92c524d90bccebff4160947d85d92a4387f216
---
# go vet

Check Go source code and report suspicious constructs (e.g. lint your Go source files).
Go vet returns a non-zero exit code if problems are found; returns a zero exit code if no problems are found.
More information: <https://pkg.go.dev/cmd/vet>.

- Check the Go package in the current directory:

`go vet`

- Check the Go package in the specified path:

`go vet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- List available checks that can be run with go vet:

`go tool vet help`

- View details and flags for a particular check:

`go tool vet help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">check_name</span>

- Display offending lines plus N lines of surrounding context:

`go vet -c=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>

- Output analysis and errors in JSON format:

`go vet -json`
