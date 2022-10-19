---
layout: page
title: common/git-bulk (English)
description: "Execute operations on multiple Git repositories."
content_hash: 36e6337b5e886d1b0be51b3f6d911f908d5a847b
---
# git bulk

Execute operations on multiple Git repositories.
Part of `git-extras`.
More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-bulk>.

- Register the current directory as a workspace:

`git bulk --addcurrent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">workspace_name</span>

- Register a workspace for bulk operations:

`git bulk --addworkspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">workspace_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/absolute/path/to/repository</span>

- Clone a repository inside a specific directory then register the repository as a workspace:

`git bulk --addworkspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">workspace_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/absolute/path/to/parent_directory</span>` --from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_repository_location</span>

- Clone repositories from a newline-separated list of remote locations then register them as workspaces:

`git bulk --addworkspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">workspace-name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">absolute/path/to/root/directory</span>` --from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">absolute/path/to/file</span>

- List all registered workspaces:

`git bulk --listall`

- Run a Git command on the repositories of the current workspace:

`git bulk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_arguments</span>

- Remove a specific workspace:

`git bulk --removeworkspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">workspace_name</span>

- Remove all workspaces:

`git bulk --purge`
