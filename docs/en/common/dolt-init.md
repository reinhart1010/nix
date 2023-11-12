---
layout: page
title: common/dolt-init (English)
description: "Create an empty Dolt data repository."
content_hash: b0627bd12bc00b6c495be02ea7626eec58d5505f
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# dolt init

Create an empty Dolt data repository.
More information: <https://docs.dolthub.com/cli-reference/cli#dolt-init>.

- Initialize a new Dolt data repository in the current directory:

`dolt init`

- Initialize a new Dolt data repository creating a commit with the specified metadata:

`dolt init --name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`" --email "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email</span>`" --date "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2021-12-31T00:00:00</span>`" -b "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>`"`
