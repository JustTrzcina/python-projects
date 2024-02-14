'''
This file contains list of blocked JWT tokens that are no longer valid
for user verification. NOTE: This approach is usually not recomended due to
possibility of really big file containing thounsands of JWT tokens. Usually
it is done in more managable manner by deleting tokens that has expired.
Also set is not persistent therefore a database soulution should be implemented
'''

BLOCKED = set()