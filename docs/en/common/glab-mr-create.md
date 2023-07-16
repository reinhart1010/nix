---
layout: page
title: common/glab-mr-create (English)
description: "Manage GitLab merge requests."
content_hash: 445b7bb0364b914cd05139ccc9522b06587e0855
last_modified_at: 2023-07-16
---
# glab mr create

Manage GitLab merge requests.
More information: <https://glab.readthedocs.io/en/latest/mr/create.html>.

- Interactively create a merge request:

`glab mr create`

- Create a merge request, determining the title and description from the commit messages of the current branch:

`glab mr create --fill`

- Create a draft merge request:

`glab mr create --draft`

- Create a merge request specifying the target branch, title, and description:

`glab mr create --target-branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_branch</span>` --title "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">title</span>`" --description "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">description</span>`"`

- Start opening a merge request in the default web browser:

`glab mr create --web`
