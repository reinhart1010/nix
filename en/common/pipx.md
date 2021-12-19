---
layout: page
title: common/pipx (English)
description: "Install and run python applications in isolated environments."
content_hash: 9f7354e393d4d159bb25dc28510a17c30ead8b71
---
# pipx

Install and run python applications in isolated environments.
More information: <https://github.com/pipxproject/pipx>.

- Run an app in a temporary virtual environment:

`pipx run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pycowsay</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">moo</span>

- Install a package in a virtual environment and add entry points to path:

`pipx install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- List installed packages:

`pipx list`

- Run an app in a temporary virtual environment with a package name different from the executable:

`pipx run --spec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpx-cli</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpx</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://www.github.com</span>
