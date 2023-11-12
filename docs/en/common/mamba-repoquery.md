---
layout: page
title: common/mamba-repoquery (English)
description: "Efficiently query conda and mamba package repositories and package dependencies."
content_hash: a8e0dffb48fea18903ba0b1c137f5658f7c77f9b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# mamba repoquery

Efficiently query conda and mamba package repositories and package dependencies.
More information: <https://mamba.readthedocs.io/en/latest/user_guide/mamba.html#repoquery>.

- Search for all available versions of a particular package:

`mamba repoquery search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Search for all packages satisfying specific constraints:

`mamba repoquery search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sphinx<5</span>

- List the dependencies of a package installed in the currently activated environment, in a tree format:

`mamba repoquery depends --tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scipy</span>

- Print packages in the current environment that require a particular package to be installed (i.e. inverse of `depends`):

`mamba repoquery whoneeds `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ipython</span>
