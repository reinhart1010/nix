---
layout: page
title: common/cdk (English)
description: "A CLI for AWS Cloud Development Kit (CDK)."
content_hash: af2b98e45c7fa1c4f5f8c2c0ebd58b935b210bfc
---
# cdk

A CLI for AWS Cloud Development Kit (CDK).
More information: <https://docs.aws.amazon.com/cdk/latest/guide/cli.html>.

- List the stacks in the app:

`cdk ls`

- Synthesize and print the CloudFormation template for the specified stack(s):

`cdk synth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stack_name</span>

- Deploy a space-separated list of stacks:

`cdk deploy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stack_name</span>

- Destroy a space-separated list of stacks:

`cdk destroy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stack_name</span>

- Compare the specified stack with the deployed stack or a local CloudFormation template:

`cdk diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stack_name</span>

- Create a new CDK project in the current directory for a specified language:

`cdk init -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">language_name</span>

- Open the CDK API reference in your browser:

`cdk docs`
