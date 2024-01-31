---
layout: page
title: common/conda-install (English)
description: "Install packages into an existing conda environment."
content_hash: ec24e361623a63aa699c505abe5bd98b8ab65b69
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# conda install

Install packages into an existing conda environment.
More information: <https://docs.conda.io/projects/conda/en/latest/commands/install.html>.

- Install one or more package into the currently active conda environment:

`conda install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- Install a single package into the currently active conda environment using channel conda-forge:

`conda install -c conda-forge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Install a single package into the currently active conda environment using channel conda-forge and ignoring other channels:

`conda install -c conda-forge --override-channels `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Install a specific version of a package:

`conda install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Install a package into a specific environment:

`conda install --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Update a package in the current environment:

`conda install --upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Install a package and agree to the transactions without prompting:

`conda install --yes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>
