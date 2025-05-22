
from jama_rest_client.model.project import Project

class ProjectParser:

    @staticmethod
    def parse(project_dict: dict) -> Project:
        project: Project = Project()
        project.id = project_dict['id']
        project.projectKey = project_dict['projectKey']
        project.isFolder = project_dict['isFolder']
        project.createdDate = project_dict['createdDate']
        project.modifiedDate = project_dict['modifiedDate']
        project.createdBy = project_dict['createdBy']
        project.modifiedBy = project_dict['modifiedBy']
        project.fields = project_dict['fields']

        return project