---
layout: page
title: linux/smbclient (italiano)
description: "Programma client simile ad FTP per server SMB/CIFS."
content_hash: 3e047ca2f58785fb3072823bed9e8190c39b90ef
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/smbclient.html
    icon: bi bi-globe
tldri18n_status: 2
---
# smbclient

Programma client simile ad FTP per server SMB/CIFS.
Maggiori informazioni: <https://manned.org/smbclient>.

- Connettiti ad una share (all'utente verrà richiesta la password; `exit` per uscire dalla sessione):

`smbclient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">//server/share</span>

- Connettiti con un altro nome utente:

`smbclient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">//server/share</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Connettiti con un altro gruppo di lavoro:

`smbclient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">//server/share</span>` --workgroup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dominio</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Connettiti con un nome utente ed una password:

`smbclient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">//server/share</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username%password</span>

- Scarica un file dal server:

`smbclient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">//server/share</span>` --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>` --command "get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.txt</span>`"`

- Carica un file sul server:

`smbclient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">//server/share</span>` --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>` --command "put `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.txt</span>`"`

- Elenca le share di un server in modo anonimo:

`smbclient --list=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>` --no-pass`
