from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

# Using langchain - using two chains run synchronously, where second chain's input is firt chain output
llm= ChatGroq(model="llama-3.1-8b-instant",temperature=0.3)
template1= "Where was the infamous dish {food} originated in the world"
prompt1= PromptTemplate(template=template1)
output= StrOutputParser()
chain1= prompt1 | llm | output
template2= "What is the major ethanicity of the {place}"
prompt2= PromptTemplate(template=template2)
chain2= prompt2 | llm | output
tot_chain= ({"place":chain1} | chain2) 
result= tot_chain.invoke({"food":"Ice cream"})
print(result)

