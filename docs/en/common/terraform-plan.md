---
layout: page
title: common/terraform-plan (English)
description: "Generate and show Terraform execution plans."
content_hash: bdbcbf1198a91fc925efd6ba8ef892988bef6759
---
# terraform plan

Generate and show Terraform execution plans.
More information: <https://www.terraform.io/docs/cli/commands/plan.html>.

- Generate and show the execution plan in the currently directory:

`terraform plan`

- Show a plan to destroy all remote objects that currently exist:

`terraform plan -destroy`

- Show a plan to update the Terraform state and output values:

`terraform plan -refresh-only`

- Specify values for input variables:

`terraform plan -var '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name1</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value1</span>`' -var '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name2</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value2</span>`'`

- Focus Terraform's attention on only a subset of resources:

`terraform plan -target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_type.resource_name[instance index]</span>

- Output a plan as JSON:

`terraform plan -json`

- Write a plan to a specific file:

`terraform plan -no-color > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
