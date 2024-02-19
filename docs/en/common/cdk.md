---
layout: page
title: common/cdk (English)
description: "A CLI for AWS Cloud Development Kit (CDK)."
content_hash: dcbaf827a920dd2ae97e83047329e3cf6d347fc6
last_modified_at: 2024-02-19
tldri18n_status: 2
---
# cdk

A CLI for AWS Cloud Development Kit (CDK).
More information: <https://docs.aws.amazon.com/cdk/latest/guide/cli.html>.

- List the stacks in the app:

`cdk ls`

- Synthesize and print the CloudFormation template for the specified stack(s):

`cdk synth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stack_name</span>

- Deploy one or more stacks:

`cdk deploy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stack_name1 stack_name2 ...</span>

- Destroy one or more stacks:

`cdk destroy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stack_name1 stack_name2 ...</span>

- Compare the specified stack with the deployed stack or a local CloudFormation template:

`cdk diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stack_name</span>

- Create a new CDK project in the current directory for a specified [l]anguage:

`cdk init -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">language</span>

- Open the CDK API reference in your browser:

`cdk docs`
