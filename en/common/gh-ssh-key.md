---
layout: page
title: common/gh-ssh-key (English)
description: "Manage GitHub SSH keys from the command-line."
content_hash: 07a7be9c70f196ee616fb7606ec7462e94d3fb7e
---
# gh ssh-key

Manage GitHub SSH keys from the command-line.
More information: <https://cli.github.com/manual/gh_ssh-key>.

- Display help:

`gh ssh-key`

- List SSH keys for the currently authenticated user:

`gh ssh-key list`

- Add an SSH key to the currently authenticated user's account:

`gh ssh-key add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/key.pub</span>

- Add an SSH key to the currently authenticated user's account with a specific title:

`gh ssh-key add --title `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">title</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/key.pub</span>
