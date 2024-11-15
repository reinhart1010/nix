---
layout: page
title: common/npm-bugs (English)
description: "Report bugs for a package in a web browser."
content_hash: 5e0361dc19af90bc61383761a09e808209a878c3
last_modified_at: 2024-11-15
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/npm-bugs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># npm bugs

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
