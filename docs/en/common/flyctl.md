---
layout: page
title: common/flyctl (English)
description: "Command-line tool for flyctl.io."
content_hash: 13571e8b7d9880e1f8a10939c07b460fbf80358c
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# flyctl

Command-line tool for flyctl.io.
More information: <https://github.com/superfly/flyctl>.

- Sign into a Fly account:

`flyctl auth login`

- Launch an application from a specific Dockerfile (the default path is the current working directory):

`flyctl launch --dockerfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/dockerfile</span>

- Open the current deployed application in the default web browser:

`flyctl open`

- Deploy the Fly applications from a specific Dockerfile:

`flyctl deploy --dockerfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/dockerfile</span>

- Open the Fly Web UI for the current application in a web browser:

`flyctl dashboard`

- List all applications in the logged-in Fly account:

`flyctl apps list`

- View the status of a specific running application:

`flyctl status --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_name</span>

- Show version information:

`flyctl version`
