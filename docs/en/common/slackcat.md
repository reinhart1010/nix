---
layout: page
title: common/slackcat (English)
description: "Utility for passing files and command output to Slack."
content_hash: 56848414ce674267dbd8c6f7caa62d14a9c9bb6e
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# slackcat

Utility for passing files and command output to Slack.
More information: <https://github.com/bcicen/slackcat>.

- Post a file to Slack:

`slackcat --channel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">channel_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Post a file to Slack with a custom filename:

`slackcat --channel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">channel_name</span>` --filename=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Pipe command output to Slack as a text snippet:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | slackcat --channel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">channel_name</span>` --filename=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">snippet_name</span>

- Stream command output to Slack continuously:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | slackcat --channel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">channel_name</span>` --stream`
