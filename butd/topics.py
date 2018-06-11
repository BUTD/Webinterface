'''
Created on May 25, 2018

@author: benjamin
'''
TOPICS_TEST = {
    '/hc04',
    '/my_topic',
    '/chatter',
    '/test_topic',
    '/test_topic1',
    '/test_topic2',
    }

TOPICS_MOTOR = {
    '/fr/feedback',
    '/fl/feedback',
    '/br/feedback',
    '/bl/feedback',
    }

ALLOWED_TOPICS_READ = TOPICS_TEST|TOPICS_MOTOR

ALLOWED_TOPICS_WRITE = ALLOWED_TOPICS_READ