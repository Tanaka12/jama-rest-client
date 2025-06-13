from datetime import datetime
from jama_rest_client.model.comment import Comment, CommentBody, CommentLocation, CommentStatus, CommentType 

class CommentJSONParser:

    @staticmethod
    def parse(comment_dict: dict) -> Comment:
        comment: Comment = Comment()
        comment.id = comment_dict['id']
        comment.in_reply_to = comment_dict['inReplyTo']
        comment.created_date = datetime.fromisoformat(comment_dict['createdDate'])
        comment.created_by = 0
        comment.modified_by = 0
        comment.deleted = comment_dict['deleted']
        comment.status = CommentJSONParser.__parse_comment_status(comment_dict['status'])
        comment.body = CommentJSONParser.__parse_comment_type(comment_dict['body'])
        comment.comment_type = CommentJSONParser.__parse_comment_body(comment_dict['commentType'])
        comment.location = comment_dict['location']

        return comment
    
    @staticmethod
    def __parse_comment_status(comment_status: str) -> CommentStatus:
        if comment_status == CommentStatus.CANCELLED.value:
            return CommentStatus.CANCELLED

        if comment_status == CommentStatus.COMPLETED.value:
            return CommentStatus.COMPLETED
        
        if comment_status == CommentStatus.OPEN.value:
            return CommentStatus.OPEN
        
        raise ValueError(f'Comment commentStatus has an invalid value: {comment_status}')
    
    @staticmethod
    def __parse_comment_type(comment_type: str) -> CommentType:
        if comment_type == CommentType.GENERAL.value:
            return CommentType.GENERAL

        if comment_type == CommentType.QUESTION.value:
            return CommentType.QUESTION
        
        if comment_type == CommentType.PROPOSED_CHANGE.value:
            return CommentType.PROPOSED_CHANGE
        
        if comment_type == CommentType.ACCEPTED_COMMENT.value:
            return CommentType.ACCEPTED_COMMENT

        if comment_type == CommentType.REJECTED_COMMENT.value:
            return CommentType.REJECTED_COMMENT
        
        if comment_type == CommentType.ISSUE.value:
            return CommentType.ISSUE

        if comment_type == CommentType.DECISION.value:
            return CommentType.DECISION

        if comment_type == CommentType.DECISION_REQUEST.value:
            return CommentType.DECISION_REQUEST
        
        raise ValueError(f'Comment commentType has an invalid value: {comment_type}')
    
    @staticmethod
    def __parse_comment_body(comment_body_dict: dict) -> CommentBody:
        comment_body: CommentBody = CommentBody()
        comment_body.text = comment_body_dict['text']

        return comment_body