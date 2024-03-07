---
layout: page
title: windows/reg (English)
description: "Manage keys and their values in the Windows registry."
content_hash: ee23179b8cc27ed7df28e22efe127f8699968ac3
last_modified_at: 2024-03-07
related_topics:
  - title: 中文 version
    url: /zh/windows/reg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# reg

Manage keys and their values in the Windows registry.
Some subcommands such as `reg add` have their own usage documentation.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg>.

- Execute a registry command:

`reg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- View documentation for adding and copying subkeys:

`tldr reg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">add|copy</span>

- View documentation for deleting keys and subkeys:

`tldr reg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">delete|unload</span>

- View documentation for searching, viewing, and comparing keys:

`tldr reg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">compare|flags|query</span>

- View documentation for exporting and importing registry keys not preserving the key ownerships and ACLs:

`tldr reg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">export|import</span>

- View documentation for saving, restoring registry and unloading keys preserving the key ownerships and ACLs:

`tldr reg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">save|restore|load|unload</span>

- Display help:

`reg /?`

- Display help for a specific command:

`reg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` /?`
