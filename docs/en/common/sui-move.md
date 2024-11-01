---
layout: page
title: common/sui-move (English)
description: "Work with Move source code."
content_hash: f8ef6c0d7128f969ff822a321e581463dcc5d6f8
last_modified_at: 2024-11-01
tldri18n_status: 2
---
# sui move

Work with Move source code.
More information: <https://docs.sui.io/references/cli/move>.

- Create a new Move project in the given folder:

`sui move new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>

- Test the Move project in the current directory:

`sui move test`

- Test with coverage and get a summary:

`sui move test --coverage; sui move coverage summary`

- Find which parts of your code are covered from tests (i.e. explain coverage results):

`sui move coverage source --module `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Build the Move project in the current directory:

`sui move build`

- Build the Move project from the given path:

`sui move build --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path</span>

- Migrate to Move 2024 for the package at the provided path:

`sui move migrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path</span>
