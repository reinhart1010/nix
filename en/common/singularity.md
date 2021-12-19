---
layout: page
title: common/singularity (English)
description: "Manage Singularity containers and images."
content_hash: ec05449d445b25d6c15ee327568b7a6b323c25ac
---
# singularity

Manage Singularity containers and images.

- Download a remote image from Sylabs Cloud:

`singularity pull --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.sif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">library://godlovedc/funny/lolcow:latest</span>

- Rebuild a remote image using the latest Singularity image format:

`singularity build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.sif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">docker://godlovedc/lolcow</span>

- Start a container from an image and get a shell inside it:

`singularity shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.sif</span>

- Start a container from an image and run a command:

`singularity exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.sif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Start a container from an image and execute the internal runscript:

`singularity run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.sif</span>

- Build a singularity image from a recipe file:

`sudo singularity build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.sif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">recipe</span>
