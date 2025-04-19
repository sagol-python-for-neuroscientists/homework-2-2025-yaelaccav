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
    """Model the outcome of the meetings of pairs of agents.

    The pairs of agents are ((a[0], a[1]), (a[2], a[3]), ...). If there's an uneven
    number of agents, the last agent will remain the same.

    Parameters
    ----------
    agent_listing : tuple of Agent
        A listing (tuple in this case) in which each element is of the Agent type, 
        containing a 'name' field and a 'category' field, with 'category' being 
        of the type Condition.

    Returns
    -------
    updated_listing : list
        A list of Agents with their 'category' field changed according to the result of the meeting.
    """
    updated_agents = list(agent_listing)

    for i, (a1, a2) in enumerate(zip_longest(agent_listing[::2], agent_listing[1::2])):
        if a2 is None:
            continue  # Odd number of agents, last one stays unchanged

        if a1.category in (Condition.HEALTHY, Condition.DEAD) or a2.category in (Condition.HEALTHY, Condition.DEAD):
            continue  # Healthy and Dead agents do not participate

        # If one is Cure, try to improve the other
        if a1.category == Condition.CURE and a2.category != Condition.CURE:
            updated_agents[2*i+1] = Agent(a2.name, improve(a2.category))
            continue
        elif a2.category == Condition.CURE and a1.category != Condition.CURE:
            updated_agents[2*i] = Agent(a1.name, improve(a1.category))
            continue
        elif a1.category == Condition.CURE and a2.category == Condition.CURE:
            continue  # Cure does not affect another Cure

        # If both are Dying, both become Dead
        if a1.category == Condition.DYING and a2.category == Condition.DYING:
            updated_agents[2*i] = Agent(a1.name, Condition.DEAD)
            updated_agents[2*i+1] = Agent(a2.name, Condition.DEAD)
        else:
            # Infected agents worsen each other
            updated_agents[2*i] = Agent(a1.name, worsen(a1.category))
            updated_agents[2*i+1] = Agent(a2.name, worsen(a2.category))

    return updated_agents

if __name__ == "__main__":
    # Sample test for Question 2
    agent_list = (
        Agent("Alice", Condition.SICK),
        Agent("Bob", Condition.DYING),
        Agent("Curey", Condition.CURE),
        Agent("Dana", Condition.DYING),
        Agent("Eli", Condition.HEALTHY),
        Agent("Zoe", Condition.DEAD),
    )

    result = meetup(agent_list)
    print("Question 2 solution:")
    for agent in result:
        print(f"{agent.name}: {agent.category.name}")

