# QuantumSanta

A small CLI app to distribute the roles for secret santa with true - quantum - randomness.
Based on the IBM-Qiskit Framwork and use the noise of their quantum system to obtain random numbers.

## A few disclaimers upfront:
- This is not an example for efficent use of ressources - in fact it is the complet opposite of it.
- In the current state the distributer - lets call them elfs - can see all the roles.
### Usage:
`./main.py [options]`

## How to use the current State:
- Edit the list in the script
- Add the provider
- Execute the script.

## How does it work:
1. The script reads the `config.json` file, if the file is not present it should get the data from the CLI arguments.
2. It calculates the curcit size based on the - very basic - formula:
`math.ceil(math.log2(num_participants**2))`.
3. It builds the quantum cuicuit, each q-bit is modified by a Hardamad gate, and then measured on a individual bit. The Hardamard Gate sets the possiblity for the events 0/1 to 1/sqrt(2).
4. It sends the requests to the quantum provider, base case is the ibm-quiskit system. (Test case is the ibm-simulator)
5. After recieving the response the strings of numbers got convertet from base-2 to base 10 mod `num_participants`.
6. The participants are given an index to rearange the order.
7. For each participant a recipiant is drawn.
When `participant_i` got `participant_j` assinged `j` is removed from the string of numbers.
8. Step 7 is repeated until every participant as someone to send a gift to or there are no numbers left.
9. A few basic checks are performed to evaluate the output.
10. The output is printed in the console.


## Roadmap:
- ~~Add Explanation to README~~~
  - improve explanation with images
- Save Output in file!
  - Save output in an encrypted file
- ~~Add CLI commands~~
- ~~Remove hard coded list~~
- Let the elfs participate:
  - Host a microserver and obtain links
  - Send mails automaticly /SMS accordingly
