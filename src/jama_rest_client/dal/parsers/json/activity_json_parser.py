from datetime import datetime
from jama_rest_client.model.activity import Activity, EventType, ObjectType

class ActivityJSONParser:

    @staticmethod
    def parse(activity_dict: dict) -> Activity:
        activity: Activity = Activity()
        activity.id = activity_dict['id']
        activity.date = ActivityJSONParser.__parse_date_time(activity_dict['date'])
        activity.details = activity_dict['details']
        activity.action = activity_dict['action']
        activity.user = activity_dict['user']
        activity.user_comment = activity_dict['userComment']
        activity.item = activity_dict['item']
        activity.item_type = activity_dict['itemType']
        activity.event_type = ActivityJSONParser.__parse_event_type(activity_dict['eventType'])
        activity.object_type = ActivityJSONParser.__parse_object_type(activity_dict['objectType'])

        return activity
    
    @staticmethod
    def __parse_date_time(date_time: str) -> datetime:
        return datetime.strptime(date_time, '%Y-%m-%dT%H:%M:%S.000+0000')
    
    @staticmethod
    def __parse_event_type(event_type: str) -> EventType:
        if event_type == EventType.BATCH_COPY.value:
            return EventType.BATCH_COPY

        if event_type == EventType.BATCH_CREATE.value:
            return EventType.BATCH_CREATE
        
        if event_type == EventType.BATCH_DELETE.value:
            return EventType.BATCH_DELETE
        
        if event_type == EventType.BATCH_SUMMARY.value:
            return EventType.BATCH_SUMMARY
        
        if event_type == EventType.BATCH_UPDATE.value:
            return EventType.BATCH_UPDATE
        
        if event_type == EventType.COPY.value:
            return EventType.COPY
        
        if event_type == EventType.CREATE.value:
            return EventType.CREATE
        
        if event_type == EventType.DELETE.value:
            return EventType.DELETE
        
        if event_type == EventType.MOVE.value:
            return EventType.MOVE
        
        if event_type == EventType.PUBLIC.value:
            return EventType.PUBLIC
        
        if event_type == EventType.UPDATE.value:
            return EventType.UPDATE
        
        raise ValueError(f'Activity eventType has an invalid value: {event_type}')

    @staticmethod
    def __parse_object_type(object_type: str) -> ObjectType:
        if object_type == ObjectType.BASELINE.value:
            return ObjectType.BASELINE

        if object_type == ObjectType.CHANGE_REQUEST.value:
            return ObjectType.CHANGE_REQUEST
        
        if object_type == ObjectType.COMMENT.value:
            return ObjectType.COMMENT
        
        if object_type == ObjectType.INTEGRATION.value:
            return ObjectType.INTEGRATION
        
        if object_type == ObjectType.ITEM_ATTACHMENT.value:
            return ObjectType.ITEM_ATTACHMENT
        
        if object_type == ObjectType.ITEM_TAG.value:
            return ObjectType.ITEM_TAG
        
        if object_type == ObjectType.MISCELLANEOUS.value:
            return ObjectType.MISCELLANEOUS
        
        if object_type == ObjectType.PROJECT.value:
            return ObjectType.PROJECT
        
        if object_type == ObjectType.RELATIONSHIP.value:
            return ObjectType.RELATIONSHIP
        
        if object_type == ObjectType.REVIEW.value:
            return ObjectType.REVIEW
        
        if object_type == ObjectType.REVISION.value:
            return ObjectType.REVISION
        
        if object_type == ObjectType.REVISION_ITEM.value:
            return ObjectType.REVISION_ITEM
        
        if object_type == ObjectType.TAG.value:
            return ObjectType.TAG
        
        if object_type == ObjectType.TEST_CYCLE.value:
            return ObjectType.TEST_CYCLE
        
        if object_type == ObjectType.TEST_PLAN.value:
            return ObjectType.TEST_PLAN
        
        if object_type == ObjectType.TEST_RESULT.value:
            return ObjectType.TEST_RESULT
                
        if object_type == ObjectType.TEST_RUN.value:
            return ObjectType.TEST_RUN
        
        if object_type == ObjectType.URL.value:
            return ObjectType.URL
        
        if object_type == ObjectType.USER.value:
            return ObjectType.USER
        
        raise ValueError(f'Activity objectType has an invalid value: {object_type}')