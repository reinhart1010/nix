---
layout: page
title: common/conda-create (English)
description: "Create new conda environments."
content_hash: 7efecf5530185b20c03edfe96b4543c14b28d1f5
---
# conda create

Create new conda environments.
More information: <https://docs.conda.io/projects/conda/en/latest/commands/create.html>.

- Create a new environment named `py39`, and install Python 3.9 and NumPy v1.11 or above in it:

`conda create --yes --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">py39</span>` python=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3.9</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numpy>=1.11</span>`"`

- Make exact copy of an environment:

`conda create --clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">py39</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">py39-copy</span>

- Create a new environment with a specified name and install a given package:

`conda create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">env_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>
