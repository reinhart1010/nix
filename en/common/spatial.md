---
layout: page
title: common/spatial (English)
description: "A set of commands for managing and developing SpatialOS projects."
content_hash: 5293d4d9a3a9bc59b949b25517dec4601f7fc548
---
# spatial

A set of commands for managing and developing SpatialOS projects.
More information: <https://ims.improbable.io/products/spatialos>.

- Run this when you use a project for the first time:

`spatial worker build`

- Build workers for local deployment on Unity on macOS:

`spatial worker build --target=development --target=Osx`

- Build workers for local deployment on Unreal on Windows:

`spatial worker build --target=local --target=Windows`

- Deploy locally:

`spatial local launch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">launch_config</span>` --snapshot=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">snapshot_file</span>

- Launch a local worker to connect to your local deployment:

`spatial local worker launch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">worker_type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">launch_config</span>

- Upload an assembly to use for cloud deployments:

`spatial cloud upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">assembly_name</span>

- Launch a cloud deployment:

`spatial cloud launch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">assembly_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">launch_config</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deployment_name</span>

- Clean worker directories:

`spatial worker clean`
