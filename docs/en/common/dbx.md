---
layout: page
title: common/dbx (English)
description: "Interact with the Databricks platform."
content_hash: 1a1a7d82a3e5fe3e9f8db50e282116fed25f5ab9
last_modified_at: 2024-12-28
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dbx.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dbx

Interact with the Databricks platform.
Note: this tool has been retired and it is recommended to use Databricks Asset Bundles instead.
More information: <https://dbx.readthedocs.io/en/latest/reference/cli/#dbx>.

- Create a new `dbx` project in the current working directory:

`dbx configure --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DEFAULT</span>

- Sync local files from the specified path to DBFS and watch for changes:

`dbx sync dbfs --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --dest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/remote_directory</span>

- Deploy the specified workflow to artifact storage:

`dbx deploy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">workflow_name</span>

- Launch the specified workflow after deploying it:

`dbx launch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">workflow_name</span>
