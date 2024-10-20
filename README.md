## **Project Summary: Advanced ETL Pipeline for Sales Data Insights**

The **Advanced ETL Pipeline for Sales Data Insights** project is designed to systematically extract, transform, and load (ETL) sales-related data from diverse sources into a centralized storage solution, enabling comprehensive data analysis and actionable business insights. Utilizing robust technologies such as **Amazon Redshift** for data warehousing, **Amazon S3** for scalable storage, and **Python** for scripting, the pipeline ensures efficient data handling and processing tailored to meet specific business requirements.

### **Key Components and Workflow**

1. **Extraction (`extract.py`):**
   - Connects securely to the Amazon Redshift data warehouse.
   - Executes SQL queries to retrieve transactional sales data from the past year.
   - Initial data transformations are performed during extraction to streamline subsequent processes.

2. **Transformation (`transform.py`):**
   - Cleans the extracted data by removing duplicates and handling missing values.
   - Enhances data quality by adding calculated fields (e.g., `total_price`) and categorizing shipping times.
   - Implements data validation checks to ensure integrity and reliability.

3. **Loading (`load_data_to_s3.py`):**
   - Connects to Amazon S3 using secure credentials.
   - Uploads the cleaned and transformed sales data as CSV files into a designated S3 bucket, organized with timestamped paths for easy tracking.

3. **Analyze (`load_data_to_s3.py`):**
   1. **Total Sales per Category:** It calculates the total sales amount for each product category allowing you to identify which categories generate the most revenue.

   2. **Sales Over Time:** This insight shows the trend of sales over different dates, helping you understand how sales are fluctuating over time (e.g., daily, weekly, monthly).

   3. **Top 10 Products by Sales:** It identifies the top-selling products based on the total sales amount, providing insight into the most popular or profitable items.

4. **Orchestration (`main.py`):**
   - Integrates the **extraction, transformation, loading and analyzing** steps into a seamless workflow.
   - Incorporates comprehensive logging for monitoring and debugging purposes.


6. **Output (`main.py`):**
      ```
      src\extract.py:15: DtypeWarning: Columns (23) have mixed types. Specify dtype option on import or set low_memory=False.
      df = pd.read_csv(file_path, encoding='utf-8')
      INFO:src.extract:Extracted 128975 records
      INFO:src.transform:Starting data transformation
      INFO:src.transform:Removed 0 duplicate records
      INFO:src.transform:Data shape after dropping missing values: (19379, 24)
      c:\__\__\Shashank\ETL-Pipeline-for-Sales-Data-Insights\src\transform.py:25: UserWarning: Could not infer format, so each element will be parsed individually, falling back to `dateutil`. To ensure parsing is consistent and as-expected, please specify a format.
      df['Date'] = pd.to_datetime(df['Date'])
      INFO:src.transform:Converted 'Date' column to datetime
      INFO:src.load:Uploading cleaned_sales_data_20241019_201718.csv to S3 bucket: examplebucneonman
      INFO:src.load:Upload successful
      INFO:src.analyze:Starting data analysis
      INFO:src.analyze:Total Sales per Category:
            Category     Amount
      0         Blouse    42488.0
      1         Bottom    41541.0
      2   Ethnic Dress   102085.0
      3          Saree     9659.0
      4            Set  5919897.0
      5            Top   721354.0
      6  Western Dress  3318232.0
      7          kurta  2891562.0
      INFO:src.analyze:Sales Over Time:
               Date    Amount
      0  2022-04-30   16615.0
      1  2022-05-01  203966.0
      2  2022-05-02  244839.0
      3  2022-05-03  244499.0
      4  2022-05-04  258427.0
      5  2022-05-05  201120.0
      6  2022-05-06  235400.0
      7  2022-05-07  296555.0
      8  2022-05-08  280755.0
      9  2022-05-09  265804.0
      10 2022-05-10  271097.0
      11 2022-05-11  272962.0
      12 2022-05-12  255285.0
      13 2022-05-13  268116.0
      14 2022-05-14  314224.0
      15 2022-05-15  364107.0
      16 2022-05-16  298008.0
      17 2022-05-17  314125.0
      18 2022-05-18  315527.0
      19 2022-05-19  286722.0
      20 2022-05-20  292438.0
      21 2022-05-21  249559.0
      22 2022-05-22  258306.0
      23 2022-05-23  190010.0
      24 2022-05-24  151246.0
      25 2022-05-25  174678.0
      26 2022-05-26  120142.0
      27 2022-05-27  131108.0
      28 2022-05-28  138472.0
      29 2022-05-29  152400.0
      30 2022-05-30  171888.0
      31 2022-05-31  193515.0
      32 2022-06-01  217498.0
      33 2022-06-02  216599.0
      34 2022-06-03  167394.0
      35 2022-06-04  182631.0
      36 2022-06-05  207339.0
      37 2022-06-06  217930.0
      38 2022-06-07  231410.0
      39 2022-06-08  207200.0
      40 2022-06-09  199320.0
      41 2022-06-10  186489.0
      42 2022-06-11  179001.0
      43 2022-06-12  223589.0
      44 2022-06-13  190787.0
      45 2022-06-14  178882.0
      46 2022-06-15  180415.0
      47 2022-06-16  190381.0
      48 2022-06-17  211641.0
      49 2022-06-18  209655.0
      50 2022-06-19  217341.0
      51 2022-06-20  195692.0
      52 2022-06-21  215712.0
      53 2022-06-22  201679.0
      54 2022-06-23  183958.0
      55 2022-06-24  150313.0
      56 2022-06-25  145856.0
      57 2022-06-26  184702.0
      58 2022-06-27  195543.0
      59 2022-06-28  203534.0
      60 2022-06-29  122412.0
      INFO:src.analyze:Top 10 Products by Sales:
                        SKU    Amount
      2364     JNE3797-KR-L  289500.0
      2365     JNE3797-KR-M  269095.0
      2366     JNE3797-KR-S  201541.0
      2367    JNE3797-KR-XL  195101.0
      3093   SET183-KR-DH-M  134343.0
      2370  JNE3797-KR-XXXL  112774.0
      2369   JNE3797-KR-XXL  106272.0
      2368    JNE3797-KR-XS  104803.0
      619       J0230-SKD-S   73269.0
      618       J0230-SKD-M   59159.0
      INFO:__main__:ETL pipeline executed successfully
      ```
