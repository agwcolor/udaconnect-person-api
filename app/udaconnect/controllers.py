from app.udaconnect.models import Person
from app.udaconnect.schemas import PersonSchema
from app.udaconnect.services import PersonService
from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import Optional, List

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa

# TODO: This needs better exception handling
'''
@api.route("/persons")
@api.param("first_name", "First Name", _in="query")
@api.param("last_name", "Last Name", _in="query")
@api.param("company_name", "Company Name", _in="query")
'''
@api.route("/persons")
class PersonsResource(Resource):
    #@accepts(schema=PersonSchema)
    @responds(schema=PersonSchema)
    def post(self) -> Person:
        # payload = request.get_json()
        payload =  {
            "first_name": "Doggo",
            "company_name": "Dog Treats for All",
            "last_name": "Jumpo"
        }
        new_person: Person = PersonService.create(payload)
        return new_person

    @responds(schema=PersonSchema, many=True)
    def get(self) -> List[Person]:
        persons: List[Person] = PersonService.retrieve_all()
        return persons


@api.route("/persons/<person_id>")
@api.param("person_id", "Unique ID for a given Person", _in="query")
class PersonResource(Resource):
    @responds(schema=PersonSchema)
    def get(self, person_id) -> Person:
        person: Person = PersonService.retrieve(person_id)
        return person
