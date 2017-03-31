# BitCiv
My first large project. Think virtual ant farm.


Current roadmap, subject to incredible change:

V0.1.0 Class layout complete, basic engine and manager layout complete, essentially just empty functions with some comments.
V0.2.0 Initializations working. Simple engine loop for running. 
V0.3.0 Web hosting working, very simple representation of 2d field. 
V0.4.0 Entity breeding mechanically available.
V0.5.0 Basic decision making based on personal priorities.
V0.6.0 Food exists and entities understand to seek it out and eat it.
V1.0.0 Entities should exist, and be viewable from the web portal. Entities should be able to understand they are hungry and seek out food.
        Entities should be able to understand other entities existing. Breeding should be possible yet random. Breeding only occurs when not hungry.

Broad goal milestones:
V2.0.0 Smarter Entities, "know" other entities. Allow basic combat/running. Figure out staying near food may be a positive.
V3.0.0 Grouping. Allow multiple entities to band together to form a town. Town should have its own representation based on stats of founders
        Allow entities to collect food and bring to town for storage.
V4.0.0 Ultimate goal. Once basic aspects are fleshed out, work primarily on "black box" decision maker. Have priorities feed into a NN? 
        Maybe use a roulette wheel system which scales not only based on priorities but also on current needs.
