---
layout: page
title: osx/whence (English)
description: "A zsh builtin to indicate how a given command would be interpreted."
content_hash: ef40cc0c94de66a3755ef463a99241c27efb4bce
---
# whence

A zsh builtin to indicate how a given command would be interpreted.

- Interpret `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`, with expansion if defined as an `alias` (similar to the `command -v` builtin):

`whence `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Display type of `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`, with location if defined as a function, or binary (equivalent to the `type` and `command -V` builtins):

`whence -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Same as above, except display content of shell functions instead of location (equivalent to `which` builtin):

`whence -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Same as above, but show all occurrences on command path (equivalent to the `where` builtin):

`whence -ca `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Search only the `PATH` for `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`, ignoring builtins, aliases or shell functions (equivalent to the `where` command):

`whence -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
