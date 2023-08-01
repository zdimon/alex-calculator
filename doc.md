# Установка AWS CLI

    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
    unzip awscliv2.zip
    sudo ./aws/install

При установке остановится на команде sudo ./aws/install и запросит пароль.

# Конфигурирование

    aws configure

Вводим секреты.
Генерировать в Account->Security credentials.
Создается файл тут ~/.aws/credentials
Регион вводим по дефолтный us-east-1.

Но регион можно менять в процессе создания экземпляра сервера.

# Установка клиента для AWS

    pip install boto3

# Создание S3 контейнера

    def create_bucket(bucket_name, region=None):
        """Create an S3 bucket in a specified region

        If a region is not specified, the bucket is created in the S3 default
        region (us-east-1).

        :param bucket_name: Bucket to create
        :param region: String region to create bucket in, e.g., 'us-west-2'
        :return: True if bucket created, else False
        """

        # Create bucket
        try:
            if region is None:
                s3_client = boto3.client('s3')
                s3_client.create_bucket(Bucket=bucket_name)
            else:
                s3_client = boto3.client('s3', region_name=region)
                location = {'LocationConstraint': region}
                s3_client.create_bucket(Bucket=bucket_name,
                                        CreateBucketConfiguration=location)
        except ClientError as e:
            logging.error(e)
            return False
        return True

# Загрузка файла в S3 контейнер

    s3 = boto3.resource('s3')

    for bucket in s3.buckets.all():
        print(bucket.name)

    data = open('run.sh', 'rb')
    s3.Bucket('mitrofan-bucket').put_object(Key='test.txt', Body=data)

# Создание EC2 контейнера.

Создаем пару ключей

    aws ec2 create-key-pair --key-name KeyPair1 --query 'KeyMaterial' --output text > KeyPair1.pem





    import boto3
    ec2 = boto3.resource('ec2')

    instances = ec2.create_instances(
            ImageId="ami-053b0d53c279acc90",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            KeyName="KeyPair1"
        )

ami-053b0d53c279acc90 - Ubuntu 



ssh -i "KeyPair1.pem" ubuntu@ec2-54-197-199-93.compute-1.amazonaws.com

ssh -i "KeyPair1.pem" ubuntu@ec2-18-212-174-15.compute-1.amazonaws.com