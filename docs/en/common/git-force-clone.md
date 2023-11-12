---
layout: page
title: common/git-force-clone (English)
description: "Provides the basic functionality of `git clone`, but if the destination git repository already exists it will force-reset it to resemble a clone of the remote."
content_hash: f6b530498dcbe4324534cf6515733cc68ce8edb6
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# git force-clone

Provides the basic functionality of `git clone`, but if the destination git repository already exists it will force-reset it to resemble a clone of the remote.
Part of `git-extras`.
More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-force-clone>.

- Clone a Git repository into a new directory:

`git force-clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_repository_location</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Clone a Git repository into a new directory, checking out an specific branch:

`git force-clone -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_repository_location</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Clone a Git repository into an existing directory of a Git repository, performing a force-reset to resemble it to the remote and checking out an specific branch:

`git force-clone -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_repository_location</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
