---
layout: page
title: common/projucer (English)
description: "A project manager for JUCE framework applications."
content_hash: e6896ee2dad37ef348cc9dfa8007dd122683ce15
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# Projucer

A project manager for JUCE framework applications.
More information: <https://juce.com/discover/stories/projucer-manual#10.4-command-line-tools>.

- Display information about a project:

`Projucer --status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project_file</span>

- Resave all files and resources in a project:

`Projucer --resave `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project_file</span>

- Update the version number in a project:

`Projucer --set-version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version_number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project_file</span>

- Generate a JUCE project from a PIP file:

`Projucer --create-project-from-pip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/PIP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output</span>

- Remove all JUCE-style comments (`//=====`, `//-----` or `///////`):

`Projucer --tidy-divider-comments `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target_folder</span>

- Display help:

`Projucer --help`
