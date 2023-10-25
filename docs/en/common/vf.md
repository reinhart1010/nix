---
layout: page
title: common/vf (English)
description: "VirtualFish is a fish shell tool for managing Python virtual environments."
content_hash: 97143d3edb9e74015f56eacc3dac89a04e4f9ed9
last_modified_at: 2023-10-25
---
# vf

VirtualFish is a fish shell tool for managing Python virtual environments.
More information: <https://virtualfish.readthedocs.io/en/latest/>.

- Create a virtual environment:

`vf new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">virtualenv_name</span>

- Create a virtual environment for a specific Python version:

`vf new --python `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/local/bin/python3.8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">virtualenv_name</span>

- Activate and use the specified virtual environment:

`vf activate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">virtualenv_name</span>

- Connect the current virtualenv to the current directory, so that it is activated automatically as soon as you enter it (and deactivated as soon as you leave):

`vf connect`

- Deactivate the current virtual environment:

`vf deactivate`

- List all virtual environments:

`vf ls`

- Remove a virtual environment:

`vf rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">virtualenv_name</span>

- Display help:

`vf help`
