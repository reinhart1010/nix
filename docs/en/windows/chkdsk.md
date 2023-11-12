---
layout: page
title: windows/chkdsk (English)
description: "Check file system and volume metadata for errors."
content_hash: 7a6e7ef5e2c4f3c0ebbe5fc659d47aa8f8d0f036
last_modified_at: 2023-11-12
related_topics:
  - title: Indonesia version
    url: /id/windows/chkdsk.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/chkdsk.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/chkdsk.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/windows/chkdsk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chkdsk

Check file system and volume metadata for errors.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/chkdsk>.

- Specify the drive letter (followed by a colon), mount point, or volume name to check:

`chkdsk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume</span>

- Fix errors on a specific volume:

`chkdsk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume</span>` /f`

- Dismount a specific volume before checking:

`chkdsk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume</span>` /x`

- Change the log file size to the specified size (only for NTFS):

`chkdsk /l`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size</span>
