## Exporting Data from Salesforce Data Cloud to Marketing Cloud

### Overview
This guide explains how to send data from Salesforce Data Cloud to Marketing Cloud using Apex, Named Credentials and, Flow builder.

### Prerequisites

### Example Use Case
We want to export all Individual records from a DMO in Data Cloud and push them to a specific Data Extension in Marketing Cloud using its External Key.

### Named Credential

Setup > Named Credentials > External Credentials  

```
Label: MktCloudToken  
Authentication Protocol: OAuth 2.0  
Authentication Flow Type: Client Credentials with Client Secret Flow  
Identity Provider URL: https://mc5htsz3sp-hs971l1lbdm0-whx0.auth.marketingcloudapis.com/v2/token  
Pass client credentials in request body: Check  

Principals
Parameter Name: OAuth  
Sequence Number: 1  
Client ID: [CLIENT ID MARKETING CLOUD]  
Client Secret: [CLIENT SECRET MARKETING CLOUD]  
```

Setup > Named Credentials > Named Credentials  

```
Label: MktCloudToken  
URL: https://mc5htsz3sp-hs971l1lbdm0-whx0.rest.marketingcloudapis.com
Enabled for Callouts: Check  
External Credential: MktCloudToken  
Generate Authorization Header: Check 
```
