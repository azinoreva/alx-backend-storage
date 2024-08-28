#!/usr/bin/env python3
'''
Provides some stats about Nginx logs stored in MongoDB
'''


def schools_by_topic(mongo_collection, topic):
    '''
    Return based on specific topic.
    '''
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return list(mongo_collection.find(topic_filter))
