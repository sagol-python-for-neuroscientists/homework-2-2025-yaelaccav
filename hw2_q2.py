from collections import namedtuple
from enum import Enum
from itertools import zip_longest

# Define the Condition enum and Agent namedtuple
Condition = Enum("Condition", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))

def improve(condition):
    """Return the improved condition after meeting a Cure agent."""
    if condition == Condition.DYING:
        return Condition.SICK
    elif condition == Condition.SICK:
        return Condition.HEALTHY
    return condition

def worsen(condition):
    """Return the worsened condition after meeting an infected agent."""
    if condition == Condition.SICK:
        return Condition.DYING
    elif condition == Condition.DYING:
        return Condition.DEAD
    return condition

def meetup(agent_listing: tuple) -> list:
    """Model the outcome of the meetings of pairs of agents."""
    # Step 1: Create a mutable version of the input
    updated_agents = {agent.name: agent for agent in agent_listing}

    # Step 2: Remove agents who don’t meet
    meeting_agents = [agent for agent in agent_listing if agent.category not in (Condition.HEALTHY, Condition.DEAD)]

    # Step 3: Pair the meeting agents
    for i in range(0, len(meeting_agents) - 1, 2):
        a1 = meeting_agents[i]
        a2 = meeting_agents[i + 1]

        # Cure logic
        if a1.category == Condition.CURE and a2.category != Condition.CURE:
            updated_agents[a2.name] = Agent(a2.name, improve(a2.category))
        elif a2.category == Condition.CURE and a1.category != Condition.CURE:
            updated_agents[a1.name] = Agent(a1.name, improve(a1.category))
        elif a1.category == Condition.CURE and a2.category == Condition.CURE:
            pass
        else:
            # Both Dying
            if a1.category == Condition.DYING and a2.category == Condition.DYING:
                updated_agents[a1.name] = Agent(a1.name, Condition.DEAD)
                updated_agents[a2.name] = Agent(a2.name, Condition.DEAD)
            else:
                # Worsen each other
                updated_agents[a1.name] = Agent(a1.name, worsen(a1.category))
                updated_agents[a2.name] = Agent(a2.name, worsen(a2.category))

    # Return a list in the original order
    return [updated_agents[agent.name] for agent in agent_listing]



# Optional testing block (only runs when running this file directly)
# if __name__ == "__main__":
#     agent_list = (
#         Agent("Alice", Condition.SICK),
#         Agent("Bob", Condition.DYING),
#         Agent("Curey", Condition.CURE),
#         Agent("Dana", Condition.DYING),
#         Agent("Eli", Condition.HEALTHY),
#         Agent("Zoe", Condition.DEAD),
#     )
#     result = meetup(agent_list)
#     print("Question 2 solution:")
#     for agent in result:
#         print(f"{agent.name}: {agent.category.name}")


