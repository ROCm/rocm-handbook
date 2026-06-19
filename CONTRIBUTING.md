<head>
  <meta charset="UTF-8">
  <meta name="description" content="Contributing to ROCm handbook">
  <meta name="keywords" content="ROCm handbook, contributing, contribute, maintainer, contributor">
</head>

# Contribute to ROCm handbook

AMD values and encourages contributions to the ROCm handbook. If you want to contribute,
first review the following guidance. For general documentation conventions, see
[Contributing to ROCm docs](https://rocm.docs.amd.com/en/latest/contribute/contributing.html).

The ROCm handbook is a book-style reference for ROCm and HIP. It aggregates documentation from
the ROCm portal and organizes it into a structured format optimized for in-depth study and offline
access, published in both PDF and HTML.

This repository is the landing index for the handbook. It does not host content directly. Each
handbook volume is maintained in its own repository and published as a separate documentation
project. To contribute to a volume's content, open your pull request against that volume's
repository. Use this repository for changes to the index, the shared build setup, or the list of
volumes.

## Development workflow

The ROCm handbook uses GitHub to host content, collaborate, and manage version control. We use pull
requests (PRs) for all changes. We use
[GitHub issues](https://github.com/ROCm/rocm-handbook/issues) to track known issues, such as errors
or gaps in the documentation.

### Issue tracking

Before filing a new issue, search the
[existing issues](https://github.com/ROCm/rocm-handbook/issues) to make sure your issue isn't
already listed.

General issue guidelines:

* Use your best judgement for issue creation. If your issue is already listed, upvote the issue and
  comment to provide additional details, such as the page affected and how to reproduce the problem.
* If you're not sure whether your issue is the same, err on the side of caution and file your issue.
  You can add a comment that includes the issue number (and link) for the similar issue. If we
  evaluate your issue as being the same as the existing issue, we'll close the duplicate.
* If your issue doesn't exist, use the issue template to file a new issue.
  * When filing an issue, provide as much information as possible, such as the affected page or
    section, the volume, and a description of the expected and actual content. This helps reduce the
    time required to address your issue.
  * Check your issue regularly, as we may require additional information.

### Pull requests

When you create a pull request, target the **main** branch.

When creating a PR, use the following process. Note that an individual volume's repository may
include additional, project-specific steps. Refer to that repository's PR process for any additional
steps.

* Identify the issue you want to fix.
* Target the **main** branch for integration.
* Build the documentation locally and confirm it builds without errors or warnings. See
  [Build the documentation](README.md#build-the-documentation) for instructions.
* Review the rendered HTML output to verify your changes display as intended.
* Check that internal links resolve and code examples are accurate.
* Submit your PR and work with the reviewer or maintainer to get it approved.
* Once approved, the maintainer merges your change and it is included in the next published build.
* We'll inform you once your change is committed.

> [!IMPORTANT]
> By creating a PR, you agree to allow your contribution to be licensed under the
> terms of the LICENSE file in this repository.

You can look up each license on the [ROCm licensing](https://rocm.docs.amd.com/en/latest/about/license.html) page.

### Proposing new content

Use the [GitHub Discussion forum](https://github.com/ROCm/rocm-handbook/discussions)
(Ideas category) to propose new volumes, chapters, or significant restructuring. Our maintainers are
happy to provide direction and feedback before you begin work.

### Writing conventions

Match the style and structure of the existing handbook content. The handbook follows the
[ROCm documentation conventions](https://rocm.docs.amd.com/en/latest/contribute/contributing.html),
including second-person voice, sentence case headings, and language tags on all code blocks. Because
the handbook aggregates content from the ROCm portal, keep contributions consistent with the upstream
source where applicable, and prefer evergreen wording over version-specific details.

## Future development workflow

The current ROCm handbook workflow is GitHub-based. If, in the future, we change this platform, the
tools and links may change. In this instance, we will update these contribution guidelines
accordingly.
