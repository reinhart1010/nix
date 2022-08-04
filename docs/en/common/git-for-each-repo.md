---
layout: page
title: common/git-for-each-repo (English)
description: "Run a Git command on a list of repositories."
content_hash: 8ad5fb4e6c4301d22f96b8a49486575c43a50879
---
# git for-each-repo

Run a Git command on a list of repositories.
Note: this command is experimental and may change.
More information: <https://git-scm.com/docs/git-for-each-repo>.

- Run maintenance on each of a list of repositories stored in the `maintenance.repo` user configuration variable:

`git for-each-repo --config=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">maintenance.repo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">maintenance run</span>

- Run `git pull` on each repository listed in a global configuration variable:

`git for-each-repo --config=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">global_configuration_variable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pull</span>
