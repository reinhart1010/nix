---
layout: page
title: common/pip (English)
description: "Python package manager."
content_hash: e748f65f90ab76ad3719875ae366d40713f2f7d7
related_topics:
  - title: Deutsch version
    url: /de/common/pip.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/pip.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/pip.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/pip.html
    icon: bi bi-globe
---
# pip

Python package manager.
Some subcommands such as `pip install` have their own usage documentation.
More information: <https://pip.pypa.io>.

- Install a package (see `pip install` for more install examples):

`pip install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Install a package to the user's directory instead of the system-wide default location:

`pip install --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Upgrade a package:

`pip install --upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Uninstall a package:

`pip uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Save installed packages to file:

`pip freeze > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">requirements.txt</span>

- Show installed package info:

`pip show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Install packages from a file:

`pip install --requirement `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">requirements.txt</span>
