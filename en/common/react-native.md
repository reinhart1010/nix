---
layout: page
title: common/react-native (English)
description: "A framework for building native apps with React."
content_hash: 7f0778b345b5ae969db748a32f0133fb9560397a
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

- Start `logkitty` and print logs to stdout:

`react-native log-android`

- Start `tail system.log` for an iOS simulator and print logs to stdout:

`react-native log-ios`
