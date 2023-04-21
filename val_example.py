import os
import valorant
from decouple import config

print(f"\nInitializing...")
print(f"\nWelcome to Val-Project")
KEY=config("VALPY-KEY")
client = valorant.Client(KEY, locale=None)

# # Retrieve Skin Collection with user query
# skins = client.get_skins()
# name = input(f"\nSearch a Valorant Skin Collection: ")

# results = skins.find_all(name=lambda x: name.lower() in x.lower())

# print("\nResults: ")
# for skin in results:
#     print(f"\t{skin.name.ljust(21)}")

# # Retrieve Agents with user query
# agents = client.get_characters()
# name = input(f"\nSearch for Valorant Agent: ")
# character_results = agents.find_all(name=lambda x: name.lower() in x.lower())
# print("\nAgents: ")
# for agent in character_results:
#     print(f"\t{agent.name.ljust(21)}")

altAcct = client.get_user_by_name("TheLastYuma#NA1")
print(f"\n{altAcct.gameName}")
print(f"\tMatch History: \n\t {altAcct.matchlist}")