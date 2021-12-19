---
layout: page
title: common/pip-install (English)
description: "Install Python packages."
content_hash: df57e274870b53ee5b0e766333446def2ad6a8df
related_topics:
  - title: Deutsch version
    url: /de/common/pip-install.html
    icon: bi bi-globe
---
# pip install

Install Python packages.
More information: <https://pip.pypa.io>.

- Install a package:

`pip install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Install a specific version of a package:

`pip install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>`==`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_version</span>

- Install packages listed in a file:

`pip install --requirement `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/requirements.txt</span>

- Install packages from an URL or local file archive (.tar.gz | .whl):

`pip install --find-links `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|path/to/file</span>

- Install the local package in the current directory in develop (editable) mode:

`pip install --editable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>