5. **Environment and Deployment:**
   - Utilizes environment variables for secure configuration management.
   - Provides Docker support for containerization, ensuring consistent deployment across different environments.
   - Includes CI/CD pipelines using tools like GitHub Actions to automate testing, building, and deployment processes.

### **Advanced Features and Enhancements**

- **Data Validation and Quality Assurance:** Implements rigorous checks post-transformation to maintain high data standards.
- **Error Handling and Retries:** Utilizes libraries like `tenacity` to manage transient failures and ensure pipeline resilience.
- **Structured Logging:** Adopts JSON-formatted logs for enhanced traceability and easier integration with monitoring tools.
- **Scheduling and Automation:** Leverages orchestration tools such as **Apache Airflow** to automate periodic ETL executions.
- **Monitoring and Alerting:** Integrates with monitoring services like **AWS CloudWatch** and **SNS** for real-time tracking and alert notifications.
- **Security Best Practices:** Ensures secure handling of credentials, data encryption both in transit and at rest, and compliance with data protection regulations.

### **Insights and Business Intelligence**

Once the ETL pipeline successfully loads the transformed sales data into Amazon S3, the project facilitates the generation of valuable business insights through integration with **Business Intelligence (BI)** tools like **Amazon QuickSight**, **Tableau**, or **Power BI**. These tools enable the creation of interactive dashboards and reports, offering visualizations on key metrics such as:

- **Total Sales Over Time**
- **Sales by Product Category and Region**
- **Customer Acquisition and Retention Rates**
- **Shipping Performance Analysis**

Additionally, the project supports advanced analytics and machine learning applications, such as predicting future sales trends and customer behavior, further empowering data-driven decision-making.

### **Deployment and Scalability**

The pipeline is containerized using **Docker**, ensuring scalability and ease of deployment across various environments. For larger data volumes and more complex processing needs, the infrastructure can be scaled using AWS services like **AWS Lambda**, **AWS Glue**, or **Amazon EMR**. Continuous Integration and Continuous Deployment (CI/CD) pipelines automate the testing and deployment processes, enhancing development efficiency and reliability.
