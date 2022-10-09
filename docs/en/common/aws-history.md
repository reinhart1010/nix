---
layout: page
title: common/aws-history (English)
description: "Print the command-line history for AWS CLI commands (the record of history of AWS CLI commands must be enabled)."
content_hash: 315f2769554f9114e4369bdb59e3f2373ebdb099
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aws history

Print the command-line history for AWS CLI commands (the record of history of AWS CLI commands must be enabled).
More information: <https://docs.aws.amazon.com/cli/latest/reference/history/>.

- List commands history with command IDs:

`aws history list`

- Display events related to a specific command given a command ID:

`aws history show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_id</span>
