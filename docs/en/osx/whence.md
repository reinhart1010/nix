---
layout: page
title: osx/whence (English)
description: "A Zsh builtin to indicate how a command would be interpreted."
content_hash: def9ff3be7eabef22dd4f0696c287bde0a391a40
last_modified_at: 2024-03-10
related_topics:
  - title: español version
    url: /es/osx/whence.html
    icon: bi bi-globe
tldri18n_status: 2
---
# whence

A Zsh builtin to indicate how a command would be interpreted.
More information: <https://keith.github.io/xcode-man-pages/whence.1.html>.

- Interpret `command`, with expansion if defined as an `alias` (similar to the `command -v` builtin):

`whence "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`

- Display type of `command`, with location if defined as a function, or binary (equivalent to the `type` and `command -V` builtins):

`whence -v "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`

- Same as above, except display content of shell functions instead of location (equivalent to `which` builtin):

`whence -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`

- Same as above, but show all occurrences on command path (equivalent to the `where` builtin):

`whence -ca "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`

- Search only the `PATH` for `command`, ignoring builtins, aliases or shell functions (equivalent to the `where` command):

`whence -p "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`
