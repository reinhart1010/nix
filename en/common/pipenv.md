---
layout: page
title: common/pipenv (English)
description: "Simple and unified Python development workflow."
content_hash: 27e4b5ce4d4cbe485ad280c3986d4336698d0b0c
related_topics:
  - title: français version
    url: /fr/common/pipenv.html
    icon: bi bi-globe
---
# pipenv

Simple and unified Python development workflow.
Manages packages and the virtual environment for a project.
More information: <https://pypi.org/project/pipenv>.

- Create a new project:

`pipenv`

- Create a new project using Python 3:

`pipenv --three`

- Install a package:

`pipenv install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Install all the dependencies for a project:

`pipenv install`

- Install all the dependencies for a project (including dev packages):

`pipenv install --dev`

- Uninstall a package:

`pipenv uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Start a shell within the created virtual environment:

`pipenv shell`

- Generate a `requirements.txt` (list of dependencies) for a project:

`pipenv lock --requirements`
