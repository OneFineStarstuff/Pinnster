# Zenodo Release Guide for Omni-Sentinel

To ensure this software is properly archived and citable with a DOI, follow these steps to create a release on Zenodo.

## 1. Automated Integration (Recommended)
Zenodo integrates directly with GitHub. To enable this:
1. Log in to [Zenodo](https://zenodo.org/) using your GitHub account.
2. Navigate to the [GitHub integration page](https://zenodo.org/account/settings/github/).
3. Find the `onefinestarstuff/omni-sentinel` repository and flip the switch to **On**.
4. Create a new Release on GitHub (e.g., `v1.0.0`).
5. Zenodo will automatically archive the repository and assign a DOI.

## 2. Manual Upload
If GitHub integration is not used:
1. Go to [Zenodo Upload](https://zenodo.org/deposit/new).
2. Upload the source code archive (ZIP or TAR.GZ).
3. Zenodo will automatically parse metadata from `CITATION.cff` and `codemeta.json` if they are included in the archive.
4. Review the metadata (Title, Authors, Description, License) and click **Publish**.

## 3. Metadata Files
The following files in the repository root support the Zenodo release:
- `CITATION.cff`: Standard citation format for researchers.
- `codemeta.json`: Structured JSON-LD metadata for software indexing.
- `LICENSE`: MIT License information.

## 4. Verification
Once published, update the `README.md` with the new DOI badge provided by Zenodo.

---
*Authorized by Omni-Sentinel Governance Board.*
