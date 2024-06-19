---
layout: page
title: linux/mount.cifs (Nederlands)
description: "Mount SMB (Server Message Block) of CIFS (Common Internet File System) shares."
content_hash: 24e0520b0222a1d1eff6eec17dcbc88b1881193d
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/linux/mount.cifs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mount.cifs

Mount SMB (Server Message Block) of CIFS (Common Internet File System) shares.
Let op: u kunt ook hetzelfde doen door de optie `-t cifs` door te geven aan `mount`.
Meer informatie: <https://manned.org/mount.cifs>.

- Verbinding maken met de opgegeven gebruikersnaam of `$USER` als standaard (U wordt gevraagd om een wachtwoord):

`mount.cifs -o user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>` //`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">share_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mountpoint</span>

- Maak verbinding als gastgebruiker (zonder wachtwoord):

`mount.cifs -o guest //`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">share_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mountpoint</span>

- Stel eigendomsinformatie in voor de mounted map:

`mount.cifs -o uid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_id|gebruikersnaam</span>`,gid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_id|groupname</span>` //`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">share_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mountpoint</span>
