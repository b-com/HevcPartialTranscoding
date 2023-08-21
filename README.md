# HevcPartialTranscoding

Welcome to the HevcPartialTranscoding repository! This project contains the source code accompanying the paper titled "Low-Consumption Partial Transcoding by HEVC" submitted to IEEE Signal Processing Letters for review.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)
- [Limitations](#limitations)
- [Build Instructions](#build-instructions)
- [Contributing](#contributing)
- [License](#license)

## Introduction

HevcPartialTranscoding is a tool designed to [provide more details about what the project does and why it's valuable]. It aims to help users efficiently transcode HEVC-encoded videos while preserving specific segments of interest.

The code in this repository corresponds to the implementation of the techniques described in the paper "Low-Consumption Partial Transcoding by HEVC" submitted to IEEE Signal Processing Letters for review. The paper explores [briefly summarize the main contributions and findings of the paper].

## Features

To be completed...

## Usage

- `--TBRCtuStartX`, `--TBRCtuStartY`, `--TBRCtuEndX`, `--TBRCtuEndY`: The coordinates of the CTUs to be replaced. To disable, use -1 for all.
- `--InputFileReplaceContent`: Path to a .txt file containing the replace content. 

## Limitations

Please note that the current version of HevcPartialTranscoding has the following limitations:

- Only encoder prototype
- Replace content size has to be multiple of CTU size
- Replace conent only on Y channel
- To be completed...

We are actively working to address these limitations and provide a smoother experience in future updates.

## Build Instructions

For detailed build instructions, please refer to the [README_HM.md](./README_HM.md) file.

## Contributing

We welcome contributions to HevcPartialTranscoding! If you'd like to contribute, please follow these steps:

1. Fork the repository and set up a development environment.
2. Creating and submit pull requests

## License

To be completed...

---

For more information, check out our [documentation](link-to-documentation) and feel free to contact us at [mohsen.adoli@gmail.com].

For the paper "Low-Consumption Partial Transcoding by HEVC," please refer to: [TBD].
