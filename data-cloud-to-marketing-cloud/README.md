## Exporting Data from Salesforce Data Cloud to Marketing Cloud

### Overview
This guide details how to export data from Salesforce Data Cloud to Marketing Cloud using Apex, Named Credentials, and Flow Builder.

### Prerequisites

A DMO (Data Model Object) in Data Cloud containing the records to export (e.g., Individual)
A target Data Extension in Marketing Cloud with a known External Key
The required credentials (Client ID and Secret) from Marketing Cloud

### Example Use Case
Export all Individual records from a DMO in Data Cloud and push them to a Data Extension in Marketing Cloud using its External Key.

### 1. Named Credential Configuration

Step 1: Create External Credential

Path: ```Setup > Named Credentials > External Credentials```

```
Label: MktCloudTokenEC  
Authentication Protocol: OAuth 2.0  
Authentication Flow Type: Client Credentials with Client Secret Flow  
Identity Provider URL: https://mc5htsz3sp-hs971l1lbdm0-whx0.auth.marketingcloudapis.com/v2/token  
Pass client credentials in request body: ✓ (Checked)

Principals Section:
Parameter Name: OAuth  
Sequence Number: 1  
Client ID: [MARKETING CLOUD CLIENT ID]  
Client Secret: [MARKETING CLOUD CLIENT SECRET]
```

Step 2: Create Named Credential

Path: ```Setup > Named Credentials > Named Credentials```

```
Label: MktCloudTokenNC  
URL: https://mc5htsz3sp-hs971l1lbdm0-whx0.rest.marketingcloudapis.com
Enabled for Callouts: ✓ (Checked)
External Credential: MktCloudTokenEC  
Generate Authorization Header: ✓ (Checked)
```

### 2. Permission Sets

Path: ```Setup > Users > Permission Sets > New```

```
Label: Named Credential Access
```
```Save```

Then go to:
```
External Credential Principal Access > Edit > 
Move "MktCloudTokenEC - OAuth" to Enabled External Credential Principals
```
⚠️ Important: After creating the permission set, make sure to assign it to the appropriate user.

### 3. Profile Access

Path: ```Setup > Users > Profiles > System Administrator```

```
Section: Enabled External Credential Principal Access > Edit > 
Move "MktCloudTokenEC - OAuth" to Enabled External Credential Principals
```

### 4. Process Automation Settings

Path: ```Setup > Process Automation > Process Automation Settings```

```
Set the "Default Workflow User" to an active user with permission to call Named Credentials
```

### 5. Create Flow to Trigger the Export

Path: ```Setup > Process Automation > Flows > New Flow```

1. Select Scheduled-Triggered Flow
2. Choose the Start Date, Time, and Frequency
3. Add Element → Action → Search for your Apex Action (e.g., "Data Cloud To Marketing Cloud")
4. Select the Action and set the Label
5. Save and Activate the Flow



