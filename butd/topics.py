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
    '/test_topic3',
    '/test_topic4',
    }

TOPICS_MOTOR = {
    '/fr/feedback',
    '/fl/feedback',
    '/br/feedback',
    '/bl/feedback',
    '/odom',
    }

TOPICS_SAFETY = {
    '/move_base/cancel'
    }

ALLOWED_TOPICS_READ = TOPICS_TEST|TOPICS_MOTOR|TOPICS_SAFETY

ALLOWED_TOPICS_WRITE = ALLOWED_TOPICS_READ