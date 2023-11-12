---
layout: page
title: linux/ostree (English)
description: "Version control for binary files similar to git but optimized for operating system root filesystems."
content_hash: a6144ac35a6dde6f649b5243366556cca2422dd6
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# ostree

Version control for binary files similar to git but optimized for operating system root filesystems.
OSTree is the foundation for immutable image-based operating systems such as Fedora Silverblue, Fedora IoT or Fedora CoreOS.
More information: <https://ostreedev.github.io/ostree>.

- Initialize a repository of the files in `$PWD` with metadata in `$PWD/path/to/repo`:

`ostree init --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repo</span>

- Create a commit (snapshot) of the files:

`ostree commit --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repo</span>` --branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Show files in commit:

`ostree ls --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_id</span>

- Show metadata of commit:

`ostree show --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_id</span>

- Show list of commits:

`ostree log --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Show repo summary:

`ostree summary --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repo</span>` --view`

- Show available refs (branches):

`ostree refs --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repo</span>
