from load_agent import load_agents
from tools import create_tools
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.output_parsers.rail_parser import GuardrailsOutputParser
from langchain.chains import LLMChain
import langchain_visualizer
import torch 

tools = create_tools()
agent=load_agents(tools)
async def search_agent_demo():
    query = input("\nEnter a query: ")
    return agent.run(input("Enter a question:"))


langchain_visualizer.visualize(search_agent_demo)
