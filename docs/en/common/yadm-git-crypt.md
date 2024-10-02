---
layout: page
title: common/yadm-git-crypt (English)
description: "Git Crypt enables transparent encryption and decryption of files in a git repository."
content_hash: 02f6da6b426af5b3343d4f5a7d28f74bb2b332ec
last_modified_at: 2024-10-02
tldri18n_status: 2
---
# yadm git-crypt

Git Crypt enables transparent encryption and decryption of files in a git repository.
See also: `git-crypt`.
More information: <https://github.com/AGWA/git-crypt>.

- Initialize repo to use Git Crypt:

`yadm git-crypt init`

- Share the repository using GPG:

`yadm git-crypt add-gpg-user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_id</span>

- After cloning a repository with encrypted files, unlock them:

`yadm git-crypt unlock`

- Export a symmetric secret key:

`yadm git-crypt export-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/key_file</span>
