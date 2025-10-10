# Salesforce Data Cloud Data Kit Deployment Guide

This documentation provides a comprehensive guide for deploying **Salesforce Data Kits** between two distinct Salesforce Data Cloud instances.

It describes a repeatable, reliable, and automated deployment process using the Salesforce Command Line Interface (Salesforce CLI) and a manifest-driven methodology — one of the most modern and efficient approaches for managing and migrating Data Cloud assets.

This guide is intended for Salesforce professionals such as Administrators, Developers, and Deployment Specialists who have experience with Salesforce Metadata API, Salesforce CLI commands, and Data Cloud implementation workflows.

By following this documentation, teams can streamline their Data Kit deployment, reduce manual configuration errors, and establish a consistent DevOps process for Salesforce Data Cloud environments.

## Prerequisites

Before beginning the deployment, ensure the following requirements are met, as outlined in the [official Salesforce installation guide](https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/install.html):

* **Visual Studio Code** installed.
* **Salesforce Extension Pack** installed in Visual Studio Code.
* **Salesforce CLI** installed and configured.
* **Java Platform, Standard Edition Development Kit (JDK)** installed (versions 11, 17, or 21 supported by certain extensions).
* Appropriate permissions in both source and target Salesforce production instances.

<br>


## Step 1: Create a Data Kit

Begin by creating a Data Kit in the source instance. This step is crucial for capturing the required metadata for deployment, so ensure all necessary elements are included.

1. Log in to the **source Salesforce instance**.
2. Navigate to **Data Cloud Setup** > **Development Tools** > **Data Kit**.
3. Create a new Data Kit and include all **required elements**.
4. Review and adjust the **Publishing Sequence** if necessary.
5. Click the down arrow button located on the top of the page, and then select **Download Manifest File**. (`package.xml`) associated with the Data Kit.

> **Notes:**
>
> * The downloaded file is named `package.xml`.
> * This file's content serves as the metadata specification for retrieval and deployment.
> * Ensure all necessary components for the target org are included.
> * Retain a local backup of the manifest file.
>
<br>

---

## Step 2: Configure the Local Environment

In this step you set up your local development workspace in Visual Studio Code, generate a project skeleton with manifest support, and prepare the project manifest for subsequent deployment steps.

### A. Create a Project

1. Open **Visual Studio Code**.
2. Open the Command Palette by pressing `Ctrl + Shift + P` on Windows or `Cmd + Shift + P` on macOS.
3. Run `SFDX: Create Project with Manifest`.
4. Select the **Standard** project template.
5. Name the project and choose a local directory.

Visual Studio Code scaffolds a project structure, including a manifest folder with a starter `package.xml` file.

<br>

### B. Update the Manifest

1. Open the downloaded `package.xml` from your Data Kit.
2. Copy its content.
3. Replace the content of `manifest/package.xml` in your local project with the copied content.

<br>

### C. Authorize the Source Org

1. Open the Command Palette by pressing `Ctrl + Shift + P` on Windows or `Cmd + Shift + P` on macOS.
2. Run `SFDX: Authorize an Org`.
3. Select the environment type **Production**, **Sandbox** or **Custom** as appropriate.
4. Use `source` as the org alias.
5. Log in via the browser and grant access.

<br>

### D. Authorize the Target Org

1. Repeat the previous steps using `target` as the org alias.

> **Note:** The Salesforce CLI retains the authentication for subsequent commands.

<br>

---

## Step 3: Retrieve and Deploy the Metadata

This step uses the manifest file (`package.xml`) you updated to retrieve the Data Kit metadata from the **source org** and then deploy it to the **target org**.

### A. Retrieve Metadata from the Source Instance

First, set your **source** org as the default for the project and execute the retrieve command.

1. Open the Command Palette by pressing `Ctrl + Shift + P` on Windows or `Cmd + Shift + P` on macOS.
2. Run `SFDX: Set a Default Org`.
3. Choose your `source` intance.
4. Open the terminal in Visual Studio Code.
5. Execute the following command:

```bash
sf project retrieve start --manifest manifest/package.xml
```

This command triggers metadata retrieval. After a few moments, your Data Kit metadata is retrieved, and the components specified in the manifest will be downloaded into the local project.

### B. Deploy Metadata to Target Org

Next, change the default org to your **target** instance to deploy the retrieved metadata.

1. Open the Command Palette again by pressing `Ctrl + Shift + P` on Windows or `Cmd + Shift + P` on macOS.
2. Run`SFDX: Set a Default Org`.
3. Choose your `target` instance.
4. In the terminal, execute the following command:

```bash
sf project deploy start --manifest manifest/package.xml
```

This command pushes the retrieved Data Kit metadata from your local machine to the target Salesforce instance, completing the deployment.

<br>

---

## Step 4: Install the Data Kit Components

Integrations must be authenticated before installation. You must successfully authenticate all integrations created by the Data Kit in the target instance to ensure the deployment succeeds.

1. Log in to the target Salesforce instance.
2. Navigate to **Data Cloud Setup**, then **Development Tools**, and finally the **Data Kit** page.
3. Locate the Data Kit you just deployed and click its name.
4. On the Data Kit detail page, click the **Deploy Data Kit** button.

Once complete, the Data Kit's status will update, and the required Data Cloud components will be fully provisioned in your target environment.

<br>

---

## References

* [Salesforce CLI Installation Guide](https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/install.html)
* [Salesforce Data Cloud Documentation](https://developer.salesforce.com/docs/atlas.en-us.mc-apis.meta/mc-apis/data_cloud.htm)
