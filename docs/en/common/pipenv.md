---
layout: page
title: common/pipenv (English)
description: "Simple and unified Python development workflow."
content_hash: 708c770f0151ffcaad83730381e3e2ebafb84ceb
last_modified_at: 2024-04-18
related_topics:
  - title: français version
    url: /fr/common/pipenv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pipenv

Simple and unified Python development workflow.
Manage packages and the virtual environment for a project.
More information: <https://pypi.org/project/pipenv>.

- Create a new project:

`pipenv`

- Create a new project using Python 3:

`pipenv --three`

- Install a package:

`pipenv install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Install all the dependencies for a project:

`pipenv install`

- Install all the dependencies for a project (including dev packages):

`pipenv install --dev`

- Uninstall a package:

`pipenv uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Start a shell within the created virtual environment:

`pipenv shell`

- Generate a `requirements.txt` (list of dependencies) for a project:

`pipenv lock --requirements`
