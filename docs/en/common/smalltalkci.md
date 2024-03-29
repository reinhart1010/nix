---
layout: page
title: common/smalltalkci (English)
description: "Framework for testing Smalltalk projects with GitHub Actions, Travis CI, AppVeyor, GitLab CI, and others."
content_hash: 7f878d6499c7c8ce55bc121b4d12647d74b1f22a
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# smalltalkci

Framework for testing Smalltalk projects with GitHub Actions, Travis CI, AppVeyor, GitLab CI, and others.
More information: <https://github.com/hpi-swa/smalltalkCI>.

- Run tests for a configuration file:

`smalltalkci `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/.smalltalk.ston</span>

- Run tests for the `.smalltalk.ston` configuration in the current directory:

`smalltalkci`

- Debug tests in headful mode (show VM window):

`smalltalkci --headful`

- Download and prepare a well-known smalltalk image for the tests:

`smalltalkci --smalltalk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Squeak64-Trunk</span>

- Specify a custom Smalltalk image and VM:

`smalltalkci --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/Smalltalk.image</span>` --vm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/vm</span>

- Clean up caches and delete builds:

`smalltalkci --clean`
