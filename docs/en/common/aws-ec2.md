---
layout: page
title: common/aws-ec2 (English)
description: "CLI for AWS EC2."
content_hash: 63f65f4af71ef0f7fb5096445dfdc82273f23a7c
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/aws-ec2.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-ec2.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-ec2.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws ec2

CLI for AWS EC2.
Provides secure and resizable computing capacity in the AWS cloud to enable faster development and deployment of applications.
More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html>.

- Display information about a specific instance:

`aws ec2 describe-instances --instance-ids `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instance_id</span>

- Display information about all instances:

`aws ec2 describe-instances`

- Display information about all EC2 volumes:

`aws ec2 describe-volumes`

- Delete an EC2 volume:

`aws ec2 delete-volume --volume-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_id</span>

- Create a snapshot from an EC2 volume:

`aws ec2 create-snapshot --volume-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_id</span>

- List available AMIs (Amazon Machine Images):

`aws ec2 describe-images`

- Show list of all available EC2 commands:

`aws ec2 help`

- Show help for specific EC2 subcommand:

`aws ec2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` help`
