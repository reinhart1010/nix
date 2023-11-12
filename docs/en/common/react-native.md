---
layout: page
title: common/react-native (English)
description: "A framework for building native apps with React."
content_hash: 20231c088a1db5de10dab0b8d59203a5051b6838
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# react-native

A framework for building native apps with React.
More information: <https://reactnative.dev>.

- Initialize a new React Native project in a directory of the same name:

`react-native init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>

- Start the metro bundler:

`react-native start`

- Start the metro bundler with a clean cache:

`react-native start --reset-cache`

- Build the current application and start it on a connected Android device or emulator:

`react-native run-android`

- Build the current application and start it on an iOS simulator:

`react-native run-ios`

- Build the current application in `release` mode and start it on a connected Android device or emulator:

`react-native run-android --variant=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">release</span>

- Start `logkitty` and print logs to `stdout`:

`react-native log-android`

- Start `tail system.log` for an iOS simulator and print logs to `stdout`:

`react-native log-ios`
