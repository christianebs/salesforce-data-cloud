# Enrichment Copy Fields

## Summary

This guide presents a comprehensive, step-by-step procedure for establishing enrichment copy fields within the Salesforce CRM system. It encompasses the processes of data importation, the creation of calculated insights, the assignment of requisite permissions, and the configuration of field enrichment, thereby enhancing data integration and functionality.

<br>

## Understanding enrichment copy fields
Enrichment copy fields are a functionality within CRM systems that allow for the enhancement of existing data by copying and integrating additional insights or metrics from external data sources. This process involves mapping calculated insights or metrics from a data cloud environment to specific fields within a CRM object. The enrichment process ensures that the CRM data is more comprehensive, accurate, and valuable for decision-making.

<br>

## Utilization of enrichment copy fields
Enrichment copy fields are used to enhance existing CRM data by integrating additional insights, such as calculated metrics or external data points, into the CRM system.

1. **Improved decision-making**: By enriching CRM data with more detailed insights, organizations can make more informed decisions based on a fuller picture of their data landscape.

2. **Streamlined data integration**: This feature allows for seamless integration of data from various sources into the CRM, ensuring that all relevant information is available in one place.

3. **Customization and flexibility**: Organizations can customize which fields are enriched and how the data is mapped, providing flexibility to meet specific business needs.

4. **Efficiency in data management**: Automating the enrichment process reduces manual data entry and ensures that data is consistently updated and accurate.

Overall, Enrichment Copy Fields enhance the value of CRM data by integrating additional insights, leading to better analytics, reporting, and strategic planning.


<br>

## Detailed Process Guide

### Step 1: Import Data and Map to DMOs

- Import data from various sources.
- Map the imported data to Data Model Objects (DMOs).

### Step 2: Create Calculated Insights

- Develop Calculated Insights with the necessary metrics (measures) and dimensions.

### Step 3: Assign Data Cloud Admin Access

1. In your CRM org, go to **Setup**.
2. Search for and select **Permission Sets**.
3. Select the **Data Cloud Admin** permission set.
4. Under **Apps**, choose **Data Cloud Space Management**.
5. In **Data Spaces**, click **Edit**, enable the `default` data space, and click **Save**.

### Step 4: Create New Fields in CRM Object

- Add new fields to the target CRM object.

### Step 5: Grant Write Permission to Customer 360 Data Platform Integration User

1. In your CRM org, go to **Setup**.
2. Search for and select **Permission Sets**.
3. Select the **Customer 360 Data Platform Integration** permission set.
4. Click **Object Settings**, then select the desired object.
5. Select all options listed.
6. Grant **edit** and **read** access for the newly selected attributes.
7. Click **Save**.

### Step 6: Create Copy Field Enrichment

1. In **Setup**, search for and select **Copy Field**.
2. Click **New**.
3. Configure the following settings:
   - Select the `default` Data Space.
   - The Data Cloud Object is the **Calculated Insight** created.
   - The target is the CRM **object** that will receive the enrichments.
   - ID Matching Method is `Use the Primary Key`.
4. Click **Next**.
5. Select the newly created fields that will receive the enrichments and click **Next**.
6. Enter the enrichment name and click **Next**.
7. In **Field Mapping**, map the source metric to the target attribute.
8. Click **Save and Start Sync**. Syncing data from Data Cloud takes a few minutes.

