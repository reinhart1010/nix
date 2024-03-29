---
layout: page
title: common/aws-rds (English)
description: "Use AWS Relational Database Service, a web service for setting up, operating and scaling relational databases."
content_hash: df7af7113730701b28a6598d74c560cc5ff596db
last_modified_at: 2024-03-04
related_topics:
  - title: español version
    url: /es/common/aws-rds.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-rds.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws rds

Use AWS Relational Database Service, a web service for setting up, operating and scaling relational databases.
More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html>.

- Display help for a specific RDS subcommand:

`aws rds `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` help`

- Stop instance:

`aws rds stop-db-instance --db-instance-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instance_identifier</span>

- Start instance:

`aws rds start-db-instance --db-instance-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instance_identifier</span>

- Modify an RDS instance:

`aws rds modify-db-instance --db-instance-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instance_identifier</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parameters</span>` --apply-immediately`

- Apply updates to an RDS instance:

`aws rds apply-pending-maintenance-action --resource-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_arn</span>` --apply-action `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system-update</span>` --opt-in-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immediate</span>

- Change an instance identifier:

`aws rds modify-db-instance --db-instance-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">old_instance_identifier</span>` --new-db-instance-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_instance_identifier</span>

- Reboot an instance:

`aws rds reboot-db-instance --db-instance-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instance_identifier</span>

- Delete an instance:

`aws rds delete-db-instance --db-instance-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instance_identifier</span>` --final-db-snapshot-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">snapshot_identifier</span>` --delete-automated-backups`
