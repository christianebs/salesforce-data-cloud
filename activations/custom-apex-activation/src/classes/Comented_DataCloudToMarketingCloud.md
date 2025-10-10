# `DataCloudToMarketingCloud` Class

The `DataCloudToMarketingCloud` class is an Apex class in Salesforce designed to facilitate the transfer of data from a Salesforce Data Cloud to the Marketing Cloud. Here's a detailed explanation of its components and functionality.

## Purpose

The primary purpose of this class is to export records from a Salesforce Data Cloud object to the Marketing Cloud. It does this by implementing a queueable job, which allows for asynchronous processing, and by making HTTP callouts to an external endpoint.

## Key Components and Concepts

### Class Declaration

```java
public with sharing class DataCloudToMarketingCloud implements Queueable, Database.AllowsCallouts {
```

- **`public`**: The class is accessible from other classes.
- **`with sharing`**: Enforces the sharing rules that apply to the current user.
- **`implements Queueable`**: Indicates that this class can be used as a queueable job, which is a type of asynchronous Apex job.
- **`Database.AllowsCallouts`**: Allows the class to make HTTP callouts to external services.

### Constants

```java
private static final Integer BATCH_SIZE = 100;
private static final String EXTERNAL_KEY = '[EXTERNAL-KEY-MARKETING-CLOUD]';
```

- **`BATCH_SIZE`**: A constant integer set to 100, which determines the number of records to process in each batch.
- **`EXTERNAL_KEY`**: A constant string representing the external key used in the endpoint URL for the Marketing Cloud. `This must be changed to the Data Extension External Key.`

### `execute` Method

```java
public void execute(QueueableContext context) {
```

- This method is the entry point for the queueable job. It processes records in batches and sends them to the Marketing Cloud.

### Endpoint Construction

```java
String ENDPOINT = '/hub/v1/dataeventsasync/key:' + EXTERNAL_KEY + '/rowset';
```

- Constructs the `ENDPOINT` URL using the `EXTERNAL_KEY`. This URL is used to send data to the Marketing Cloud.

### Data Retrieval and Processing

```java
List<Object> jsonList = new List<Object>();
Integer count = 0;
```

- Initializes a list to hold JSON objects and a counter to track the number of records processed.

```sql
for (ssot__Individual__dlm ind : [
    SELECT ssot__Id__c, ssot__FirstName__c, ssot__LastName__c 
    FROM ssot__Individual__dlm 
    ORDER BY ssot__id__c ASC
]) {
```

- Executes a SOQL query to retrieve records from the `ssot__Individual__dlm` object, ordered by `ssot__id__c`.

```java
jsonList.add(buildObject(ind));
count++;
```

- For each record, it calls the `buildObject` method to create a JSON representation and adds it to the `jsonList`. The counter is incremented.

```java
if (count >= BATCH_SIZE) {
    MarketingCloudApiClient.sendRequest(ENDPOINT, JSON.serialize(jsonList));
    jsonList.clear();
    count = 0;
}
```

- If the number of records in `jsonList` reaches `BATCH_SIZE`, it sends the data to the Marketing Cloud using `MarketingCloudApiClient.sendRequest`. The list and counter are then reset.

### Final Batch Check

```java
if (!jsonList.isEmpty()) {
    MarketingCloudApiClient.sendRequest(ENDPOINT, JSON.serialize(jsonList));
}
```

- After the loop, if there are any remaining records in `jsonList`, they are sent in a final request.

### `buildObject` Method

```java
private Map<String, Object> buildObject(ssot__Individual__dlm ind) {
    return new Map<String, Object>{
        'keys' => new Map<String, String>{ 'IndividualId' => ind.ssot__Id__c },
        'values' => new Map<String, Object>{
            'Name' => ind.ssot__FirstName__c,
            'LastName' => ind.ssot__LastName__c
        }
    };
}
```

- This private method constructs a map representing a single record, which includes:
  - **`keys`**: A map containing the `IndividualId`.
  - **`values`**: A map containing the individual's `Name` and `LastName`.

### `startExport` Method

```java
@InvocableMethod(label='Data Cloud To Marketing Cloud' description='Sends all records from a Data Cloud DMO to Marketing Cloud' category='Data Cloud')
public static void startExport() {
    System.enqueueJob(new DataCloudToMarketingCloud());
}
```

- Annotated with `@InvocableMethod`, making it accessible as an invocable action in Salesforce, such as in Process Builder or Flow.
- Enqueues a new instance of the `DataCloudToMarketingCloud` class as a queueable job using `System.enqueueJob`.

## Usage

To initiate the data transfer, call the `startExport` method. This will enqueue the job and begin processing records asynchronously.

## Considerations

- Ensure that the `MarketingCloudApiClient` class is properly implemented to handle HTTP requests.
- Verify that the `ssot__Individual__dlm` object and its fields are correctly defined in your Salesforce environment.
- Adjust the `BATCH_SIZE` if needed, based on the limits and performance considerations of your Salesforce and Marketing Cloud setup.

This class is designed to efficiently process and transfer data from Salesforce to the Marketing Cloud, leveraging asynchronous processing to handle large volumes of data.
