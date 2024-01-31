---
layout: page
title: common/aws-cloud9 (English)
description: "Manage Cloud9 - a collection of tools to code, build, run, test, debug, and release software in the cloud."
content_hash: deaa14ccaec765e70bb4bede391632afb23509e2
last_modified_at: 2024-01-31
related_topics:
  - title: 한국어 version
    url: /ko/common/aws-cloud9.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws cloud9

Manage Cloud9 - a collection of tools to code, build, run, test, debug, and release software in the cloud.
More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/index.html>.

- List all Cloud9 development environment identifiers:

`aws cloud9 list-environments`

- Create a Cloud9 development environment:

`aws cloud9 create-environment-ec2 --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --instance-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instance_type</span>

- Display information about Cloud9 development environments:

`aws cloud9 describe-environments --environment-ids `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment_ids</span>

- Add an environment member to a Cloud9 development environment:

`aws cloud9 create-environment-membership --environment-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment_id</span>` --user-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_arn</span>` --permissions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">permissions</span>

- Display status information for a Cloud9 development environment:

`aws cloud9 describe-environment-status --environment-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment_id</span>

- Delete a Cloud9 environment:

`aws cloud9 delete-environment --environment-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment_id</span>

- Delete an environment member from a development environment:

`aws cloud9 delete-environment-membership --environment-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment_id</span>` --user-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_arn</span>
