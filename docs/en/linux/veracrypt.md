---
layout: page
title: linux/veracrypt (English)
description: "Free and open source disk encryption software."
content_hash: b84df2212613b52fe521845ffcbd5773df8f96e1
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# veracrypt

Free and open source disk encryption software.
More information: <https://www.veracrypt.fr/code/VeraCrypt/plain/doc/html/Documentation.html>.

- Create a new volume through a text user interface and use `/dev/urandom` as a source of random data:

`veracrypt --text --create --random-source=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/urandom</span>

- Decrypt a volume interactively through a text user interface and mount it to a directory:

`veracrypt --text `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/volume</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mount_point</span>

- Decrypt a partition using a keyfile and mount it to a directory:

`veracrypt --keyfiles=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/keyfile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mount_point</span>

- Dismount a volume on the directory it is mounted to:

`veracrypt --dismount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mounted_point</span>
