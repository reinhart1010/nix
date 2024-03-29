---
layout: page
title: windows/mount (italiano)
description: "Montare le condivisioni di rete del Network File System (NFS)."
content_hash: d665fb26dc86ff80a980eb126b353a6256b383b9
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/mount.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mount

Montare le condivisioni di rete del Network File System (NFS).
Maggiori informazioni: <https://learn.microsoft.com/windows-server/administration/windows-commands/mount>.

- Monta una share con la lettera di unità "Z":

`mount \\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_del_computer</span>`\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_della_share</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Z:</span>

- Monta una share con la successiva lettera di unità disponibile:

`mount \\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_del_computer</span>`\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_della_share</span>` *`

- Monta una share con un timeout di lettura in secondi (predefinito a 0,8, può essere 0,9 o da 1 a 60):

`mount -o timeout=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secondi</span>` \\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_del_computer</span>`\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_della_share</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Z:</span>

- Monta una share e riprova fino a 10 volte se fallisce:

`mount -o retry=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_di_ripetizioni</span>` \\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_del_computer</span>`\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_della_share</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Z:</span>

- Monta una share forzando la distinzione tra maiuscole e minuscole:

`mount -o casesensitive \\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_del_computer</span>`\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_della_share</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Z:</span>

- Monta una share come utente anonimo:

`mount -o anon \\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_del_computer</span>`\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_della_share</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Z:</span>

- Monta una share utilizzando un tipo di montaggio specifico:

`mount -o mtype=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">soft|hard</span>` \\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_del_computer</span>`\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_della_share</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Z:</span>
