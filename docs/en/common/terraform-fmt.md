---
layout: page
title: common/terraform-fmt (English)
description: "Format configuration according to Terraform language style conventions."
content_hash: 765e7fe75bb4dea1a33b3118db46685398d6ddae
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/terraform-fmt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# terraform fmt

Format configuration according to Terraform language style conventions.
More information: <https://www.terraform.io/docs/commands/fmt.html>.

- Format the configuration in the current directory:

`terraform fmt`

- Format the configuration in the current directory and subdirectories:

`terraform fmt -recursive`

- Display diffs of formatting changes:

`terraform fmt -diff`

- Do not list files that were formatted to `stdout`:

`terraform fmt -list=false`
