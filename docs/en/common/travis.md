---
layout: page
title: common/travis (English)
description: "Command-line client to interface with Travis CI."
content_hash: f04d506a50260fa5db1f46c725b16e9959c6a884
---
# travis

Command-line client to interface with Travis CI.
More information: <https://github.com/travis-ci/travis.rb>.

- Display the client version:

`travis version`

- Authenticate the CLI client against the server, using an authentication token:

`travis login`

- List repositories the user has permissions on:

`travis repos`

- Encrypt values in `.travis.yml`:

`travis encrypt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token</span>

- Generate a `.travis.yml` file and enable the project:

`travis init`
