---
layout: page
title: common/ruff-check (English)
description: "An extremely fast Python linter. `check` is the default command - it can be omitted everywhere."
content_hash: 521f5c3207af9f69e53a7c20addc03a3f3542cf8
last_modified_at: 2024-02-28
tldri18n_status: 2
---
# ruff check

An extremely fast Python linter. `check` is the default command - it can be omitted everywhere.
If no files or directories are specified, the current working directory is used by default.
More information: <https://docs.astral.sh/ruff/linter>.

- Run the linter on the given files or directories:

`ruff check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>

- Apply the suggested fixes, modifying the files in-place:

`ruff check --fix`

- Run the linter and re-lint on change:

`ruff check --watch`

- Only enable the specified rules (or all rules), ignoring the configuration file:

`ruff check --select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ALL|rule_code1,rule_code2,...</span>

- Additionally enable the specified rules:

`ruff check --extend-select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rule_code1,rule_code2,...</span>

- Disable the specified rules:

`ruff check --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rule_code1,rule_code2,...</span>

- Ignore all existing violations of a rule by adding `# noqa` directives to all lines that violate it:

`ruff check --select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rule_code</span>` --add-noqa`
