# QuantumSanta

A small CLI app to distribute the roles for secret santa with true - quantum - randomness.
Based on the IBM-Qiskit Framwork and use the noise of their quantum system to obtain random numbers.

# A few disclaimers upfront:
- This is not an example for efficent use of ressources - in fact it is the complet opposite of it.
- In the current state the distributer - lets call them elfs - can see all the roles.

# How to use the current State:
- Edit the list in the script
- Add the provider
- Execute the script.

# Roadmap:
- Add CLI commands
- Remove hard coded list
- Let the elfs participate:
  - Host a microserver and obtain links
  - Send mails automaticly
