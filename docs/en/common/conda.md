---
layout: page
title: common/conda (English)
description: "Package, dependency and environment management for any programming language."
content_hash: 784fa189f872b53d404e3ef45fb677b65f0babb3
related_topics:
  - title: italiano version
    url: /it/common/conda.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/conda.html
    icon: bi bi-globe
---
# conda

Package, dependency and environment management for any programming language.
Some subcommands such as `conda create` have their own usage documentation.
More information: <https://github.com/conda/conda>.

- Create a new environment, installing named packages into it:

`conda create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">python=3.9 matplotlib</span>

- List all environments:

`conda info --envs`

- Load an environment:

`conda `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">activate environment_name</span>

- Unload an environment:

`conda `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deactivate</span>

- Delete an environment (remove all packages):

`conda remove --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment_name</span>` --all`

- Install packages into the current environment:

`conda install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">python=3.4 numpy</span>

- List currently installed packages in current environment:

`conda list`

- Delete unused packages and caches:

`conda clean --all`
