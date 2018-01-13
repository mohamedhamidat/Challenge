-- Create a graph database
CREATE DATABASE graphdb;
go

USE  graphdb;
go

--Create Graph table
create table Graph (
  Id VARCHAR(10) not null PRIMARY KEY,
  GraphName VARCHAR(100) not null);


-- Create NODE table
CREATE TABLE Node (
  Id VARCHAR(10) not null PRIMARY KEY, 
  NodeName VARCHAR(100) not null,
  GraphId VARCHAR(10) not null REFERENCES Graph(Id),
) AS NODE;

-- Create EDGE table. 
 CREATE TABLE Edge (
    Id integer PRIMARY KEY,
    FromNode VARCHAR(10) not null references Node(Id),
    ToNode VARCHAR(10) not null references Node(Id),
    Cost FLOAT (10, 3) not null default 0,
    GraphId VARCHAR(10) not null REFERENCES Graph(Id),
 ) AS EDGE;



-- We have a Node table which contains the nodes with Id and Name 
-- Edge table which lists the connections, the edges, between the nodes. 
-- It references the graph table in Node and edge tables . 

-- The node Id is the primary key of the node table and the clustered index of this table. 
-- The edge Id is the primary key of the Edge table as we assume we can only have one edge going in the same direction
-- between two nodes. 
-- Cost by default are 0,
