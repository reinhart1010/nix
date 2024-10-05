---
layout: page
title: common/conda (English)
description: "Package, dependency and environment management for any programming language."
content_hash: 4861df877273618aff88570fbcd86d5b0ae0d083
last_modified_at: 2024-10-05
related_topics:
  - title: Deutsch version
    url: /de/common/conda.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/conda.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/conda.html
    icon: bi bi-globe
tldri18n_status: 2
---
# conda

Package, dependency and environment management for any programming language.
Some subcommands such as `create` have their own usage documentation.
More information: <https://github.com/conda/conda>.

- Create a new environment, installing named packages into it:

`conda create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">python=3.9 matplotlib</span>

- List all environments:

`conda info --envs`

- Load an environment:

`conda activate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment_name</span>

- Unload an environment:

`conda deactivate`

- Delete an environment (remove all packages):

`conda remove --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment_name</span>` --all`

- Install packages into the current environment:

`conda install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">python=3.4 numpy</span>

- List currently installed packages in current environment:

`conda list`

- Delete unused packages and caches:

`conda clean --all`
