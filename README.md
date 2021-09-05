# Election-Analysis

## Project Overview
A Colorado Board of Elections employee has give you the following tasks to complete the election audit of a recent local congressional election.

## Election Audit Roadmap
1. Calculate the total votes cast.
2. Get a complete list of counties who received votes.
3. Calculate the total number of votes each county received.
4. Calculate the percentage of votes cast per ocunty.
5. Determine the largest county turnout.
6. Get a complete list of candidates who received votes.
7. Caluculate the total number of votes each candidate received.
8. Calculate the percentage of votes each candidate won.
9. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_recults.csv
- Software Python 3.9, Visual Studio Code 1.60

## Election Audit Results
The analysis of the election shows that:
- There were __369,711__ votes cast in the election.
- The counties were:
    - Jefferson
    - Denver
    - Araphoe
- The county results were:
    - Jefferson received __10.5%__ of the vote and __38,855__ number of votes.
    - Denver received __82.8%__ of the vote and __306,055__ number of votes.
    - Arapahoe received __6.7%__ of the vote and __11,606__ number of votes.

- The candidates were: 
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane

- The candidate results were:
    - Charles Casper Stockham received __23%__ of the vote and __85,213__ number of votes.
    - Diana DeGette received __73.8%__ of the vote and __272,892__ number of votes.
    - Raymon Anthony Doane receoved __3%__ of the vote and __11,606__ number of votes.

- The winner of the election was:
    - Diana Degette, who received __73.8%__ of the vote and __272,892__ number of votes.

## Election Audit Summary
For this auditing tool, it can easily be modified to perform an analysis on any election, given that the dataset is in a ___Commma Separated Value (.CSV)___ format. By simply changing or adding the counties and candidate names, we can still determine any county's turnout and any candidate's performance in an election. If one should use the tool for a different dataset, we must ensure that the data source file is in format as show on image below -
<br>

![image](https://raw.githubusercontent.com/RobC30/Election-Analysis/main/Resources/csv%20format.PNG)
<br>

If we are to increase our analysis reach towards different states, we simply need to assign new variables & add a few lines of code to determine state turnouts, essentially auditing a country's election results. Much like how we reused code to determine the winning candidates and transorming it into county turnouts, we can use the same code with different assigned variables to determine state turnouts. Here are the steps to add a __State Analysis__:

1. Create a State list & State votes dictionary
2. Assign trackers for the largest state & state voter tunrout
3. Extract State from each row
4. Modify _if statement_ to create a list of states and add into code
5. Start a state vote count
6. Adding a vote to that state's vote count
7. Write a for loop with necessary calculations to determine a state's total votes & percentage vs. all states
8. Determine largest State turnout.

See below preview of what new lines of code might look like to create a __State Analysis__:

![image](https://raw.githubusercontent.com/RobC30/Election-Analysis/main/Resources/state.PNG)