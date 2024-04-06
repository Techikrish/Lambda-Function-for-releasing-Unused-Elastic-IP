# Lambda Function: for Releasing Unused Elastic IPs
-   The primary purpose of this Lambda function is to  **identify and release**  Elastic IP (EIP) addresses that are no longer associated with any Amazon EC2 instances.
-   When an EIP is not attached to an instance, it continues to incur costs. By releasing unassigned EIPs, you can optimize your AWS resources.

### Prerequisites - 
**Lambda Function Timeout**: Set the function timeout to **10 seconds** to ensure efficient execution

**IAM Policy Permissions** Create an IAM policy with the following permissions for your Lambda function’s execution role:

    -     `ec2:DescribeAddresses`
    - -   `ec2:DescribeRegions`
    - -   'ec2:ReleaseAddress
    - -   `logs:PutLogEvents`: Allows the function to write logs to CloudWatch, which can be helpful for monitoring and debugging.
   

