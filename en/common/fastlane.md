---
layout: page
title: common/fastlane (English)
description: "Build and release mobile applications from the command-line."
content_hash: 84852104d6ca9b7636c38dd8259cfccf60771e3c
---
# fastlane

Build and release mobile applications from the command-line.
More information: <https://docs.fastlane.tools/actions/>.

- Build and sign the iOS application in the current directory:

`fastlane run build_app`

- Run `pod install` for the project in the current directory:

`fastlane run cocoapods`

- Delete the derived data from Xcode:

`fastlane run clear_derived_data`

- Remove the cache for pods:

`fastlane run clean_cocoapods_cache`
