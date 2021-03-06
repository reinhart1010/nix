---
layout: page
title: common/duplicity (italiano)
description: "Crea archivi incrementali, compressi, cifrati con controllo di versione."
content_hash: 38e1836c47300601d04fb51749e1a9a9456f3d8c
related_topics:
  - title: English version
    url: /en/common/duplicity.html
    icon: bi bi-globe
---
# duplicity

Crea archivi incrementali, compressi, cifrati con controllo di versione.
Può caricare i backup su una varietà di servizi backend.
Maggiori informazioni: <http://duplicity.nongnu.org>.

- Esegui il backup di una directory via FTPS su una macchina remota, cifrandolo con una password:

`FTP_PASSWORD=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password_login_ftp</span>` PASSPHRASE=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password_cifratura</span>` duplicity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/cartella_sorgente</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ftps://utente@hostname/percorso/a/cartella_target/</span>

- Esegui il backup di una directory in un server Amazon S3, facendo un backup completo ogni mese:

`duplicity --full-if-older-than `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1M</span>` --use-new-style s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_bucket[/prefisso]</span>

- Elimina le versioni più vecchie di un anno da un backup salvato in un server WebDAV:

`FTP_PASSWORD=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password_login_webdav</span>` duplicity remove-older-than `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1Y</span>` --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">webdav[s]://utente@hostname[:porta]/directory</span>

- Elenca i backup disponibili:

`duplicity collection-status "file://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/assoluto/a/directory/di/backup</span>`"`

- Elenca i file in un backup salvato su una macchina remota, via SSH:

`duplicity list-current-files --time `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYY-MM-DD</span>` scp://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utente@hostname</span>`/percorso/a/directory/backup`

- Ripristina una sotto-directory da un backup locale cifrato con GnuPG in una posizione precisa:

`PASSPHRASE=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password_chiave_gpg</span>` duplicity restore --encrypt-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_chiave_gpg</span>` --file-to-restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/relativo/sotto_directory</span>` file://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/assoluto/a/directory/di/backup</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/directory/dove/ripristinare</span>
