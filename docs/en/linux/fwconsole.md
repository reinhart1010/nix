---
layout: page
title: linux/fwconsole (English)
description: "Manage and configure your FreePBX system (PBX server)."
content_hash: 56930abde6b36599ad206a26fc5060977d1f04ef
last_modified_at: 2024-12-29
tldri18n_status: 2
---
# fwconsole

Manage and configure your FreePBX system (PBX server).
More information: <https://sangomakb.atlassian.net/wiki/spaces/PG/pages/41779247/fwconsole+commands+13>.

- Reload FreePBX configurations:

`fwconsole reload`

- Start Asterisk and other commands needed by FreePBX:

`fwconsole start`

- Stop Asterisk and other commands needed by FreePBX:

`fwconsole stop`

- View and update settings:

`fwconsole setting `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_value</span>

- List available backups:

`fwconsole backup --list`

- List available FreePBX commands:

`fwconsole list`

- Change ownership of all files and directories that FreePBX needs to be owned by the apache user:

`fwconsole chown`
