---
layout: page
title: common/bower (English)
description: "A package manager optimized for front-end web development."
content_hash: 6e4f19796c8dcf0d685448219aa9d1f277aa1ad2
related_topics:
  - title: italiano version
    url: /it/common/bower.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bower.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/bower.html
    icon: bi bi-globe
---
# bower

A package manager optimized for front-end web development.
A package can be a GitHub user/repo shorthand, a Git endpoint, a URL or a registered package.
More information: <https://bower.io/>.

- Install a project's dependencies, listed in its bower.json:

`bower install`

- Install one or more packages to the bower_components directory:

`bower install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Uninstall packages locally from the bower_components directory:

`bower uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- List local packages and possible updates:

`bower list`

- Display help information about a bower command:

`bower help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Create a `bower.json` file for your package:

`bower init`

- Install a specific dependency version, and add it to `bower.json`:

`bower install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_name</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>`#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>` --save`
