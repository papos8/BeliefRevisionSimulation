# BeliefRevisionSimulation
Repository to store the code for Master Thesis

This repository stores the code for simulation of belief revision and truth tracking.
This simulation is a part of the Master Thesis - Formal Models of Cognitive Bias in Artificial Intelligence and Multi-agent Systems.

Author: Panagiotis Papadamos
Student Number: s205637
Email: panagiotispapadamos@gmail.com

# Project's Description
An implementation of Artificial Intelligence agents is stored in the repository. The main concept of the project is the update of an agent's belief, based on the incoming information.

Three methods introduced in 'Truth-Tracking by Belief Revision, Baltag, Gierasimczuk and Smets' are implemented and 9 more are proposed, as well as implemented on the project. The unbiased methods, namely conditioning, lexicographic revision and minimal revision are compared to the proposed ones namely:
1. Confirmation bias conditioning
2. Confirmation bias lexicographic revision 
3. Confirmation bias minimal revision
4. Framing bias conditioning
5. Framing bias lexicographic revision
6. Framing bias minimal revision
7. Anchoring bias conditioning
8. Anchoring bias lexicographic revision
9. Anchoring bias minimal revision
10. In-group favoritism conditioning
11. In-group favoritism lexicographic revision
12. In-group favoritism minimal revision

# Project's stucture
The class **Agent** is the brain of the artificial intelligence agents. All the belief revision methods are part of the **Agent** class. Additionally, functions related to the belief revision functions, such as the framing function, are part of the same class. An object of this class can be constructed either automatically or manually by the user. The constructor of the class receives three arguments, an **Epistemic Space**, the bias of the agent and the type of the agent (if not "Custom" the agent is created automatically). The **Epistemic Space** takes as arguments **States** and **Observables**. After an agent's instantiation the user can pass information to the agent as propositions ad the agent will revisethe epistemic space based on this inforamition.

# main.py
The file **main.py** includes the tests cases we ran to compare the methods. The user can run the file in two ways. The first way is to run the file without an additional argument. The user will receive a prompt from the terminal to enter a number and select a test case. The prompt looks like the image below. 

![Alt](https://github.com/papos8/BeliefRevisionSimulation/blob/main/Images/TerminalMessage.png)

The second way is to pass the number directly as an argument on the command line. For example, **python main.py 4** will run prompt the user to create step by step a custom test to compare framing bias conditioning and unbiased conditioning. 
Note that if the user selects randomly created tests then the 200 test cases run and the results are stored under the folder **Randomly_Created_Tests** on the same repository.
