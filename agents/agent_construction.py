import json
import os
from dotenv import load_dotenv
load_dotenv()

import chromadb
import autogen
from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent

# Accepted file formats for that can be stored in
# a vector database instance
from autogen.retrieve_utils import TEXT_FORMATS

config_list = [
    {"model": os.getenv("MODEL"), "api_key": os.getenv("OPENAI_API_KEY"), "api_type": "openai"},
]

assert len(config_list) > 0
print("models to use: ", [config_list[i]["model"] for i in range(len(config_list))])