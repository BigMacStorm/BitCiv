# BitCiv
This is a server engine entity which will host a game world filled with "Ant" entities, which will have their own brains and decision making. Some of the things I hope to get them to accomplish are:

Eat
Drink
Breed
Die
Think

# Current plan
Each ANT is going to have its own NN. When an ant decides to take the breed action (more on that later), the two NN will spawn another X NN, based on averaging and random mutations. As the ANT lives its life, it will have a cumulative score. Score will be affected by such things as eating when hungry, drinking when thirsty, being around friendly ants, winning combat if they are agressive, creating offspringm. When two ANTs breed, the score will factor into how much mutation, or which parent to derive more traits (nuerons probably) from.

The NN will take the state of the ant as an input layer, and the output layer will consist of a single int between 1 and X, X being the number of action states. These states are currently something akin to: Idle, Attack, Forage (look for food/water to store in memory), Drink (drink water if near, or move towards closest known water that wasnt seen too long ago), Eat (same idea as drink, but for food), Run (run away from another ANT or a possible predator), Play (ANTs who play will follow another ANT around, and remember them as a friend), Mate (will attempt to mate with another ANT, which could either result in offspring, the other ant fleeing, or even an attack). 

Each section of the game will be handled by a manager. Currently the managers are:

Entity manager - Will handle all ants and food.

World manager - Will handle world events, such as growth of trees (obstacles), water appearing after a rain event, food growing, and in the event of mass extinction, creation of a new world with new entities

Network manager - The network manager keeps a running list of the state of each other manager, and provides it through self hosted websockets, which will allow a visual interface for the ants at a later point

More possibly TBD

The engine itself will run each manager, and will only be directly handled by the top level model, which will host a simple UI for controlling the simulation through a form (hopefully using a simple MVVM set up)

Todo
- [ ] Create the Engine model class and the view/view model to go with it
- [ ] world manager to act as director, place food, reset on exitnction, etc
- [ ] ES NN
- [ ] Add food
- [ ] Make the ANTs need food, allow them to eat
