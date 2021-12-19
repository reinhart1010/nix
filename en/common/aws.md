---
layout: page
title: common/aws (English)
description: "The official CLI tool for Amazon Web Services."
content_hash: 8e65f3ba899595b369864578538a4c519b0d1602
related_topics:
  - title: Deutsch version
    url: /de/common/aws.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/aws.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aws.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/aws.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws.html
    icon: bi bi-globe
---
# aws

The official CLI tool for Amazon Web Services.
Some subcommands such as `aws s3` have their own usage documentation.
More information: <https://aws.amazon.com/cli>.

- Configure the AWS Command-line:

`aws configure wizard`

- Configure the AWS Command-line using SSO:

`aws configure sso`

- See help text for the AWS command:

`aws `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` help`

- Get the caller identity (used to troubleshoot permissions):

`aws sts get-caller-identity`

- List AWS resources in a region and output in YAML:

`aws dynamodb list-tables --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us-east-1</span>` --output yaml`

- Use auto prompt to help with a command:

`aws iam create-user --cli-auto-prompt`

- Get an interactive wizard for an AWS resource:

`aws dynamodb wizard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_table</span>

- Generate a JSON CLI Skeleton (useful for infrastructure as code):

`aws dynamodb update-table --generate-cli-skeleton`
