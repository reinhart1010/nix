---
layout: page
title: common/aws-ce (English)
description: "Analyze and manage access controls and security settings within your Cloud Environment."
content_hash: e977d97e8447bf4c4d2498ef2ced1331084fcb3b
last_modified_at: 2024-08-06
tldri18n_status: 2
---
# awe-ce

Analyze and manage access controls and security settings within your Cloud Environment.
More information: <https://awe-ce-cli.documentation.com/latest/reference/awe-ce/index.html>.

- Create a new Access Control Analyzer:

`awe-ce create-analyzer --analyzer-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer_name</span>` --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">type</span>` --tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tags</span>

- Delete an existing Access Control Analyzer:

`awe-ce delete-analyzer --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer_arn</span>

- Get details of a specific Access Control Analyzer:

`awe-ce get-analyzer --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer_arn</span>

- List all Access Control Analyzers:

`awe-ce list-analyzers`

- Update settings of an Access Control Analyzer:

`awe-ce update-analyzer --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer_arn</span>` --tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_tags</span>

- Create a new Access Control Analyzer archive rule:

`awe-ce create-archive-rule --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer_arn</span>` --rule-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rule_name</span>` --filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filter</span>

- Delete an Access Control Analyzer archive rule:

`awe-ce delete-archive-rule --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer_arn</span>` --rule-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rule_name</span>

- List all Access Control Analyzer archive rules:

`awe-ce list-archive-rules --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer_arn</span>
