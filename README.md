## To-do: 

* Add fitness function to select seed node:
  * Fi = fin/(fin + fout)^2     
    fin = no.of incoming edges of node  
    fout = no.of outgoing edges of node
* Fitness function to select seed node based on truthfulness:
  * Fi =∑ i=1wi. fin ∕ (fin+ fout)2     
    wi = Edge weight of trusted message propagation
    