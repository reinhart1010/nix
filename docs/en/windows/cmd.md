---
layout: page
title: windows/cmd (English)
description: "The Windows command interpreter."
content_hash: b55246096f9297505e359fa99b42dd775ea8e826
related_topics:
  - title: italiano version
    url: /it/windows/cmd.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/cmd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/cmd.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/cmd.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/cmd.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/cmd.html
    icon: bi bi-globe
---
# cmd

The Windows command interpreter.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmd>.

- Start an interactive shell session:

`cmd`

- Execute a [c]ommand:

`cmd /c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`

- Execute a script:

`cmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bat</span>

- Execute a command and then enter an interactive shell:

`cmd /k "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`

- Start an interactive shell session where `echo` is disabled in command output:

`cmd /q`

- Start an interactive shell session with delayed [v]ariable expansion enabled or disabled:

`cmd /v:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Start an interactive shell session with command [e]xtensions enabled or disabled:

`cmd /e:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Start an interactive shell session with used Unicode encoding:

`cmd /u`
