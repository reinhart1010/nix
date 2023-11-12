---
layout: page
title: windows/shutdown (English)
description: "A tool for shutting down, restarting or logging off a machine."
content_hash: 0c330bbbb69473ef0adeb5fa983bce4f268bee2f
last_modified_at: 2023-11-12
related_topics:
  - title: Nederlands version
    url: /nl/windows/shutdown.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/shutdown.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shutdown

A tool for shutting down, restarting or logging off a machine.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/shutdown>.

- Shutdown the current machine:

`shutdown /s`

- Shutdown the current machine force-closing all apps:

`shutdown /s /f`

- Restart the current machine immediately:

`shutdown /r /t 0`

- Hibernate the current machine:

`shutdown /h`

- Log off the current machine:

`shutdown /l`

- Specify a timeout in seconds to wait before shutting down:

`shutdown /s /t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8</span>

- Abort a shutdown sequence whose timeout is yet to expire:

`shutdown /a`

- Shutdown a remote machine:

`shutdown /m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\\hostname</span>
