Note that the following few assumptions are made for the query:
(a) If query length <6, then the search is made on all attributes of
    the extended dataset except storyline.
(b) If query length >5, then the search is made on the storyline only.
    The best matched entry is returned.

For example, one such example is:- 

If the user queries:
aamir salman

Output:-
Movie Recommended : 
Andaz apna apna

If the user queries:
Rohit Mehra

Output:-
Movie Recommended : 
Koi...Mil gaya

If the user queries:
Quantum

Output:-
Movie Recommended : 
Quantum of solace

If the user queries:
Quantum

Output:-
Movie Recommended : 
Quantum of solace

If the user queries:
Photograph plane college address student hindi

Output:-
Movie Recommended : 
3 idiots
We are marshell
Lord of the Flies
etc.
