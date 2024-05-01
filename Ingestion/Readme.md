The ingestion will happen via Spark. The spark code will be a generic one, instead of having one notebook per table, we will have generic spark code, that will be parametrised, such that it fetches the values from a config file. 
For explaining this better, following files have been added:
1) Config.json -> which is a sample config file, it contains the configuration around which table to ingest data in, schema definition, transformations to perform, joins to perform and what metadata columns to add
2) genericDataLoader -> generic Spark code that reads the config and performs all the transformations as specific in config and writes it out.
3) genericConsumer -> its a spark streaming application that reads data from kafka, performs transformation.

The above code is just a psuedo code for demo and explainability purposes, and is not actually created/tested to be run. 

For correlating ad_impression and clicks conversion, it would be best to create a view on top the tables containing clicks data and ad_impression data, instead of combining data into clicks table and mixing data, to ensure data purity is maintained. For that, I have created a views.sql file that contains the logic on how to correlate. 

**click_through_rate** = > counts of users that clicked on the ad.

**conversion_rate** = > counts of users that actioned the ad after clicking it. 
