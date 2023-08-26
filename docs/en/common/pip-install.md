---
layout: page
title: common/pip-install (English)
description: "Install Python packages."
content_hash: 98b9cc218ec0279d4511ab11716457c15edd3fda
last_modified_at: 2023-08-26
related_topics:
  - title: Deutsch version
    url: /de/common/pip-install.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/pip-install.html
    icon: bi bi-globe
---
# pip install

Install Python packages.
More information: <https://pip.pypa.io>.

- Install a package:

`pip install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Install a specific version of a package:

`pip install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>`==`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Install packages listed in a file:

`pip install --requirement `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/requirements.txt</span>

- Install packages from an URL or local file archive (.tar.gz | .whl):

`pip install --find-links `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|path/to/file</span>

- Install the local package in the current directory in develop (editable) mode:

`pip install --editable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>
