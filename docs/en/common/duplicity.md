---
layout: page
title: common/duplicity (English)
description: "Create incremental, compressed, encrypted and versioned backups."
content_hash: bda6af5f28270455e5e178241cabadb821eaa741
last_modified_at: 2024-04-20
related_topics:
  - title: italiano version
    url: /it/common/duplicity.html
    icon: bi bi-globe
tldri18n_status: 2
---
# duplicity

Create incremental, compressed, encrypted and versioned backups.
Can also upload the backups to a variety of backend services.
It is worth mentioning that depending on the version, some options may not be available (e.g. `--gio` in 2.0.0).
More information: <http://duplicity.nongnu.org>.

- Backup a directory via FTPS to a remote machine, encrypting it with a password:

`FTP_PASSWORD=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ftp_login_password</span>` PASSPHRASE=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encryption_password</span>` duplicity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ftps://user@hostname/target/directory/path/</span>

- Backup a directory to Amazon S3, doing a full backup every month:

`duplicity --full-if-older-than `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1M</span>` s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bucket_name[/prefix]</span>

- Delete versions older than 1 year from a backup stored on a WebDAV share:

`FTP_PASSWORD=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">webdav_login_password</span>` duplicity remove-older-than `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1Y</span>` --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">webdav[s]://user@hostname[:port]/some_dir</span>

- List the available backups:

`duplicity collection-status "file://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">absolute/path/to/backup/directory</span>`"`

- List the files in a backup stored on a remote machine, via SSH:

`duplicity list-current-files --time `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYY-MM-DD</span>` scp://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user@hostname</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/backup/dir</span>

- Restore a subdirectory from a GnuPG-encrypted local backup to a given location:

`PASSPHRASE=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gpg_key_password</span>` duplicity restore --encrypt-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gpg_key_id</span>` --path-to-restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">relative/path/restoredirectory</span>` file://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">absolute/path/to/backup/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory/to/restore/to</span>
