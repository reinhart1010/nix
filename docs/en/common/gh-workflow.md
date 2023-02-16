---
layout: page
title: common/gh-workflow (English)
description: "List, view, and run GitHub Actions workflows."
content_hash: 06edf9098a5449e915b4be78fea366922c7c2767
last_modified_at: 2023-02-16
---
# gh workflow

List, view, and run GitHub Actions workflows.
More information: <https://cli.github.com/manual/gh_workflow>.

- Interactively select a workflow to view the latest jobs for:

`gh workflow view`

- View a specific workflow in the default browser:

`gh workflow view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id|workflow_name|filename.yml</span>` --web`

- Display the YAML definition of a specific workflow:

`gh workflow view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id|workflow_name|filename.yml</span>` --yaml`

- Display the YAML definition for a specific Git branch or tag:

`gh workflow view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id|workflow_name|filename.yml</span>` --ref `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch|tag_name</span>` --yaml`

- List workflow files (use `--all` to include disabled workflows):

`gh workflow list`

- Run a manual workflow with parameters:

`gh workflow run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id|workflow_name|filename.yml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--raw-field param1=value1 --raw-field param2=value2 ...</span>

- Run a manual workflow using a specific branch or tag with JSON parameters from `stdin`:

`echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{"param1": "value1", "param2": "value2", ...}</span>`' | gh workflow run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id|workflow_name|filename.yml</span>` --ref `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch|tag_name</span>

- Enable or disable a specific workflow:

`gh workflow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enable|disable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id|workflow_name|filename.yml</span>
