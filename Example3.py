#Sequence chain
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnablePassthrough, RunnableSequence, RunnableLambda

llm= ChatGroq(model="llama-3.1-8b-instant")
output= StrOutputParser()
template1= "At which place the dish {food} was originated"
prompt1= PromptTemplate(template=template1)
chain1= prompt1 | llm | output
template2= "what is the population of the place {place}"
prompt2= PromptTemplate(template=template2)
chain2= prompt2 | llm | output
template3= "Compute the {population} divided by 4"
prompt3= PromptTemplate(template=template3)
chain3= prompt3 | llm | output
tot= RunnablePassthrough().assign(place=chain1).assign(population=chain2).assign(calculation=chain3)
results= tot.invoke({"food":"Ramen"})
print(results)
print("+"*100)
tot1= RunnableSequence(chain1,RunnableLambda(lambda place:{"place":place}),chain2, RunnableLambda(lambda population:{"population":population}),chain3)
results1= tot1.invoke({"food":"Ramen"})
print(results1)
