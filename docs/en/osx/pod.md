---
layout: page
title: osx/pod (English)
description: "Dependency manager for Swift and Objective-C Cocoa projects."
content_hash: 93af320fd3fd8d6899a261c1a272a9c072ab6517
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/osx/pod.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pod

Dependency manager for Swift and Objective-C Cocoa projects.
More information: <https://guides.cocoapods.org/terminal/commands.html>.

- Create a Podfile for the current project with the default contents:

`pod init`

- Download and install all pods defined in the Podfile (that haven't been installed before):

`pod install`

- List all available pods:

`pod list`

- Show the outdated pods (of those currently installed):

`pod outdated`

- Update all currently installed pods to their newest version:

`pod update`

- Update a specific (previously installed) pod to its newest version:

`pod update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod_name</span>

- Remove CocoaPods from a Xcode project:

`pod deintegrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xcode_project</span>
