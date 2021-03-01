# maximum and minimum degree  
def identify_router (edges, leng) :  
  
    # Map to store the degrees of every node  
    m = {}; 
      
    for i in range(leng) : 
        m[edges[i][0]] = 0; 
        m[edges[i][1]] = 0; 
          
    for i in range(leng) : 
          
        # Storing the degree for each node 
        m[edges[i][0]] += 1; 
        m[edges[i][1]] += 1;  
  
    # maxi and mini variables to store the maximum and minimum degree  
    maxi = 0;  
    for i in m.keys() : 
        maxi = max(maxi, m[i]);  

    # Printing all the nodes  with maximum degree  
    print("Nodes with maximum degree : ",  end = "") 
      
    for i in m.keys() : 
        if (m[i] == maxi) : 
            print(i, end = " ");  
  
    print() 

  
# Driver code  
if __name__ == "__main__" :  
  

    # The edge list  
    #edges1 = 1 -> 2 -> 3 -> 5 -> 2 -> 1 
	#edges2 = 1 -> 3 -> 5 -> 6 -> 4 -> 5 -> 2 -> 6 
    #edge3 = 2 -> 4 -> 6 -> 2 -> 5 -> 6 = 2, 6
    
    # Count of nodes and edges 

    m1 = 5;  
    edges1 = [[ 1, 2 ], [ 2, 3 ],  [ 3, 5 ], [ 5, 2 ],  [ 2, 1 ]];
    print("\n printing for edges1: ")
    identify_router (edges1, m1); 

    n2 = 5; m2 = 7;  
    edges2 = [[ 1, 3 ], [ 3, 5 ],  [ 5, 6 ], [ 6, 4 ],  [ 4, 5 ], [ 5, 2 ], [ 2, 6 ]];
    print("\n printing for edges2: ")
    identify_router (edges2, m2);  

    n3 = 4; m3 = 5;  
    edges3 = [[ 2, 4 ], [ 4, 6 ],  [ 6, 2 ], [ 2, 5 ],  [ 5, 6 ]];    
    print("\n  printing for edges3: ")
    identify_router (edges3, m3); 

# time complexity of identify_router function is O(n)