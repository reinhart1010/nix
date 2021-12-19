---
layout: page
title: common/nx (English)
description: "CLI utility for managing `nx` workspaces."
content_hash: f6ac9a5bb2ab2c921286e27755c4e174ac3b817b
---
# nx

CLI utility for managing `nx` workspaces.
More information: <https://nx.dev/l/r/getting-started/nx-cli>.

- Build a specific project:

`nx build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project</span>

- Test a specific project:

`nx test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project</span>

- Execute a target on a specific project:

`nx run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>

- Execute a target on multiple projects:

`nx run-many --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>` --projects `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project1</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project2</span>

- Execute a target on all projects in the workspace:

`nx run-many --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>` --all`

- Execute a target only on projects that have been changed:

`nx affected --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>
