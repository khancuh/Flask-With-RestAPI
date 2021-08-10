from flask_restful import Resource
import logging as logger

class TaskAPI(Resource):

    def get(self):
        logger.debug("Inside the get method of Task")
        return {"message" : "Inside get method"},200


    def post(self):
        logger.debug("Inisde the post method of Task")
        return {"message" : "Inside post method"},200

    def put(self):
        logger.debug("Inisde the put method of Task")
        return {"message" : "Inside put method"},200

    def delete(self):

        logger.debug("Inisde the delete method of Task")
        return {"message" : "Inside delete method"},200