---
layout: page
title: linux/autopkgtest (English)
description: "Run tests on Debian packages."
content_hash: 9d8049cff35264a76ae6d9c1a16d436bd65ae2cf
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# autopkgtest

Run tests on Debian packages.
More information: <https://wiki.debian.org/ContinuousIntegration/autopkgtest>.

- Build the package in the current directory and run all tests directly on the system:

`autopkgtest -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">null</span>

- Run a specific test for the package in the current directory:

`autopkgtest --test-name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test_name</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">null</span>

- Download and build a specific package with `apt-get`, then run all tests:

`autopkgtest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">null</span>

- Test the package in the current directory using a new root directory:

`autopkgtest -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chroot</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/new/root</span>

- Test the package in the current directory without rebuilding it:

`autopkgtest --no-built-binaries -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">null</span>
