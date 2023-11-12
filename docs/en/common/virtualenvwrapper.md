---
layout: page
title: common/virtualenvwrapper (English)
description: "Group of simple wrapper commands for Python's `virtualenv` tool."
content_hash: 6928029d54ee69aac1d09f2623a32937e417564b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# virtualenvwrapper

Group of simple wrapper commands for Python's `virtualenv` tool.
More information: <http://virtualenvwrapper.readthedocs.org>.

- Create a new Python `virtualenv` in `$WORKON_HOME`:

`mkvirtualenv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">virtualenv_name</span>

- Create a `virtualenv` for a specific Python version:

`mkvirtualenv --python `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/local/bin/python3.8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">virtualenv_name</span>

- Activate or use a different `virtualenv`:

`workon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">virtualenv_name</span>

- Stop the `virtualenv`:

`deactivate`

- List all virtual environments:

`lsvirtualenv`

- Remove a `virtualenv`:

`rmvirtualenv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">virtualenv_name</span>

- Get summary of all virtualenvwrapper commands:

`virtualenvwrapper`
