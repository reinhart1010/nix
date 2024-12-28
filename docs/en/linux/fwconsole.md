---
layout: page
title: linux/fwconsole (English)
description: "Manage and configure your FreePBX system (PBX server)."
content_hash: 56930abde6b36599ad206a26fc5060977d1f04ef
last_modified_at: 2024-12-28
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/fwconsole.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fwconsole

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
