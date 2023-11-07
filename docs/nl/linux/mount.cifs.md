---
layout: page
title: linux/mount.cifs (Nederlands)
description: "Mount SMB (Server Message Block) of CIFS (Common Internet File System) shares."
content_hash: d89c1da91afb2198f06e6db5f40faafeaaee583e
last_modified_at: 2023-11-07
related_topics:
  - title: English version
    url: /en/linux/mount.cifs.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mount.cifs

Mount SMB (Server Message Block) of CIFS (Common Internet File System) shares.
Opmerking: u kunt ook hetzelfde doen door de optie `-t cifs` door te geven aan `mount`.
Meer informatie: <https://manned.org/mount.cifs>.

- Verbinding maken met de opgegeven gebruikersnaam of `$USER` als standaard (U wordt gevraagd om een wachtwoord):

`mount.cifs -o user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>` //`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">share_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mountpoint</span>

- Maak verbinding als gastgebruiker (zonder wachtwoord):

`mount.cifs -o guest //`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">share_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mountpoint</span>

- Stel eigendomsinformatie in voor de mounted map:

`mount.cifs -o uid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_id|gebruikersnaam</span>`,gid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_id|groupname</span>` //`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">share_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mountpoint</span>
