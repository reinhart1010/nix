---
layout: page
title: common/pyenv-virtualenv (English)
description: "Create virtual environments based on one's installed Python distributions."
content_hash: 4e61d0ef7fea4b31c28e9f40cff7301c82235cff
related_topics:
  - title: italiano version
    url: /it/common/pyenv-virtualenv.html
    icon: bi bi-globe
---
# pyenv virtualenv

Create virtual environments based on one's installed Python distributions.
More information: <https://github.com/pyenv/pyenv-virtualenv>.

- Create a new Python 3.6.6 virtual environment:

`pyenv virtualenv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3.6.6</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">virtualenv_name</span>

- List all existing virtual environments:

`pyenv virtualenvs`

- Activate a virtual environment:

`pyenv activate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">virtualenv_name</span>

- Deactivate the virtual environment:

`pyenv deactivate`
