
# Python program to demonstrate
# main() function
import boto3
from botocore.config import Config



  
# Defining main function
def main():
    print("hey there")
    azs = (get_all_regions_and_avaliability_zones().items())

  
  
def get_all_instance_types_by_az(azs):
    for az in azs:
        client.get_paginator('describe_instance_type_offerings')

def get_all_regions_and_avaliability_zones():
    all_zones_to_regions = {}
    regions = boto3.client('ec2').describe_regions()['Regions']
    for region in regions:
        ec2 = boto3.client('ec2', region_name=region['RegionName'])
        response = ec2.describe_availability_zones()
        for zone in response['AvailabilityZones']:
            if zone['ZoneType'] == 'availability-zone':
                all_zones_to_regions[zone["ZoneName"]] = zone['RegionName']
                
    return all_zones_to_regions

        
    



# Using the special variable 
# __name__
if __name__=="__main__":
    main()

