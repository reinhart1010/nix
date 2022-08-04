---
layout: page
title: common/command (English)
description: "Command forces the shell to execute the program and ignore any functions, builtins and aliases with the same name."
content_hash: c6a668c283d760bdf4a74f2bc40839480eae196b
related_topics:
  - title: italiano version
    url: /it/common/command.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/command.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/command.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/command.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/command.html
    icon: bi bi-globe
---
# command

Command forces the shell to execute the program and ignore any functions, builtins and aliases with the same name.
More information: <https://manned.org/command>.

- Execute the `ls` program literally, even if an `ls` alias exists:

`command `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls</span>

- Display the path to the executable or the alias definition of a specific command:

`command -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_name</span>
