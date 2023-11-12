---
layout: page
title: common/complete (English)
description: "Provides argument autocompletion to shell commands."
content_hash: e283d60d47eb34b2f654621f750728825bfd3a85
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/common/complete.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/complete.html
    icon: bi bi-globe
tldri18n_status: 2
---
# complete

Provides argument autocompletion to shell commands.
More information: <https://www.gnu.org/software/bash/manual/html_node/Programmable-Completion-Builtins.html>.

- Apply a function that performs autocompletion to a command:

`complete -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">function</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Apply a command that performs autocompletion to another command:

`complete -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">autocomplete_command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Apply autocompletion without appending a space to the completed word:

`complete -o nospace -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">function</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
