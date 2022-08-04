---
layout: page
title: common/tox (English)
description: "Automate Python testing across multiple Python versions."
content_hash: d6d0fbc2b1b6b88edcc0d31de0fd853e5897149d
---
# tox

Automate Python testing across multiple Python versions.
Use tox.ini to configure environments and test command.
More information: <https://github.com/tox-dev/tox>.

- Run tests on all test environments:

`tox`

- Create a `tox.ini` configuration:

`tox-quickstart`

- List the available environments:

`tox --listenvs-all`

- Run tests on a specific environment (e.g. python 3.6):

`tox -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">py36</span>

- Force the virtual environment to be recreated:

`tox --recreate -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">py27</span>
