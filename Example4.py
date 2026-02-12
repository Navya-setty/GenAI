# branching code workflow (multiprompt routing)
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda

llm= ChatGroq(model="llama-3.1-8b-instant",temperature=0.3)
output= StrOutputParser()
template_hr= "What is the work of the HR in a company"
prompt_hr= PromptTemplate(template=template_hr)
chain_hr= prompt_hr | llm | output
template_finance= "What is the work of the finance department in a company"
prompt_finance= PromptTemplate(template= template_finance)
chain_finance= prompt_finance | llm | output
default_chain= RunnableLambda(lambda _: "The other department is the marketing.")

tot= RunnableBranch(
    (lambda x: x.get("role")=="HR",chain_hr),
    (lambda x: x.get("role")=="Finance",chain_finance),
    default_chain
)

result= tot.invoke({"role":"HR"})
print(result)

