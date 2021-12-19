---
layout: page
title: common/terraform-fmt (English)
description: "Format configuration according to Terraform language style conventions."
content_hash: 2c0efde8ff89eaef8be8273604904d8ff92e4bb6
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

- Do not list files that were formatted to stdout:

`terraform fmt -list=false`
