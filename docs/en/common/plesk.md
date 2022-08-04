---
layout: page
title: common/plesk (English)
description: "Plesk hosting control panel CLI interface."
content_hash: 297567dffb67239b5565b50fd6f18374cd583ab1
---
# plesk

Plesk hosting control panel CLI interface.
More information: <https://docs.plesk.com>.

- Generate an auto login link for the admin user and print it:

`plesk login`

- Show product version information:

`plesk version`

- List all hosted domains:

`plesk bin domain --list`

- Start watching for changes in the `panel.log` file:

`plesk log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">panel.log</span>

- Start the interactive MySQL console:

`plesk db`

- Open the Plesk main configuration file in the default editor:

`plesk conf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">panel.ini</span>
