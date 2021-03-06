﻿[![Build Status](https://travis-ci.org/mohamedhamidat/Challenge.svg?branch=master)](https://travis-ci.org/mohamedhamidat/Challenge)


##Challenge for XX company's interview 




Consider the following XML sample intended to model a directed graph.
```
<graph>
    <id>g0</id>
    <name>The Graph Name</name>
    <nodes>
        <node>
            <id>a</id>
            <name>A</name>
        </node>
        <node>
            <id>b</id>
            <name>B</name>
        </node>
....
    </nodes>
    <edges>
        <node>
            <id>4</id>
            <from>C</from>
            <to>D</to>
            <cost>3</cost>
        </node>
        <node>
            <id>5</id>
            <from>B</from>
            <to>E</to>
            <cost>2</cost>
        </node>
.....
    </edges>
</graph>
```
Write a program in your favorite language to:
1. Download a text file containing an XML file like the one described.
2. Parse the file to make sure it is syntactically and semantically correct subject to the following restrictions:
• There must be an &lt;id&gt; and &lt;name&gt; for the &lt;graph&gt;.
• Assume the &lt;nodes&gt; group will always come before the &lt;edges&gt;group.
• There must be at least one &lt;node&gt; in the &lt;nodes&gt; group.
• All nodes must have different &lt;id&gt; tags.
• For every &lt;edge&gt;, there must be a single &lt;from&gt; tag and a single
&lt;to&gt; tag, corresponding to nodes that must have been defined before.
• The &lt;cost&gt; tag is optional and can provide an arbitrary non-negative
floating point number. If it’s not present, then the cost for the &lt;edge&gt;
defaults to zero.
You’d have chosen an XML parsing library for your favorite programming
language to tackle this task. Please explain why you chose the particular
library.
3. Propose a normalized SQL schema to model this graphs in PostgreSQL
using standard SQL data types only.
Please explain briefly each attribute and relationship you propose. You
can use SQL documentation facilities and comments in order to do that.
4. Write an SQL query that finds cycles in a given graph, according to the
data model you proposed on item (3). You can use standard SQL99 or
PL/pgSQL functions.
5. Suppose there’s a frontend application where end-users can create queries
having this JSON form
{
"queries" : [
...
"paths" : {
"start" : "a",
"end" : "e"
},
...
"cheapest" : {
"start" : "a",
"end" : "e"
},
...
]
}
Write a program that receives this structure via standard input, queries
the database, and answers via standard output. The possible queries are
to be interpreted as follows:
• There can be many interleaved paths and cheapest queries, but at
least one query.
• A single JSON document should be emitted, holding all the answers.
• Each paths query must return a list of possible paths between the
start and end nodes referenced by id, if there are paths between
them; an empty list if there aren’t any paths from start to end. If
the graph has cycles, they are to be ignored.
A sample answer could be:
{
"answers" : [
...
"paths" : {
"from" : "a",
"to" : "e",
"paths" : [ [ "a", "b", "e" ], [ "a", "e" ] ]
},
...
]
}
assuming there are paths a-&gt;b-&gt;e and a-&gt;e.
• Each cheapest query must return the cheapest path between the
start and end nodes referenced by id, if there’s at least one path; a
false value if there aren’t any paths from start to end. If the graphs
has cycles, they are to be ignored.
A sample answer could be:
{
"answers" : [
...
"cheapest" : {
"from" : "a",
"to" : "e",
"path" : [ "a", "e" ]
},
...
"cheapest" : {
"from" : "a",
"to" : "h",
"path" : false,
},
...
]
}

assuming a-&gt;e is the cheapest path, and there’s no path from a to h.
You’d have chosen a JSON parsing/serialization library for your favorite
programming language to tackle this task. Please explain why you chose
the particular libraries.
Please explain how you solved the “are there any paths” and the “cheapest
path” problems.

