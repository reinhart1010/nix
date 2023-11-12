---
layout: page
title: common/pipx (English)
description: "Install and run Python applications in isolated environments."
content_hash: 48032e4525db17c1d4b84f70b33a5970792edc73
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pipx

Install and run Python applications in isolated environments.
More information: <https://github.com/pypa/pipx>.

- Run an app in a temporary virtual environment:

`pipx run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pycowsay</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">moo</span>

- Install a package in a virtual environment and add entry points to path:

`pipx install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- List installed packages:

`pipx list`

- Run an app in a temporary virtual environment with a package name different from the executable:

`pipx run --spec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpx-cli</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpx</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://www.github.com</span>

- Inject dependencies into an existing virtual environment:

`pipx inject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependency1 dependency2 ...</span>

- Install a package in a virtual environment with pip arguments:

`pipx install --pip-args='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pip-args</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>
