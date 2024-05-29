---
layout: page
title: common/mypy (English)
description: "Type check Python code."
content_hash: 1b3cab39c33504c8a601f3f2b195863131d2805f
last_modified_at: 2024-05-29
tldri18n_status: 2
---
# mypy

Type check Python code.
More information: <https://mypy.readthedocs.io/en/stable/running_mypy.html>.

- Type check a specific file:

`mypy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.py</span>

- Type check a specific [m]odule:

`mypy -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Type check a specific [p]ackage:

`mypy -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Type check a string of code:

`mypy -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>`"`

- Ignore missing imports:

`mypy --ignore-missing-imports `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Show detailed error messages:

`mypy --show-traceback `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Specify a custom configuration file:

`mypy --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config_file</span>

- Display [h]elp:

`mypy -h`
