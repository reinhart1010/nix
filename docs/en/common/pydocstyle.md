---
layout: page
title: common/pydocstyle (English)
description: "Statically check Python scripts for compliance with Python docstring conventions."
content_hash: 9c9b07902d8b774afda818407304c77c0e10cd55
last_modified_at: 2024-06-12
related_topics:
  - title: español version
    url: /es/common/pydocstyle.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pydocstyle

Statically check Python scripts for compliance with Python docstring conventions.
More information: <https://www.pydocstyle.org/en/latest/>.

- Analyze a Python script or all the Python scripts in a specific directory:

`pydocstyle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.py|path/to/directory</span>

- Show an explanation of each error:

`pydocstyle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-e|--explain</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.py|path/to/directory</span>

- Show debug information:

`pydocstyle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--debug</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.py|path/to/directory</span>

- Display the total number of errors:

`pydocstyle --count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.py|path/to/directory</span>

- Use a specific configuration file:

`pydocstyle --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.py|path/to/directory</span>

- Ignore one or more errors:

`pydocstyle --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">D101,D2,D107,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.py|path/to/directory</span>

- Check for errors from a specific convention:

`pydocstyle --convention `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pep257|numpy|google</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.py|path/to/directory</span>
