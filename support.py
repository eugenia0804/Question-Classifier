import json

# List of file names
file_names = ['Results/iteration-2/results/1to10.json',
                'Results/iteration-2/results/11to20.json',
                'Results/iteration-2/results/21to30.json',
                'Results/iteration-2/results/31to40.json',
                'Results/iteration-2/results/41to50.json']

# Create an empty dictionary to store the combined data
combined_data = {}

# Read each file and add its data to the combined dictionary
for file_name in file_names:
    with open(file_name) as file:
        data = json.load(file)
        combined_data.update(data)

# Save the combined data to a new JSON file
output_file = 'Results/iteration-2/final/1to50.json'
with open(output_file, 'w') as file:
    json.dump(combined_data, file, indent=4)

print(f"Combined data saved to '{output_file}'.")

string = """
First, we'll create the same sampling distribution that we created yesterday. Use the model above to create the sampling distribution for the mean scores of samples of 2 students (n=2) taken from a population of 48 students (N=48).

1) Set the slider and click `setup` and `collect samples.` The sampling will happen faster if you pull the `model speed` slider all the way to the right.

"""
print(len(string))