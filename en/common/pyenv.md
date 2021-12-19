---
layout: page
title: common/pyenv (English)
description: "Switch between multiple versions of Python easily."
content_hash: 1b5a4e5acc047ba7e071e0c108d7af845cb8a0f7
related_topics:
  - title: italiano version
    url: /it/common/pyenv.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/pyenv.html
    icon: bi bi-globe
---
# pyenv

Switch between multiple versions of Python easily.
More information: <https://github.com/pyenv/pyenv>.

- List all available commands:

`pyenv commands`

- List all Python versions under the `${PYENV_ROOT}/versions` directory:

`pyenv versions`

- Install a Python version under the `${PYENV_ROOT}/versions` directory:

`pyenv install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.7.10</span>

- Uninstall a Python version under the `${PYENV_ROOT}/versions` directory:

`pyenv uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.7.10</span>

- Set Python version to be used globally in the current machine:

`pyenv global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.7.10</span>

- Set Python version to be used in the current directory and all directories below it:

`pyenv local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.7.10</span>
