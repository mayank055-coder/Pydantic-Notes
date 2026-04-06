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

# Model Validator 
    @model_validator(mode='after')
    def validate_emergency_contacts(cls,model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('patients older than 60 must have an emergency contact')
        return model
    
#Computed Field
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi

#Field Validator
    @field_validator('email')
    @classmethod
    def email_validator(cls,value):

        valid_domains = ['hdfc.com','icici.com',gmail.com]

        domain_name = value.split('@')[-1]

        if domains_name not in valid_domains:
            raise ValueError('Not in valid domains')
        
        return value
    
        @field_validator('name')
        @classmethod
    def name_validator(cls,value):
        return value.upper()
    
    @field_validator('age',mode=after)
    @classmethod
    def validate_age(cls,value):
        if 0<value<100:
            return value
        else:
            raise ValueError('age should be greater than 100')
        


    def update_patient_data(patient: Patient):

        print(patient.name)
        print(patient.age)
        print(patient.married)
        print('updated')

    patient_info = {'name':'mayank','email':'mayankguptag055gmail.com','linkedin':'https://linkedin.com/132','age':'30','weight':75.2,'contact_details':{'phone':'8383898700'}}


    patient1 = Patient(**patient_info)

    update_patient_data(patient1)
        print(patient.married)
        print('updated')

    patient_info = {'name':'mayank','email':'mayankguptag055gmail.com','linkedin':'https://linkedin.com/132','age':'30','weight':75.2,'contact_details':{'phone':'8383898700'}}


    patient1 = Patient(**patient_info)

    update_patient_data(patient1)
