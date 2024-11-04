---
layout: page
title: common/terraform-fmt (English)
description: "Format configuration according to Terraform language style conventions."
content_hash: 727fe14f1f68ee48b9fc6979f58be509c9dad459
last_modified_at: 2024-11-04
related_topics:
  - title: Deutsch version
    url: /de/common/terraform-fmt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# terraform fmt

Format configuration according to Terraform language style conventions.
More information: <https://developer.hashicorp.com/terraform/cli/commands/fmt>.

- Format the configuration in the current directory:

`terraform fmt`

- Format the configuration in the current directory and subdirectories:

`terraform fmt -recursive`

- Display diffs of formatting changes:

`terraform fmt -diff`

- Do not list files that were formatted to `stdout`:

`terraform fmt -list=false`
