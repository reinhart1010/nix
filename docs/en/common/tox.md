---
layout: page
title: common/tox (English)
description: "Automate Python testing across multiple Python versions."
content_hash: 7a847bef65a0c2c1e3d43417927a2d35def40cec
last_modified_at: 2023-11-12
related_topics:
  - title: العربية version
    url: /ar/common/tox.html
    icon: bi bi-globe
tldri18n_status: 2
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

- Run tests on a specific environment (e.g. Python 3.6):

`tox -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">py36</span>

- Force the virtual environment to be recreated:

`tox --recreate -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">py27</span>
