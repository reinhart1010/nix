---
layout: page
title: common/pyenv (English)
description: "Switch between multiple versions of Python easily."
content_hash: ba24bce48602da5de72e87d039af5f18f4cf2634
last_modified_at: 2024-01-09
related_topics:
  - title: italiano version
    url: /it/common/pyenv.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/pyenv.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/pyenv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pyenv

Switch between multiple versions of Python easily.
See also: `asdf`.
More information: <https://github.com/pyenv/pyenv>.

- List all available commands:

`pyenv commands`

- List all Python versions under the `${PYENV_ROOT}/versions` directory:

`pyenv versions`

- List all Python versions that can be installed from upstream:

`pyenv install --list`

- Install a Python version under the `${PYENV_ROOT}/versions` directory:

`pyenv install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.7.10</span>

- Uninstall a Python version under the `${PYENV_ROOT}/versions` directory:

`pyenv uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.7.10</span>

- Set Python version to be used globally in the current machine:

`pyenv global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.7.10</span>

- Set Python version to be used in the current directory and all directories below it:

`pyenv local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.7.10</span>
