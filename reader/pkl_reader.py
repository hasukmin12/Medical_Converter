import pickle

path = '/home/has/Results/plans.pkl'

with open(path, 'rb') as f:
    data = pickle.load(f)

print(data)
# print(list(data['plans_per_stage'].keys()))
# print(data['plans_per_stage'][0])
# print(data['plans_per_stage'][1])