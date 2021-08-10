from flask_restful import Api
from app import flaskAppInstance
from .TaskAPI import TaskAPI
from .TaskByID import TaskByID


restServerInstance = Api(flaskAppInstance)

restServerInstance.add_resource(TaskAPI,"/api/v1.0/task")
restServerInstance.add_resource(TaskByID,"/api/v1.0/task/id/<string:taskId>")