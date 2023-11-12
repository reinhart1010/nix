---
layout: page
title: common/ipfs (English)
description: "Inter Planetary File System."
content_hash: 77dd73a73507c8f95f936274b50f446cb12c1a5b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# ipfs

Inter Planetary File System.
A peer-to-peer hypermedia protocol. Aims to make the web more open.
More information: <https://ipfs.io>.

- Add a file from local to the filesystem, pin it and print the relative hash:

`ipfs add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Add a directory and its files recursively from local to the filesystem and print the relative hash:

`ipfs add -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Save a remote file and give it a name but not pin it:

`ipfs get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Pin a remote file locally:

`ipfs pin add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash</span>

- Display pinned files:

`ipfs pin ls`

- Unpin a file from the local storage:

`ipfs pin rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash</span>

- Remove unpinned files from local storage:

`ipfs repo gc`
