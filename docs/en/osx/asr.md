---
layout: page
title: osx/asr (English)
description: "Restore (copy) a disk image onto a volume."
content_hash: c74ba1314c759e7f2fd825db2f28dd179c4c83c5
last_modified_at: 2024-01-31
related_topics:
  - title: español version
    url: /es/osx/asr.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/asr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/asr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/asr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# asr

Restore (copy) a disk image onto a volume.
The command name stands for Apple Software Restore.
More information: <https://www.unix.com/man-page/osx/8/asr/>.

- Restore a disk image to a target volume:

`sudo asr restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_file.dmg</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/volume_file</span>

- Erase the target volume before restoring:

`sudo asr restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_file.dmg</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/volume_file</span>` --erase`

- Skip verification after restoring:

`sudo asr restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_file.dmg</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/volume_file</span>` --noverify`

- Clone volumes without using an intermediate disk image:

`sudo asr restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/volume_file</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/volume_file</span>
