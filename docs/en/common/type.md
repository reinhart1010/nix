---
layout: page
title: common/type (English)
description: "Display the type of command the shell will execute."
content_hash: fc5971ecebf6c0a89def1f3145a8d2666b33b894
last_modified_at: 2024-04-28
related_topics:
  - title: français version
    url: /fr/common/type.html
    icon: bi bi-globe
tldri18n_status: 2
---
# type

Display the type of command the shell will execute.
Note: all examples are not POSIX compliant.
More information: <https://manned.org/type>.

- Display the type of a command:

`type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Display all locations containing the specified executable (works only in Bash/fish/Zsh shells):

`type -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Display the name of the disk file that would be executed (works only in Bash/fish/Zsh shells):

`type -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Display the type of a specific command, alias/keyword/function/builtin/file (works only in Bash/fish shells):

`type -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
