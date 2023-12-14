import pymongo
from pymongo import MongoClient


mongo_cluster = MongoClient("mongodb+srv://HypTAASuser:3Zh2bCN5FugZ2Rhe@hyptaas.wqjqmye.mongodb.net/?retryWrites=true&w=majority")

db = mongo_cluster['HypTAAS']
collection = db['userinfo']

# collection.insert_one({"user_id":"anve4082@colorado.edu", "temp": 10})

data = {
    'user_id': 'anve4082@colorado.edu',
    'runs': {
        'qa_sample': [
            {
                'exp_id': 'qa_sample_1',
                'task_type': 'qa',
                'model_name': 'bert',
                'learning_rate': 1,
                'batch_size': 10,
                'accuracy': 0.0,
                'training': True 
            },
            {
                'exp_id': 'qa_sample_2',
                'task_type': 'qa',
                'model_name': 'bert',
                'learning_rate': 2,
                'batch_size': 10,
                'accuracy': 0.0,
                'training': True 
            }
        ]
    }
}

# collection.insert_one(data)



# collection.find_one_and_update(
#     {'user_id':'anve4082@colorado.edu', 'run.qa_sample.exp_id': 'qa_sample_1'},
#     {'$set': {
#         'run.qa_sample.$.accuracy':10.0,
#         'run.qa_sample.$.training':False
#     }}
# )

temp = collection.find_one({'user_id':'adch9983@colorado.edu',
                            'runs.classification_demo.exp_id':'classification_demo_0',
                            'runs.classification_demo.$': 1
                            })
print(temp)

# temp = collection.find_one({'user_id':'anve4082@colorado.edu','runs.qa_sample.exp_id':'qa_sample_1'})
# print(temp)

# collection.find_one_and_update(
#     {'user_id':'anve4082@colorado.edu','runs.qa_sample.exp_id':'qa_sample_1'},
#     {'$set': {
#         'runs.qa_sample.$.accuracy':10.0,
#         'runs.qa_sample.$.training':False
#     }}
# )

# collection.find_one_and_update(
#     {'user_id':'anve4082@colorado.edu','runs.qa_sample.exp_id':'qa_sample_1'},
#     {'$set': {
#         'runs.qa_sample.$.accuracy':10.0,
#         'runs.qa_sample.$.training':False
#     }}
# )

collection.update_one(
    {'user_id':'anve4082@colorado.edu'},
    {
        '$push': {
            'runs.qa_sample': {
                'exp_id': 'qa_sample_3',
                'task_type': 'qa',
                'model_name': 'bert',
                'learning_rate': 3,
                'batch_size': 20,
                'accuracy': 0.0,
                'training': True 
            }
        }
    }
)

# collection.find_one_and_update({"user_id":"anve4082@colorado.edu"}, {"$set" : {"temp" : 20}}, upsert = False ).