---
layout: page
title: windows/msg (English)
description: "Send a message to a user or session."
content_hash: 47556d4de2d677a1f6b438822fce3db47057cabd
last_modified_at: 2024-02-15
related_topics:
  - title: polski version
    url: /pl/windows/msg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/msg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# msg

Send a message to a user or session.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/msg>.

- Send a message to a specified user or session:

`msg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username|session_name|session_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>

- Send a message from `stdin`:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`" | msg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username|session_name|session_id</span>

- Send a message to a specific server:

`msg /server:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username|session_name|session_id</span>

- Send a message to all users of the current machine:

`msg *`

- Set a delay in seconds for a message:

`msg /time:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>
