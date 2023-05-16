---
layout: page
title: common/aws-cloudformation (English)
description: "Model, provision, and manage AWS and third-party resources by treating infrastructure as code."
content_hash: bfdbd47f88452b8e336dff10cc1429001aea2918
last_modified_at: 2023-05-16
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aws cloudformation

Model, provision, and manage AWS and third-party resources by treating infrastructure as code.
More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html>.

- Create a stack from a template file:

`aws cloudformation create-stack --stack-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stack-name</span>` --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">region</span>` --template-body `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file://path/to/file.yml</span>` --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile</span>

- Delete a stack:

`aws cloudformation delete-stack --stack-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stack-name</span>` --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile</span>

- List all stacks:

`aws cloudformation list-stacks --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile</span>

- List all running stacks:

`aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile</span>

- Check the status of a stack:

`aws cloudformation describe-stacks --stack-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stack-id</span>` --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile</span>

- Initiate drift detection for a stack:

`aws cloudformation detect-stack-drift --stack-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stack-id</span>` --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile</span>

- Check the drift status output of a stack using 'StackDriftDetectionId' from the previous command output:

`aws cloudformation describe-stack-resource-drifts --stack-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stack-drift-detection-id</span>` --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile</span>
