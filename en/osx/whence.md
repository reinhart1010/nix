---
layout: page
title: osx/whence (English)
description: "A zsh builtin to indicate how a given command would be interpreted."
content_hash: 562a9795e0efc195a46f16830d95ded074db6f79
---
# whence

A zsh builtin to indicate how a given command would be interpreted.
More information: <https://www.unix.com/man-page/OpenSolaris/1/whence/>.

- Interpret `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`, with expansion if defined as an `alias` (similar to the `command -v` builtin):

`whence "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`

- Display type of `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`, with location if defined as a function, or binary (equivalent to the `type` and `command -V` builtins):

`whence -v "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`

- Same as above, except display content of shell functions instead of location (equivalent to `which` builtin):

`whence -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`

- Same as above, but show all occurrences on command path (equivalent to the `where` builtin):

`whence -ca "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`

- Search only the `PATH` for `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`, ignoring builtins, aliases or shell functions (equivalent to the `where` command):

`whence -p "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`
