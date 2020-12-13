
# Meta Quantum Circuits with Constraints

This repository contains the instructions for running and the source code organization for a quantum meta-programming framework, which is the primary software artifact for the paper

*Haowei Deng, Yuxiang Peng, Michael Hicks, Xiaodi Wu. Automating NISQ Application Design with Meta Quantum Circuits with Constraints (MQCC)*
[paper link here]()

Near-term quantum computers are likely to have very restricted hardware resources, where precisely controllable qubits are expensive, error-prone, and scarce. Therefore, application designers for such near-term intermediate scale quantum (NISQ) computers are forced to investigate the best balance of trade-offs among a large number of (potentially heterogeneous) factors specific to the targeted application and quantum hardware. 
Meta Quantum Circuits with Constraints (MQCC) is a meta-programming framework to assist quantum application designers. Designers express their application as a succinct collection of normal quantum circuits stitched together by a set of meta-level choice variables, whose values are constrained according to a programmable set of quantitative optimization criteria. MQCC’s compiler automatically generates the appropriate constraints, hands them to a solver (e.g., a Satisfiability Modulo Theories (SMT) solver), and from the solution produces an optimized, runnable program. 

For example, below is a simple MQCC program

```c
fcho c1 = {0, 1};
qreg q[3];

h(q[0]);
cnot(q[0],q[1]);

choice (c1){
    0 : cnot(q[0],q[1]);
        h(q[0]);

    1 : h(q[0]);
}
```
The first statement _fcho c1 = {0, 1};_ declares a choice variable *c1* whose value ranges in {0, 1}. The value of variable *c1* decides which branch in the *choice* block below is valid. If you let the MQCC compiler calculate the gate number in the program, MQCC will generate a cost expression
```c
gateNum:  2 + ([c1,0]*2 + [c1,1]*1)
```
In the output expression, term [c1, n] means: [c1, n] = 1 if c1 == n else 0. Thus the total gate number in the program is: 4 if c1 == 0, 3 if c1 == 1. If user wants to minimize the total gate number of the program, MQCC will let c1 be 1 and generate the corresponding fixed-choice MQCC program which contains only 3 gates.
```c
fcho c1 = {0, 1};
qreg q[3];

h(q[0]);
cnot(q[0],q[1]);
h(q[0]);
```
The whole syntax of MQCC program is [here](doc/MQCC_syntax.md)

# Release Information

## Supported Operating Systems

Linux OS. Ubuntu 16.04 or later version is better.
For Windows 10 users, you can install Windows Subsystem for Linux (WSL) following the microsoft manual [here](https://docs.microsoft.com/en-us/windows/wsl/install-win10#:~:text=Windows%20Subsystem%20for%20Linux%20Installation%20Guide%20for%20Windows,...%207%20Set%20up%20a%20new%20distribu%20)

## Prerequisites
### For Ubuntu

MQCC is implemented based on Python 3. To run MQCC, python-ply is needed. You can install python-ply from the [source code](https://www.dabeaz.com/ply/) or install python-ply through **pip**
```
sudo pip install ply
```

MQCC also uses z3 SMT solver. It can be installed through **pip**
```
sudo pip install z3-solver
```

# Installation
Clone this repository and cd to the root directory. Run the command below to test MQCC successfully solving the multi-proramming problem.
```
sh run.sh test/example
```
If MQCC prints a solution model, you install MQCC successfully.

# Using MQCC

## Object Specification

To solve problems with MQCC, you need to define your goal and constraint objects and specify your objects' goal or constraints. Each object is defined by a python class. The manual of how to define objects is [here](doc/object_doc.md). There is a file "YourObject.py" in the root directory and you can define your objects' python class in it. MQCC receives your object specification through a python file "Attr.py" in the root directory, which imports all objects you define in the YourObject.py. It also imports some example objects we have already defined, and you can use them directly. 

In Attr.py, there is an *ObjectSet* dictionary referring to your goal object and constraint objects. You need to modify it to specify your objects of interest, along with an optimization goal or some constraints. You should define *ObjectSet* in the below format.

```python
ObjectSet = {ObjectName : (ObjectClass, Goal | Constraint, [OptKind]), ...,}
```
Each object is a key-value item. Each key is a string denoting a object's name. The corresponding value is a python tuple.

- The tuple's first element is the corresponding python class of the object. 
- The second element is a string denoting the goal or constraints of the object. If the object is a goal object, the tuple's second element should be a string  "min" or "max" to let MQCC find the minimum or maximum of the object. There can be one and only one goal object in the *ObjectSet*. If it is a constraint object, its *Constraint* consists of a relation operator's string and the string of the range. The relation operator can be "<", ">", "<=" or ">=". The range can be an arbitrary real number. For example, "<1.4" means to let MQCC keep the value of this object <1.4. 
- If the object is additive, the tuple has a third element, 'add' . MQCC can generate simpler cost expressions for additive objects and solve the problem faster.
  
For example, the *ObjectSet* below:
  
```python
ObjectSet = {'Depth': (Depth, 'min'), 'Noise': (Noise, '<0.15', 'add')}
```
It specifies two objects to MQCC, circuit depth define by a python class **Depth** and noise defined by class **Noise**. It suggests MQCC find the minimum of the circuit depth while keeping the program's noise less than 0.4. It also indicates the noise object is additive.

## Run MQCC

After modifying the Attr.py file to give your object specification, you can run MQCC on your target MQCC program with the command
```
sh run.sh targetfile
```
MQCC will use z3 solver to solve the problem and print out the result value of all the program's free choice variables. MQCC will generate two more files

- Your specified objects' cost expressions will be written into the file "Expressions" in the root directory.
- A fixed choice MQCC program where all choice statements are chosen based on the choice variable's result value will also be generated in the file "Fixed-choice MQCC" in the root directory.

If you only want MQCC to generate the cost expressions for all objects and not to waste time solving the problem with z3, you can use the command
```
sh run.sh -d targetfile
```
MQCC will not call z3 solver and only generate the object expressions in file "Expressions".

# Example
We use MQCC to solve several optimization problems as examples of MQCC applications, and you can find these example projects [here](doc/examples.md). The example projects include the problem we solve in the paper, and you can run commands below to test the example projects.

- Solve multi-programming problem
  ```sh
  sh run.sh -e 1 test/example
  ```
- Crosstalk mitigation
  ```sh
  sh run.sh -e 2 test/crosstalk
  ```
- Delayed uncomputation
  ```sh
  sh run.sh -e 3 test/belle
  ```

