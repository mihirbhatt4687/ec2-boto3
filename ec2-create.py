import boto3

session = boto3.session.Session(
    'PROFILE OR ACCESS AND SECRET ID'
)

ec2 = session.resource('ec2')

instance = ec2.create_instances(
    ImageId='ami-0e001c9271cf7f3b9',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    KeyName='KEYPAIR_NAME',
    UserData="""#!/bin/bash
    sudo apt update -y
    sudo apt install apache2 -y 
    sudo apt install python-software-properties -y
    sudo add-apt-repository ppa:ondrej/php -y 
    sudo apt update -y
    sudo apt install php8.2 -y
    """,
    NetworkInterfaces=[{
        'AssociatePublicIpAddress': True,
        'DeviceIndex': 0,
        'Groups' : [
            "SECURITY_GROUP_ID_1",
            "SECURITY_GROUP_ID_2",
        ],
    }]
);

instance_id = instance[0].id

print(f"Instance {instance_id} is creating...")
