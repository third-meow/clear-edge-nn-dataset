## clear-edge neural net dataset

a simple dataset.

#### object extracted from file produced by `build_dataset.py` follows format:


    [[ shape, label ], ...
        ^       ^
        |        \
        |         \          >  0 0  or 1 0 or 1 1 or 0 1
                   \        /   1 1     1 0    0 0    0 1
     [[0, 0],       \      /
      [1, 1]]     1. : edge 
                  0. : non-edge
    

and there are the same number of edges as non-edges.

Enjoy :)


   

