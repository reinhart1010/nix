---
layout: page
title: linux/duperemove (English)
description: "Finds duplicate filesystem extents and optionally schedule them for deduplication."
content_hash: 3a4868aed68221056d4d4b019faceaf424b460f5
---
# duperemove

Finds duplicate filesystem extents and optionally schedule them for deduplication.
An extent is small part of a file inside the filesystem.
On some filesystems one extent can be referenced multiple times, when parts of the content of the files are identical.
More information: <https://markfasheh.github.io/duperemove/>.

- Search for duplicate extents in a directory and show them:

`duperemove -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Deduplicate duplicate extents on a Btrfs or XFS (experimental) filesystem:

`duperemove -r -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Use a hash file to store extent hashes (less memory usage and can be reused on subsequent runs):

`duperemove -r -d --hashfile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/hashfile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Limit I/O threads (for hashing and dedupe stage) and CPU threads (for duplicate extent finding stage):

`duperemove -r -d --hashfile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/hashfile</span>` --io-threads=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` --cpu-threads=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
