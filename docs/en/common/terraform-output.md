---
layout: page
title: common/terraform-output (English)
description: "Export structured data about your Terraform resources."
content_hash: 0a95579fef1b33d27049a4a3c9d9a0300749f9b1
last_modified_at: 2024-07-11
tldri18n_status: 2
---
# terraform output

Export structured data about your Terraform resources.
More information: <https://developer.hashicorp.com/terraform/cli/commands/output>.

- With no additional arguments, `output` will display all outputs for the root module:

`terraform output`

- Output only a value with specific name:

`terraform output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Convert the output value to a raw string (useful for shell scripts):

`terraform output -raw`

- Format the outputs as a JSON object, with a key per output (useful with jq):

`terraform output -json`
