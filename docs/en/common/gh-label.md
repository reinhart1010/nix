---
layout: page
title: common/gh-label (English)
description: "Work with GitHub labels."
content_hash: 96179b6ea92e5f8d94c391111057eb808100102d
last_modified_at: 2023-07-16
---
# gh label

Work with GitHub labels.
More information: <https://cli.github.com/manual/gh_label>.

- List labels for the repository in the current directory:

`gh label list`

- View labels for the repository in the current directory in the default web browser:

`gh label list --web`

- Create a label with a specific name, description and color in hexadecimal format for the repository in the current directory:

`gh label create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --description "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">description</span>`" --color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">color_hex</span>

- Delete a label for the repository in the current directory, prompting for confirmation:

`gh label delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Update the name and description for a specific label for the repository in the current directory:

`gh label edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_name</span>` --description "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">description</span>`"`

- Clone labels from a specific repository into the repository in the current directory:

`gh label clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">owner</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>

- Display help for a subcommand:

`gh label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` --help`
