---
layout: page
title: common/pydocstyle (English)
description: "Statically check Python scripts for compliance with Python docstring conventions."
content_hash: 9dfd6ca89ff170d19da64199fb1416419414d214
last_modified_at: 2024-03-31
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pydocstyle.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pydocstyle

Statically check Python scripts for compliance with Python docstring conventions.
More information: <https://www.pydocstyle.org/en/latest/>.

- Analyze a Python script or all the Python scripts in a specific directory:

`pydocstyle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.py|path/to/directory</span>

- Show an [e]xplanation of each error:

`pydocstyle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-e|--explain</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.py|path/to/directory</span>

- Show [d]ebug information:

`pydocstyle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--debug</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.py|path/to/directory</span>

- Display the total number of errors:

`pydocstyle --count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.py|path/to/directory</span>

- Use a specific configuration file:

`pydocstyle --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.py|path/to/directory</span>

- Ignore one or more errors:

`pydocstyle --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">D101,D2,D107,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.py|path/to/directory</span>

- Check for errors from a specific convention:

`pydocstyle --convention `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pep257|numpy|google</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.py|path/to/directory</span>
