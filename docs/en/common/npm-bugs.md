---
layout: page
title: common/npm-bugs (English)
description: "Report bugs for a package in a web browser."
content_hash: 5e0361dc19af90bc61383761a09e808209a878c3
last_modified_at: 2024-11-16
tldri18n_status: 2
---
# npm bugs

Report bugs for a package in a web browser.
Attempts to open the package's bug tracker URL or support email.
More information: <https://docs.npmjs.com/cli/npm-bugs>.

- Report bugs for a specific package by opening the bug tracker for the specified package:

`npm bugs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Open the bug tracker for the current package by searching for a `package.json` file and using its name:

`npm bugs`

- Configure the browser used to open URLs by setting your preferred browser for `npm` commands:

`npm config set browser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">browser_name</span>

- Control URL opening: set `browser` to `true` for the system URL opener, or `false` to print URLs in the terminal:

`npm config set browser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true|false</span>
