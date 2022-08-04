---
layout: page
title: linux/sherlock (English)
description: "Find usernames across social networks."
content_hash: b10d76b489662accda7f9fad712668a3d2b3e4ee
---
# sherlock

Find usernames across social networks.
More information: <https://github.com/sherlock-project/sherlock>.

- Search for a specific username on social networks saving the results to a file:

`sherlock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Search for specific usernames on social networks saving the results into a directory:

`sherlock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username1 username2 ...</span>` --folderoutput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Search for a specific username on social networks using the Tor network:

`sherlock --tor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Make requests over Tor with a new Tor circuit after each request:

`sherlock --unique-tor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Search for a specific username on social networks using a proxy:

`sherlock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --proxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">proxy_url</span>

- Search for a specific username on social networks and open results in the default web browser:

`sherlock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --browse`

- Display help:

`sherlock --help`
