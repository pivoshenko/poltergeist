# Contributing

- [Contributing](#contributing)
  - [Reporting Bugs](#reporting-bugs)
    - [How Do I Submit a Bug Report?](#how-do-i-submit-a-bug-report)
  - [Suggesting Enhancements](#suggesting-enhancements)
    - [How Do I Submit A Suggested Enhancement?](#how-do-i-submit-a-suggested-enhancement)
  - [Code Contributions](#code-contributions)
    - [Local Development](#local-development)
    - [Pull Requests](#pull-requests)

First, thank you for taking the time to contribute!

The following guidelines are for contributing to `poltergeist`. These are mostly guidelines, not strict rules. Use your best judgement, and feel free to propose changes to this document in a pull request.

## Reporting Bugs

This section guides you through submitting a bug report for `poltergeist`. Following these guidelines will help maintainers and the community understand your report, reproduce the behaviour, and find related reports.

Before submitting bug reports, please check if your issue already exists in the issue tracker. When creating a bug report, please include as many details as possible. Filling out the required template will help maintainers resolve the issue faster.

> [!NOTE]
> If you find a **Closed** issue that seems like the one you're experiencing, open a new issue and include a link to the original issue in the body of your report.

### How Do I Submit a Bug Report?

Bugs concerning `poltergeist` should be submitted to the main issue tracker using the appropriate issue template.

Please follow these steps to explain the problem clearly and make it easier for others to search for and understand:

- Use a clear and descriptive title to identify the issue
- Describe the exact steps to reproduce the problem in as much detail as possible
- Explain the observed behaviour after following the steps, and how it indicates a bug
- Describe the expected behaviour and why you think the current behaviour is incorrect

Provide detailed steps to reproduce your issue:

- Include your example repository, ensuring private information (like private package repositories or names) is removed
- Provide specific examples, such as an example repository or a sequence of steps in a container, to demonstrate the problem
- If the issue is not consistently reproducible, explain how often it occurs and under which conditions it tends to happen

Additional context can help:

- Did the problem start after an update (e.g., to a new version of `poltergeist`), or was it always present?
- If the problem started recently, can you reproduce it in an older version? Which version was the last working one?
- Are there any unusual aspects of your environment (e.g., special container images or Apple Silicon CPUs)?

Include details about your environment:

- Which version of Python is being used?
- What’s the name and version of your operating system?

To help others understand and reproduce your issue, provide thorough reproduction steps. If possible, ensure others can reproduce the issue in a pristine container or VM and share the steps you performed in that environment.

## Suggesting Enhancements

This section provides guidance on submitting enhancement suggestions for `poltergeist`, including entirely new features and improvements to existing functionality. Following these guidelines will help maintainers and the community understand your suggestion and identify related suggestions.

Before creating an enhancement suggestion, please check this list to see if your suggestion already exists. When submitting an enhancement, include as many details as possible, and fill out the template with steps you would take if the requested feature were implemented.

### How Do I Submit A Suggested Enhancement?

Enhancement suggestions should be submitted to the main issue tracker, using the appropriate issue template.

- Use a clear and descriptive title for the suggestion
- Provide a detailed description of the proposed enhancement, with specific steps or examples when possible
- Describe the current behaviour and explain the behaviour you would like to see, and why

## Code Contributions

### Local Development

First, fork the `poltergeist` repository and clone it locally to make pull requests against the project.

If you're new to `git` and pull request-based development, GitHub offers a helpful [guide](https://docs.github.com/en/get-started/quickstart/contributing-to-projects).

Next, install dependencies and run the test suite to ensure everything is working as expected:

```shell
uv sync
uv run poe test
```

When contributing to `poltergeist`, automated tools will be run to ensure your code is mergeable. You must make sure your code passes type checks and is formatted properly:

```shell
uv run poe format
uv run poe lint
```

> [!IMPORTANT]
> Your code must always be accompanied by corresponding tests. Code without tests will not be merged.

### Pull Requests

- Fill out the pull request description completely and accurately, ensuring it reflects the final changes and potential changelog entry
- Ensure your pull request includes tests that cover the changed or added code. Code without tests will not be merged
- Make sure your pull request passes all checks. You can run these tools locally to verify this
- If your changes affect the documentation, ensure the pull request also updates the documentation. Review the documentation preview generated by CI for any rendering issues

> [!NOTE]
> Make sure your branch is rebased against the latest `main` branch. Maintainers may ask you to update your branch before merging (especially if there have been CI changes on `main`), and to resolve any conflicts.

All pull requests will be accepted into the `main` branch unless otherwise instructed. Maintainers will decide if backports to other branches are needed and will handle them accordingly.
