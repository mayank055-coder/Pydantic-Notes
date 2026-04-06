from pydantic import BaseModel,EmailStr,AnyUrl, Field
from typing import Annotated,List,Dict,Optional

class patient(BaseModel):

    name:Annotated[str,Field(max_length=50, title = 'Name of the Patient',Description = 'Give the name of the patient in less than 50 chars', examples=['Mayank','Amit'])]
    email:EmailStr
    linkedin_url:AnyUrl
    github_link:AnyUrl
    age:int = Field(gt=0,ls=120)
    weight:Annotated[float,Field(gt=0,strict=True)]
    married:Annotated[bool,Field(default=None,description='Is the patient is married or not')]
    allergies:Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details:Dict[str,str]


    def update_patient_data(patient: Patient):

        print(patient.name)
        print(patient.age)
        print(patient.married)
        print('updated')

    patient_info = {'name':'mayank','email':'mayankguptag055gmail.com','linkedin':'https://linkedin.com/132','age':'30','weight':75.2,'contact_details':{'phone':'8383898700'}}


    patient1 = Patient(**patient_info)

    update_patient_data(patient1)