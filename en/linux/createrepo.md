---
layout: page
title: linux/createrepo (English)
description: "Initializes an RPM repository in the given directory, including all XML and SQLite files."
content_hash: 1c180c11b66d189826dbfe236cb8aa71fa8d72fe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># createrepo

Initializes an RPM repository in the given directory, including all XML and SQLite files.
More information: <https://manned.org/createrepo>.

- Initialize a basic repository in a directory:

`createrepo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Initialize a repository, exclude test RPMs and display verbose logs:

`createrepo -v -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test_*.rpm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Initialize a repository, using SHA1 as the checksum algorithm, and ignoring symbolic links:

`createrepo -S -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sha1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
