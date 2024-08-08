---
layout: page
title: common/ntfyme (English)
description: "A notification tool to track and notify you about your long-running termination process."
content_hash: 9dcbbe20de38d9522b6ee02e21d0167cead4cddd
last_modified_at: 2024-08-08
tldri18n_status: 2
---
# ntfyme

A notification tool to track and notify you about your long-running termination process.
Send notifications with success/error messages with Gmail, Telegram, and more.
More information: <https://github.com/AnirudhG07/ntfyme>.

- Directly run your command:

`ntfyme exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--cmd</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Pipe your command and run:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | ntfyme exec`

- Run multiple commands by enclosing them in quotes:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command1; command2; command3</span>`" | ntfyme exec`

- Track and terminate the process after prolonged suspension:

`ntfyme exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--track-process</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--cmd</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Setup the tool configurations interactively:

`ntfyme setup`

- Encrypt your password:

`ntfyme enc`

- See the log history:

`ntfyme log`

- Open and edit the configuration file:

`ntfyme config`
