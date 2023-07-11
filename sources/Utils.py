from igraph import *
import os

def addVertex(g,name_str):
    try:
        if (name_str not in g.vs['name']):
            print("Inserted node",name_str)
            g.add_vertex(name = name_str)
        else:
            print("Node ",name_str, " already added")
            print(g.vs.find(name_str).index)
    except KeyError:
        g.add_vertex(name = name_str)
    return g 

def Write(f,t):
    string = str(t[0])+" "+str(t[1])+'\n'
    f.write(string)

def Retrieve(g,t):
    a = (g.vs[t[0]]['name'],g.vs[t[1]]['name'])
    return a 

def LoadData(filename,g,path):
    filenums = [0]
    for i,num in enumerate(filenums):
        print(num)
        filename = path+str(num)+".edges"
        print("filename: ",filename)
        f = open(filename)
        line = f.readline()
        while(line!=""):
            c = (line.split())
            g = addVertex(g,c[0])
            g = addVertex(g,c[1])
            g.add_edge(c[0],c[1])
            line = f.readline()
    g.simplify()
    return
