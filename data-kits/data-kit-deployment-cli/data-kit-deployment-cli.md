# Salesforce Data Cloud Data Kit Deployment Guide

This documentation provides a comprehensive guide for deploying **Salesforce Data Kits** between two distinct Salesforce Data Cloud instances.

It describes a repeatable, reliable, and automated deployment process using the Salesforce Command Line Interface (Salesforce CLI) and a manifest-driven methodology — one of the most modern and efficient approaches for managing and migrating Data Cloud assets.

This guide is intended for Salesforce professionals such as Administrators, Developers, and Deployment Specialists who have experience with Salesforce Metadata API, Salesforce CLI commands, and Data Cloud implementation workflows.

By following this documentation, teams can streamline their Data Kit deployment, reduce manual configuration errors, and establish a consistent DevOps process for Salesforce Data Cloud environments.

## Prerequisites

Prior to initiating the deployment process, ensure all the following requirements are satisfied, as detailed in the [official installation guide](https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/install.html):

- **Visual Studio Code** installed.
- **Salesforce Extension Pack** installed in Visual Studio Code.
- **Salesforce CLI** installed and correctly configured.
- **Java Platform, Standard Edition Development Kit (JDK)** installed. Note that some extensions require specific JDK versions – for instance, versions 11, 17, or 21 are supported.
- Appropriate permissions granted in both Salesforce production instances

<br>

---

### Step 1: Create a Data Kit

Begin by creating a Data Kit in the source instance. This step is crucial for capturing the required metadata for deployment, so ensure all necessary elements are included.

1. Log in to the **source Salesforce instance**.
2. Navigate to **Data Cloud Setup**, then **Development Tools**, and finally the **Data Kit** page.
3. Create a new Data Kit and include all **required elements**.
4. Review the **Publishing Sequence** and adjust it if necessary.
5. Click the down arrow and then Download the Manifest file `package.xml` associated with the Data Kit.

<small>
Notes:

- Ensure that every component needed in the target instance is included in the Data Kit.
- The manifest file `package.xml` will act as the metadata spec for retrieval and deployment steps.
- Adjust the publishing sequence only if dependency ordering matters.
- After downloading the manifest, retain a backup copy locally.
  </small>

---

### Step 2: Configure the environment

In this step you set up your local development workspace in Visual Studio Code, generate a project skeleton with manifest support, and prepare the project manifest for subsequent deployment steps.

#### (A) Create the project

1. Open **Visual Studio Code**.
2. Open the Command Palette by pressing `Ctrl + Shift + P` on Windows or `Cmd + Shift + P` on macOS.
3. Type `SFDX: Create Project with Manifest` and press Enter.
4. Select the **Standard** project template.
5. Enter a project name for your local workspace.
6. Select the local directory where you want to create the project. Visual Studio Code scaffolds a project structure, including a manifest folder with a starter `package.xml` file.

---

#### (B) Update the `package.xml` file

1. Open the downloaded `package.xml` file from your Data Kit and copy its content.
2. In your new local project, open the generated manifest file at `manifest/package.xml`.
3. Replace the existing content in this file with the content you copied.

---

#### (C) Authorize the Source Org

1. Open the Command Palette by pressing `Ctrl + Shift + P` on Windows or `Cmd + Shift + P` on macOS.
2. Type `SFDX: Authorize an Org` and press Enter.
3. Select the environment type **Production**, **Sandbox** or **Custom** as appropriate.
4. Type `source` as the alias for your org and press Enter.
5. A new window will open in your default browser. Enter your login credentials for the source organization and Allow Access to grant the required permissions.
6. Once validated, close the browser window and go back to Visual Studio Code.

---

#### (D) Authorize the Target Org

1. Repeat steps 1-3.
2. Type `target` as the alias for your org and press Enter.
3. Complete the login process in your browser for the target organization.

<br>

**Note**: Upon successful login and approval, the org is authorized and the Salesforce CLI retains the authentication association.

---

### Step 3: Retrieve and Deploy the Metadata

This step uses the manifest file (`package.xml`) you updated to retrieve the Data Kit metadata from the **source org** and then deploy it to the **target org**.

#### (A) Retrieve Metadata from the Source Instance

First, set your **source** org as the default for the project and execute the retrieve command.

1. Open the Command Palette by pressing `Ctrl + Shift + P` on Windows or `Cmd + Shift + P` on macOS.
2. Type `SFDX: Set a Default Org` and press Enter.
3. Choose your `source` intance.
4. Open the Command Palette by pressing `Ctrl + Shift + P` on Windows or `Cmd + Shift + P` on macOS.
5. Type `Terminal: Focus on Terminal View` and press Enter.
6. In the terminal, paste the following code: `sf project retrieve start --manifest manifest/package.xml`

This will trigger the metadata retrievement. After some instance, you will have your Data Kit metadata retrieved.

---

#### (B) Deploy Metadata to Target Org

Next, change the default org to your **target** instance to deploy the retrieved metadata.

1. Open the Command Palette again by pressing `Ctrl + Shift + P` on Windows or `Cmd + Shift + P` on macOS.
2. Type or select `SFDX: Set a Default Org`.
3. Choose your `target` instance.
4. In the terminal, execute the following command: `sf project deploy start --manifest manifest/package.xml`.

This command pushes the retrieved Data Kit metadata from your local machine to the target Salesforce instance, completing the deployment.

---

### Step 4: Deploy Data Kit

Authentication is required prior to deployment. You must successfully authenticate all integrations created by the Data Kit in the target instance to ensure the deployment succeeds.

1. Log in to the target Salesforce instance.
2. Navigate to **Data Cloud Setup**, then **Development Tools**, and finally the **Data Kit** page.
3. Locate the Data Kit you just deployed and click its name.
4. On the Data Kit detail page, click the **Deploy Data Kit** button.

Once complete, the Data Kit's status will update, and the required Data Cloud components will be fully provisioned in your target environment.
