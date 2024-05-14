import json
import os

import chromadb

import autogen
from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent

# Accepted file formats for that can be stored in
# a vector database instance
from autogen.retrieve_utils import TEXT_FORMATS

config_list = [
    {"model": "gpt-3.5-turbo-0125", "api_key": "<YOUR_API_KEY>", "api_type": "openai"},
]

assert len(config_list) > 0
print("models to use: ", [config_list[i]["model"] for i in range(len(config_list))])