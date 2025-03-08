import langchain
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm=ChatGroq(temperature=0,groq_api_key=os.getenv("GROQ_API_KEY1"), model="llama-3.3-70b-versatile")

    def extract_jobs(self,cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """ SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ###INSTRUCTION:
            The scraped text is from the career's page of website.
            Your job is to extract the job posting and return them in JSON format containing the following key:
            'role','experience','skills', and 'description'.
            Only return the valid JSON inside,remove all data outside the json object
            Extract only first object
            ###VALID JSON(NO PREAMBLE):

                """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke( input={'page_data': cleaned_text} )
        try:
            json_parser=JsonOutputParser()
            res=json_parser.parse(res.content)

        except OutputParserException:
            raise  OutputParserException(str(res))
        return res if isinstance(res,list) else [res]

    def write_mail(self,job,links):
        prompt_email=PromptTemplate.from_template(
        """
        ### JOB Description:
        {job_description}
        
        ###INSTRUCTION:
        You are Sushree, a test automation engineer currently working with Boeing.You are a result driven automation tester with 11+ years of experience in
        frontend and backend test automation,mobile,performance and api testing.Skilled in designing and implementing test automation
        stratergies across web,mobile and cloud based application.Currently enhancing your skills in LLM.
        Your job is to write a cold email to the client regarding the job mentioned above in fulfiling their needs for automation tester recruitement.
        Also add the most relevent once from the following expertise to showcase your experience: {links}
        Restric the email to 500 words
        Remember you are Sushree, Senior Automation Test Engineer at Boeing.
        Do not provide a preamble
        ### EMAIL (NO PREAMBLE)
            """
)
        chain_email=prompt_email|self.llm
        res=chain_email.invoke({"job_description":str(job),"links":links})
        return res.content





