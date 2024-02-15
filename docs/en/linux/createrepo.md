---
layout: page
title: linux/createrepo (English)
description: "Initializes an RPM repository in a directory, including all XML and SQLite files."
content_hash: b3025903b5fb283a6db0b2b5d0c34c1384827ddb
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# createrepo

Initializes an RPM repository in a directory, including all XML and SQLite files.
More information: <https://manned.org/createrepo>.

- Initialize a basic repository in a directory:

`createrepo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Initialize a repository, exclude test RPMs and display verbose logs:

`createrepo -v -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test_*.rpm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Initialize a repository, using SHA1 as the checksum algorithm, and ignoring symbolic links:

`createrepo -S -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sha1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
