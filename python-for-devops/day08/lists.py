
# Basic
s3_bucket_list = ["dev_bucket", "stagging_bucket", "uat_bucket", "prod_bucket"]

print(s3_bucket_list)

# list indexing
print(s3_bucket_list[0]) # access the first element

# list length
print(len(s3_bucket_list))

###----------------------###

# list appended
ec2_instance_list = ["dev_instance", "stagging_instance", "uat_instance", "prod_instance"]
ec2_instance_list.append("test_instance")

print(ec2_instance_list)


# list removed
ec2_instance_list.remove("stagging_instance")

print(ec2_instance_list)

#list slicing
sliced_list = ec2_instance_list[0:2]
print(sliced_list)

# list concatenation
concate_list = ["simba", "naala", "tamun", "zaazo"]
print(concate_list[0] + "<<>>" + concate_list[1])


# list sorting
# Ascending order
sorted_list = [1, 33, 10, 5, 90]
sorted_list.sort()
print(sorted_list)

# reverse or decending order
sorted_list.sort(reverse=True)
print(sorted_list)